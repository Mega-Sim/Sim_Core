#!/usr/bin/env python3
"""Dependency-free smoke tests for the Flow Workbench server helpers."""

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import run_ui


class WorkbenchSmokeTest(unittest.TestCase):
    def test_status_exposes_real_and_prototype_capabilities(self):
        payload = run_ui.status_payload()
        stages = {item["stage"] for item in payload["capabilities"]}
        self.assertEqual({"available", "prototype"}, stages)
        self.assertIn("engine", payload)

    def test_configured_binary_is_discovered(self):
        with tempfile.TemporaryDirectory() as directory:
            binary = Path(directory) / "sim-core"
            binary.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
            binary.chmod(0o755)
            with mock.patch.dict(os.environ, {"SIM_CORE_BIN": str(binary)}):
                self.assertEqual(binary.resolve(), run_ui.find_sim_core())

    def test_sample_contract_when_repository_examples_are_present(self):
        sample_root = run_ui.REPOSITORY_ROOT / "examples" / "cross_domain"
        if not sample_root.is_dir():
            self.skipTest("전체 저장소 예제가 없는 UI 단독 검사 환경")
        sample = run_ui.load_sample()
        self.assertIn("nodes", sample["facility"])
        self.assertIn("vehicles", sample["scenario"])
        self.assertIn("expected_moves_per_hour", sample["from_to"])


if __name__ == "__main__":
    unittest.main()
