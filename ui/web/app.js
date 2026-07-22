"use strict";

const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
const NS = "http://www.w3.org/2000/svg";

const state = {
  status: null,
  facility: null,
  scenario: null,
  fromTo: "",
  names: { facility: "", scenario: "", fromTo: "", cad: "" },
  cadFile: null,
  analysis: null,
  manifest: null,
  trace: "",
  selected: null,
  zoom: 1,
  prototype: null,
  bottleneckScores: null,
};

const viewInfo = {
  workspace: ["워크스페이스", "물류 흐름을 한 화면에서 실험합니다"],
  inputs: ["입력 · CAD", "실제 모델 데이터를 연결합니다"],
  analysis: ["Flow 분석", "실제 Core 분석 결과를 확인합니다"],
  simulation: ["시뮬레이션", "결정론적 이벤트 실행을 제어합니다"],
  lab: ["Future Lab", "다음 기능의 사용 경험을 먼저 검증합니다"],
};

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function formatNumber(value, maximumFractionDigits = 1) {
  const number = Number(value);
  if (!Number.isFinite(number)) return "—";
  return new Intl.NumberFormat("ko-KR", { maximumFractionDigits }).format(number);
}

function formatBytes(bytes) {
  if (!Number.isFinite(bytes)) return "";
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
  return `${(bytes / 1024 / 1024).toFixed(1)} MB`;
}

function toast(message, type = "info") {
  const item = document.createElement("div");
  item.className = `toast ${type}`;
  item.textContent = message;
  $("#toastStack").append(item);
  setTimeout(() => item.remove(), 3800);
}

function setLoading(active, title = "Core 실행 중", sub = "입력과 결과를 안전하게 분리하고 있습니다.") {
  $("#loadingOverlay").hidden = !active;
  $("#loadingTitle").textContent = title;
  $("#loadingSub").textContent = sub;
}

async function api(path, options = {}) {
  const response = await fetch(path, {
    headers: options.body ? { "Content-Type": "application/json" } : undefined,
    ...options,
  });
  let payload;
  try {
    payload = await response.json();
  } catch {
    throw new Error(`서버 응답을 해석할 수 없습니다. (HTTP ${response.status})`);
  }
  if (!response.ok) throw new Error(payload.error || `HTTP ${response.status}`);
  return payload;
}

function switchView(view) {
  if (!viewInfo[view]) return;
  $$(".nav-item").forEach((button) => button.classList.toggle("active", button.dataset.view === view));
  $$(".view").forEach((section) => section.classList.toggle("active", section.id === `view-${view}`));
  $("#viewCrumb").textContent = viewInfo[view][0];
  $("#viewTitle").textContent = viewInfo[view][1];
  $("#prototypeNotice").hidden = view !== "lab";
  if (view === "workspace") requestAnimationFrame(renderNetwork);
}

function demandRows() {
  if (state.fromTo.trim()) {
    return state.fromTo.trim().split(/\r?\n/).slice(1).filter((line) => line.trim());
  }
  return Array.isArray(state.scenario?.from_to_demands) ? state.scenario.from_to_demands : [];
}

function updateReadiness() {
  const items = [
    ["Facility", Boolean(state.facility), state.names.facility || "파일을 선택하세요", "#readyFacility", "#facilityName"],
    ["Scenario", Boolean(state.scenario), state.names.scenario || "파일을 선택하세요", "#readyScenario", "#scenarioName"],
    ["Demand", demandRows().length > 0, state.names.fromTo || (demandRows().length ? "Scenario 내부 수요" : "선택 입력입니다"), "#readyDemand", "#demandName"],
  ];
  for (const [, ready, name, icon, label] of items) {
    $(icon).classList.toggle("done", ready);
    $(icon).textContent = ready ? "✓" : $(icon).id.slice(-1);
    $(label).textContent = name;
  }
  $("#nodeMetric").textContent = formatNumber(state.facility?.nodes?.length, 0);
  $("#edgeMetric").textContent = formatNumber(state.facility?.edges?.length, 0);
  $("#stationMetric").textContent = formatNumber(state.facility?.stations?.length, 0);
  $("#demandMetric").textContent = formatNumber(demandRows().length, 0);

  const scenario = state.scenario;
  $("#simScenario").textContent = scenario?.scenario_id || "—";
  $("#simDuration").textContent = scenario ? `${formatNumber((scenario.duration_us || 0) / 1_000_000)} s` : "—";
  $("#simVehicles").textContent = scenario ? `${scenario.vehicles?.length || 0} 대` : "—";
  $("#simJobs").textContent = scenario ? `${scenario.jobs?.length || 0} 건` : "—";
  $("#simSeed").textContent = scenario?.master_seed ?? "—";
}

function svgElement(name, attributes = {}) {
  const element = document.createElementNS(NS, name);
  for (const [key, value] of Object.entries(attributes)) element.setAttribute(key, String(value));
  return element;
}

function heatColor(ratio) {
  const bounded = Math.max(0, Math.min(1, Number(ratio) || 0));
  const hue = 184 - bounded * 152;
  const light = 48 + bounded * 12;
  return `hsl(${hue} 78% ${light}%)`;
}

function networkTransform() {
  const nodes = state.facility?.nodes || [];
  const points = nodes.map((node) => node.position_um).filter(Boolean);
  if (!points.length) return null;
  const xs = points.map((point) => Number(point.x) || 0);
  const ys = points.map((point) => Number(point.y) || 0);
  const minX = Math.min(...xs), maxX = Math.max(...xs);
  const minY = Math.min(...ys), maxY = Math.max(...ys);
  const width = Math.max(1, maxX - minX);
  const height = Math.max(1, maxY - minY);
  const padding = 65;
  const scale = Math.min((900 - 2 * padding) / width, (460 - 2 * padding) / height);
  const usedWidth = width * scale;
  const usedHeight = height * scale;
  const offsetX = (900 - usedWidth) / 2;
  const offsetY = (460 - usedHeight) / 2;
  return (point) => ({
    x: offsetX + ((Number(point.x) || 0) - minX) * scale,
    y: 460 - (offsetY + ((Number(point.y) || 0) - minY) * scale),
  });
}

function renderNetwork() {
  const svg = $("#networkCanvas");
  svg.replaceChildren();
  const facility = state.facility;
  const transform = networkTransform();
  $("#emptyCanvas").hidden = Boolean(facility && transform);
  if (!facility || !transform) return;

  const defs = svgElement("defs");
  const marker = svgElement("marker", { id: "arrow", viewBox: "0 0 10 10", refX: 8, refY: 5, markerWidth: 4, markerHeight: 4, orient: "auto-start-reverse" });
  marker.append(svgElement("path", { d: "M 0 0 L 10 5 L 0 10 z", fill: "context-stroke" }));
  defs.append(marker);
  svg.append(defs);

  const flowByEdge = new Map((state.analysis?.edge_flows || []).map((item) => [item.edge_id, item]));
  const scoreByEdge = state.bottleneckScores || new Map();
  const edgeLayer = svgElement("g", { class: "edge-layer" });
  for (const edge of facility.edges || []) {
    const sourcePoints = edge.polyline_um?.length ? edge.polyline_um : [];
    if (sourcePoints.length < 2) continue;
    const points = sourcePoints.map(transform).map((point) => `${point.x.toFixed(2)},${point.y.toFixed(2)}`).join(" ");
    const flow = flowByEdge.get(edge.id);
    const prototypeScore = scoreByEdge.get(edge.id)?.score;
    const ratio = prototypeScore ?? flow?.flow_share ?? 0;
    const polyline = svgElement("polyline", {
      points,
      class: `network-edge${state.selected?.type === "edge" && state.selected.id === edge.id ? " selected" : ""}`,
      "data-id": edge.id,
      "marker-end": "url(#arrow)",
    });
    if (flow || Number.isFinite(prototypeScore)) {
      polyline.style.stroke = heatColor(ratio);
      polyline.style.strokeWidth = String(3 + Math.min(8, ratio * 12));
    }
    polyline.addEventListener("click", () => selectEntity("edge", edge.id));
    edgeLayer.append(polyline);
  }
  svg.append(edgeLayer);

  const nodeLayer = svgElement("g", { class: "node-layer" });
  for (const node of facility.nodes || []) {
    if (!node.position_um) continue;
    const point = transform(node.position_um);
    nodeLayer.append(svgElement("circle", { cx: point.x, cy: point.y, r: 4.5, class: "network-node" }));
  }
  svg.append(nodeLayer);

  const nodeMap = new Map((facility.nodes || []).map((node) => [node.id, node]));
  const stationLayer = svgElement("g", { class: "station-layer" });
  for (const station of facility.stations || []) {
    const node = nodeMap.get(station.attachment_node_id);
    const position = station.position_um || node?.position_um;
    if (!position) continue;
    const point = transform(position);
    const circle = svgElement("circle", {
      cx: point.x,
      cy: point.y,
      r: 8,
      class: `network-station${state.selected?.type === "station" && state.selected.id === station.id ? " selected" : ""}`,
      "data-id": station.id,
    });
    circle.addEventListener("click", () => selectEntity("station", station.id));
    const label = svgElement("text", { x: point.x + 11, y: point.y - 10, class: "network-label" });
    label.textContent = station.id;
    stationLayer.append(circle, label);
  }
  svg.append(stationLayer);
  svg.style.transform = `scale(${state.zoom})`;
}

function selectEntity(type, id) {
  state.selected = { type, id };
  const collection = type === "edge" ? state.facility?.edges : state.facility?.stations;
  const item = collection?.find((candidate) => candidate.id === id);
  if (!item) return;
  $("#inspectorEmpty").hidden = true;
  $("#inspectorContent").hidden = false;
  const flow = type === "edge" ? state.analysis?.edge_flows?.find((candidate) => candidate.edge_id === id) : state.analysis?.station_flows?.find((candidate) => candidate.station_id === id);
  const properties = type === "edge" ? [
    ["From → To", `${item.from_node_id} → ${item.to_node_id}`],
    ["Length", `${formatNumber((item.length_um || 0) / 1_000_000, 3)} m`],
    ["Speed limit", `${formatNumber((item.speed_limit_um_per_s || 0) / 1_000_000, 2)} m/s`],
    ["Moves / hour", flow ? formatNumber(flow.expected_moves_per_hour, 2) : "분석 전"],
    ["Flow share", flow ? `${formatNumber(flow.flow_share * 100, 1)}%` : "분석 전"],
  ] : [
    ["Attached node", item.attachment_node_id],
    ["Operation", item.operation_type],
    ["Capacity / hour", formatNumber(item.handling_capacity_per_hour, 1)],
    ["Peak / hour", flow ? formatNumber(flow.peak_moves_per_hour, 1) : "분석 전"],
    ["Utilization", flow ? `${formatNumber(flow.utilization_ratio * 100, 1)}%` : "분석 전"],
  ];
  $("#inspectorContent").innerHTML = `
    <span class="inspector-tag">${type.toUpperCase()}</span>
    <div class="inspector-title">${escapeHtml(id)}</div>
    <div class="property-list">${properties.map(([key, value]) => `<div><span>${escapeHtml(key)}</span><b>${escapeHtml(value)}</b></div>`).join("")}</div>`;
  renderNetwork();
}

async function readFile(input, kind) {
  const file = input.files?.[0];
  if (!file) return;
  if (file.size > 25 * 1024 * 1024) {
    toast("파일이 25 MB 제한을 초과했습니다.", "error");
    input.value = "";
    return;
  }
  try {
    if (kind === "cad") {
      state.cadFile = file;
      state.names.cad = file.name;
      $("#cadFileMeta").textContent = `${file.name} · ${formatBytes(file.size)}`;
      toast("CAD 파일 정보를 연결했습니다. 현재는 Import 계약 검사 단계입니다.", "success");
      return;
    }
    const text = await file.text();
    if (kind === "facility" || kind === "scenario") {
      const parsed = JSON.parse(text);
      state[kind] = parsed;
      state.names[kind] = file.name;
      $(`#${kind}FileMeta`).textContent = `${file.name} · ${formatBytes(file.size)}`;
      if (kind === "facility") {
        state.analysis = null;
        state.bottleneckScores = null;
        state.selected = null;
        renderAnalysis();
        renderNetwork();
      }
    } else {
      state.fromTo = text;
      state.names.fromTo = file.name;
      $("#demandFileMeta").textContent = `${file.name} · ${formatBytes(file.size)}`;
    }
    updateReadiness();
    toast(`${file.name} 연결 완료`, "success");
  } catch (error) {
    toast(`${file.name}을 읽지 못했습니다: ${error.message}`, "error");
  }
}

async function loadSample(showToast = true) {
  setLoading(true, "샘플 준비 중", "저장소의 Cross-Domain 예제를 불러옵니다.");
  try {
    const sample = await api("/api/sample");
    state.facility = sample.facility;
    state.scenario = sample.scenario;
    state.fromTo = sample.from_to;
    state.names = { ...state.names, ...sample.names };
    state.analysis = null;
    state.manifest = null;
    state.selected = null;
    state.bottleneckScores = null;
    $("#facilityFileMeta").textContent = sample.names.facility;
    $("#scenarioFileMeta").textContent = sample.names.scenario;
    $("#demandFileMeta").textContent = sample.names.from_to;
    updateReadiness();
    renderAnalysis();
    renderNetwork();
    if (showToast) toast("Cross-Domain 샘플을 불러왔습니다.", "success");
  } catch (error) {
    toast(error.message, "error");
  } finally {
    setLoading(false);
  }
}

function terminalText(result) {
  const command = `$ sim-core ${result.action}\n`;
  const stdout = result.stdout?.trim() || "";
  const stderr = result.stderr?.trim() || "";
  const meta = `\n\n[exit=${result.return_code} · ${formatNumber(result.elapsed_ms, 2)} ms · run=${result.run_id}]`;
  return command + (stdout || "(stdout 없음)") + (stderr ? `\n\n[stderr]\n${stderr}` : "") + meta;
}

async function executeCore(action) {
  if (action !== "replay" && (!state.facility || !state.scenario)) {
    toast("Facility와 Scenario를 먼저 연결해 주세요.", "error");
    switchView("inputs");
    return;
  }
  const titles = { validate: "모델 검증 중", analyze: "Flow Intelligence 실행 중", run: "결정론적 DES 실행 중", replay: "Trace 재생 중" };
  setLoading(true, titles[action], "C++ Core가 입력을 처리하고 있습니다.");
  try {
    const body = {
      action,
      facility: JSON.stringify(state.facility),
      scenario: JSON.stringify(state.scenario),
      from_to: state.fromTo,
      trace: state.trace,
    };
    const result = await api("/api/execute", { method: "POST", body: JSON.stringify(body) });
    const passed = result.ok;
    $("#runSummary").innerHTML = `<span class="run-state ${passed ? "pass" : "fail"}">${passed ? "PASS" : "FAIL"}</span><p>${escapeHtml(action)} · ${formatNumber(result.elapsed_ms, 2)} ms · exit ${result.return_code}</p>`;
    if (action === "validate") {
      $("#terminalOutput").textContent = terminalText(result);
      $("#terminalMeta").textContent = `${passed ? "PASS" : "FAIL"} · ${formatNumber(result.elapsed_ms, 2)} ms`;
      switchView("analysis");
    } else if (action === "analyze") {
      state.analysis = result.report || null;
      state.bottleneckScores = null;
      $("#terminalOutput").textContent = terminalText(result);
      $("#terminalMeta").textContent = `${passed ? "PASS" : "FAIL"} · ${formatNumber(result.elapsed_ms, 2)} ms`;
      renderAnalysis();
      renderNetwork();
      switchView("analysis");
    } else if (action === "run") {
      state.manifest = result.manifest || null;
      state.trace = result.trace || "";
      $("#simTerminal").textContent = terminalText(result);
      $("#simTerminalMeta").textContent = `${passed ? "COMPLETED" : "FAILED"} · ${formatNumber(result.elapsed_ms, 2)} ms`;
      renderManifest();
      switchView("simulation");
    }
    toast(`${titles[action]} — ${passed ? "완료" : "오류 확인 필요"}`, passed ? "success" : "error");
  } catch (error) {
    const target = action === "run" ? $("#simTerminal") : $("#terminalOutput");
    target.textContent = `[UI ERROR]\n${error.message}`;
    toast(error.message, "error");
  } finally {
    setLoading(false);
  }
}

function renderAnalysis() {
  const report = state.analysis;
  const edges = report?.edge_flows || [];
  const stations = report?.station_flows || [];
  const nodes = report?.node_flows || [];
  const diagnostics = report?.diagnostics || [];
  const errors = diagnostics.filter((item) => String(item.severity).toLowerCase() === "error").length;
  $("#analysisStatus").textContent = report ? (errors ? "FAIL" : "PASS") : "미실행";
  $("#analysisStatus").style.color = report ? (errors ? "var(--red)" : "var(--green)") : "";
  $("#analysisStatusSub").textContent = report ? `오류 ${errors} · 진단 ${diagnostics.length}` : "Core 결과 대기";
  $("#routeMetric").textContent = report ? formatNumber(report.demand_routes?.length || 0, 0) : "—";
  $("#topFlowMetric").textContent = report ? formatNumber(Math.max(0, ...edges.map((item) => Number(item.expected_moves_per_hour) || 0))) : "—";
  $("#mergeMetric").textContent = report ? formatNumber(Math.max(0, ...nodes.map((item) => Number(item.merge_pressure) || 0))) : "—";
  $("#exportReportButton").disabled = !report;

  const edgeBody = $("#edgeTableBody");
  if (!edges.length) {
    edgeBody.innerHTML = '<tr class="empty-row"><td colspan="4">분석을 실행하면 결과가 표시됩니다.</td></tr>';
  } else {
    edgeBody.innerHTML = [...edges].sort((a, b) => b.expected_moves_per_hour - a.expected_moves_per_hour).map((item) => `
      <tr><td><strong>${escapeHtml(item.edge_id)}</strong></td><td>${formatNumber(item.expected_moves_per_hour, 2)}</td><td>${formatNumber(item.flow_share * 100, 1)}%<span class="flow-bar"><i style="width:${Math.min(100, item.flow_share * 100)}%"></i></span></td><td>${formatNumber(item.demand_count, 0)}</td></tr>`).join("");
  }
  const stationBody = $("#stationTableBody");
  if (!stations.length) {
    stationBody.innerHTML = '<tr class="empty-row"><td colspan="4">분석을 실행하면 결과가 표시됩니다.</td></tr>';
  } else {
    stationBody.innerHTML = [...stations].sort((a, b) => b.utilization_ratio - a.utilization_ratio).map((item) => `
      <tr><td><strong>${escapeHtml(item.station_id)}</strong></td><td>${formatNumber(item.peak_moves_per_hour, 2)}</td><td class="${item.over_capacity ? "capacity-over" : "capacity-ok"}">${formatNumber(item.utilization_ratio * 100, 1)}%</td><td>${formatNumber(item.capacity_margin_per_hour, 2)}</td></tr>`).join("");
  }
}

function renderManifest() {
  const manifest = state.manifest;
  $("#simPlaceholder").hidden = Boolean(manifest);
  $("#manifestGrid").hidden = !manifest;
  if (!manifest) return;
  const values = [
    ["Status", manifest.status],
    ["Events", manifest.processed_event_count],
    ["Final time", `${formatNumber((manifest.final_simulation_time_us || 0) / 1_000_000, 3)} s`],
    ["Trace hash", manifest.trace_hash],
    ["Fingerprint", manifest.run_fingerprint],
    ["Seed", manifest.master_seed],
  ];
  $("#manifestGrid").innerHTML = values.map(([key, value]) => `<article><small>${escapeHtml(key)}</small><strong>${escapeHtml(value ?? "—")}</strong></article>`).join("");
}

function downloadJson(filename, value) {
  const blob = new Blob([JSON.stringify(value, null, 2) + "\n"], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = filename;
  anchor.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function cadContract() {
  const extension = state.cadFile?.name.split(".").pop()?.toLowerCase() || null;
  return {
    schema_version: "0.1.0-prototype",
    contract_type: "cad-import-request",
    implementation_status: "ADAPTER_NOT_CONNECTED",
    source: state.cadFile ? { file_name: state.cadFile.name, extension, size_bytes: state.cadFile.size } : null,
    coordinate: { source_unit: $("#cadUnit").value, up_axis: $("#cadUpAxis").value, target_frame: $("#targetFrame").value.trim() },
    mapping: { rail_center_layer: $("#railLayer").value.trim(), station_layer_or_block: $("#stationLayer").value.trim(), direction_layer: $("#directionLayer").value.trim() },
    expected_output: ["nodes", "edges", "stations", "source_artifacts", "geometry_transforms"],
    next_required_component: extension === "dxf" ? "DXF entity parser + semantic mapper" : "CAD format converter to DXF + DXF semantic mapper",
  };
}

function checkCad() {
  const contract = cadContract();
  const missing = [];
  if (!state.cadFile) missing.push("CAD 파일");
  if (!contract.mapping.rail_center_layer) missing.push("Rail Layer");
  if (!contract.mapping.station_layer_or_block) missing.push("Station Layer");
  if (!contract.coordinate.target_frame) missing.push("Canonical Frame");
  const result = $("#cadCheckResult");
  if (missing.length) {
    result.textContent = `준비 미완료: ${missing.join(", ")}`;
    result.style.color = "var(--red)";
    $("#downloadCadContractButton").disabled = true;
    toast("CAD Import 계약의 필수 항목을 채워주세요.", "error");
    return;
  }
  result.textContent = `계약 준비 완료 · ${contract.source.extension.toUpperCase()} · 다음 구현: ${contract.next_required_component}`;
  result.style.color = "var(--green)";
  state.prototype = contract;
  $("#downloadCadContractButton").disabled = false;
  toast("CAD Import 개발 계약을 생성했습니다. 실제 geometry 변환은 아직 수행하지 않습니다.", "success");
}

function bottleneckPreview() {
  if (!state.analysis?.edge_flows?.length) {
    toast("먼저 3차 Flow 분석을 실행해 주세요.", "error");
    switchView("analysis");
    return;
  }
  const nodeFlows = new Map((state.analysis.node_flows || []).map((item) => [item.node_id, item]));
  const maxMerge = Math.max(1, ...(state.analysis.node_flows || []).map((item) => Number(item.merge_pressure) || 0));
  const scores = new Map();
  for (const edge of state.analysis.edge_flows) {
    const downstreamMerge = Number(nodeFlows.get(edge.to_node_id)?.merge_pressure) || 0;
    const score = 0.7 * (Number(edge.flow_share) || 0) + 0.3 * downstreamMerge / maxMerge;
    scores.set(edge.edge_id, { score, flow_share: edge.flow_share, downstream_merge: downstreamMerge });
  }
  state.bottleneckScores = scores;
  const ranking = [...scores].map(([edge_id, value]) => ({ edge_id, ...value })).sort((a, b) => b.score - a.score);
  showPrototype({
    schema_version: "0.1.0-ui-hypothesis",
    contract_type: "bottleneck-preview",
    authoritative: false,
    warning: "UI 표현 검증용 가설 점수이며 A5 Core 알고리즘이 아닙니다.",
    formula: "0.70 * edge.flow_share + 0.30 * normalized_downstream_merge_pressure",
    ranking,
  });
  renderNetwork();
  toast("UI 가설 점수를 네트워크 색상에 반영했습니다.", "success");
}

function roiContract() {
  if (!state.facility || !state.bottleneckScores?.size) {
    toast("Bottleneck 가설 점수를 먼저 생성해 주세요.", "error");
    return;
  }
  const depth = Number($("#roiDepth").value);
  const edges = state.facility.edges || [];
  const top = [...state.bottleneckScores.entries()].sort((a, b) => b[1].score - a[1].score)[0]?.[0];
  const selected = new Set(top ? [top] : []);
  for (let level = 0; level < depth; level += 1) {
    const frontier = edges.filter((edge) => selected.has(edge.id));
    const nodes = new Set(frontier.flatMap((edge) => [edge.from_node_id, edge.to_node_id]));
    for (const edge of edges) if (nodes.has(edge.from_node_id) || nodes.has(edge.to_node_id)) selected.add(edge.id);
  }
  const nodeIds = new Set(edges.filter((edge) => selected.has(edge.id)).flatMap((edge) => [edge.from_node_id, edge.to_node_id]));
  showPrototype({
    schema_version: "0.1.0-prototype",
    contract_type: "roi-reduction-request",
    implementation_status: "REDUCTION_ENGINE_NOT_CONNECTED",
    model_revision_id: state.facility.revision_id,
    selection_reason: "top-ui-hypothesis-score",
    seed_edge_id: top,
    adjacency_depth: depth,
    retained_edge_ids: [...selected].sort(),
    retained_node_ids: [...nodeIds].sort(),
    required_outputs: ["reduced_facility", "boundary_contract", "reduction_manifest", "validation_report"],
  });
}

function abContract() {
  if (!state.scenario) {
    toast("Scenario를 먼저 연결해 주세요.", "error");
    return;
  }
  showPrototype({
    schema_version: "0.1.0-prototype",
    contract_type: "policy-ab-request",
    implementation_status: "REPLACEABLE_POLICY_RUNTIME_NOT_CONNECTED",
    model_revision_id: state.facility?.revision_id,
    scenario_id: state.scenario.scenario_id,
    common_seed: state.scenario.master_seed ?? 0,
    experiment_a: { routing_policy: $("#policyA").value },
    experiment_b: { routing_policy: $("#policyB").value },
    comparison_metrics: ["completed_jobs", "travel_time", "queue_time", "first_divergence", "trace_hash"],
  });
}

function projectionContract() {
  if (!state.facility) {
    toast("Facility를 먼저 연결해 주세요.", "error");
    return;
  }
  showPrototype({
    schema_version: "0.1.0-prototype",
    contract_type: "digital-twin-projection-request",
    implementation_status: "USD_ADAPTER_NOT_CONNECTED",
    model_revision_id: state.facility.revision_id,
    coordinate_reference: state.facility.coordinate_reference,
    visualization_fidelity: $("#projectionQuality").value,
    entity_count: { nodes: state.facility.nodes?.length || 0, edges: state.facility.edges?.length || 0, stations: state.facility.stations?.length || 0 },
    target: "OpenUSD / Omniverse / Isaac Sim",
    required_outputs: ["scene.usda", "entity_mapping.json", "asset_binding_report.json"],
  });
}

function showPrototype(value) {
  state.prototype = value;
  $("#prototypeOutput").textContent = JSON.stringify(value, null, 2);
  $("#downloadPrototypeButton").disabled = false;
  toast("프로토타입 계약을 생성했습니다.", "success");
}

function renderCapabilities() {
  const capabilities = state.status?.capabilities || [];
  $("#capabilityGrid").innerHTML = capabilities.map((item) => `
    <article class="capability-card"><header><b>${escapeHtml(item.name)}</b><span class="stage-tag ${item.stage}">${item.stage === "available" ? "사용 가능" : "프로토타입"}</span></header><p>${escapeHtml(item.description)}</p></article>`).join("");
}

async function initialize() {
  bindEvents();
  updateReadiness();
  renderAnalysis();
  renderManifest();
  try {
    state.status = await api("/api/status");
    const ready = state.status.engine.ready;
    $("#engineDot").classList.toggle("ready", ready);
    $("#engineLabel").textContent = ready ? "Core 실행 가능" : "Core 미빌드";
    $("#enginePath").textContent = ready ? state.status.engine.path : "UI와 프로토타입은 실행할 수 있습니다.";
    $("#uiVersion").textContent = `UI v${state.status.ui_version}`;
    renderCapabilities();
    if (state.status.sample_ready) await loadSample(false);
  } catch (error) {
    $("#engineLabel").textContent = "서버 연결 실패";
    toast(error.message, "error");
  }
}

function bindEvents() {
  $$(".nav-item").forEach((button) => button.addEventListener("click", () => switchView(button.dataset.view)));
  $$('[data-jump]').forEach((button) => button.addEventListener("click", () => switchView(button.dataset.jump)));
  $$('[data-action]').forEach((button) => button.addEventListener("click", () => executeCore(button.dataset.action)));
  $("#analyzeTopButton").addEventListener("click", () => executeCore("analyze"));
  $("#sampleButton").addEventListener("click", () => loadSample(true));
  $$('[data-file]').forEach((button) => button.addEventListener("click", () => document.getElementById(button.dataset.file).click()));
  $("#facilityInput").addEventListener("change", (event) => readFile(event.target, "facility"));
  $("#scenarioInput").addEventListener("change", (event) => readFile(event.target, "scenario"));
  $("#demandInput").addEventListener("change", (event) => readFile(event.target, "demand"));
  $("#cadInput").addEventListener("change", (event) => readFile(event.target, "cad"));
  $("#zoomInButton").addEventListener("click", () => changeZoom(.15));
  $("#zoomOutButton").addEventListener("click", () => changeZoom(-.15));
  $("#fitButton").addEventListener("click", () => { state.zoom = 1; changeZoom(0); });
  $("#copyBuildButton").addEventListener("click", async () => {
    const hint = state.status?.engine?.build_hint || "cmake -S . -B build -DCMAKE_BUILD_TYPE=Release && cmake --build build --parallel";
    await navigator.clipboard.writeText(hint);
    toast("빌드 명령을 복사했습니다.", "success");
  });
  $("#exportReportButton").addEventListener("click", () => downloadJson("cross-domain-report.json", state.analysis));
  $("#checkCadButton").addEventListener("click", checkCad);
  $("#downloadCadContractButton").addEventListener("click", () => downloadJson("cad-import-contract.json", cadContract()));
  $("#previewBottleneckButton").addEventListener("click", bottleneckPreview);
  $("#roiDepth").addEventListener("input", (event) => { $("#roiDepthValue").textContent = event.target.value; });
  $("#createRoiButton").addEventListener("click", roiContract);
  $("#createAbButton").addEventListener("click", abContract);
  $("#createProjectionButton").addEventListener("click", projectionContract);
  $("#downloadPrototypeButton").addEventListener("click", () => downloadJson("sim-core-prototype-contract.json", state.prototype));
  document.addEventListener("keydown", (event) => {
    if (event.target.matches("input, select, textarea")) return;
    const view = ["workspace", "inputs", "analysis", "simulation", "lab"][Number(event.key) - 1];
    if (view) switchView(view);
  });
}

function changeZoom(delta) {
  state.zoom = Math.max(.55, Math.min(2.2, state.zoom + delta));
  $("#zoomLabel").textContent = `${Math.round(state.zoom * 100)}%`;
  $("#networkCanvas").style.transform = `scale(${state.zoom})`;
}

initialize();
