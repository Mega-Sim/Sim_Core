/*Vehicle based*/
begin pm initialization function

	set theVehicle A_cgStopDelay = -1 										/* Needs to check */
	
	set theVehicle defined forward normal to vrNormalVelocity m per sec
	set theVehicle defined forward curve to vrCurveVelocity m per sec
	set theVehicle defined forward spur to vrCurveVelocity m per sec		/* what's spur? */
	
	set theVehicle defined reverse normal to vrNormalVelocity m per sec
	set theVehicle defined reverse curve to vrCurveVelocity m per sec
	set theVehicle defined reverse spur to vrCurveVelocity m per sec 
	
	set theVehicle defined acceleration to vrAcceleration m per sec
	set theVehicle defined deceleration to vrDeceleration m per sec
	
	set theVehicle defined brake = vrBrakeDistance m
	set theVehicle defined stop = vrStopDistance m
	
	set theVehicle atBattery to vrBatteryCapa * 0.80	
	
	if theVehicle type = "DefVehicle" then
	begin
		set theVehicle segments first color to blue violet
		inc vcOHT by 1
		set theVehicle aID = vcOHT
		set theVehicle aAssign = 0								/* JobAssigned 1, ParkAssigned 2, etc. 3 */
		
		if theVehicle aID <= vnOHT then
		begin
			insert theVehicle into vlistOHT
			insert theVehicle into vlistOHTall
			
			if theVehicle aID <= vnOHT - 400 then
				insert theVehicle into vlistOHT_Bat
		end	
	end
	else 
	begin
		set theVehicle segments first color to green yellow
		inc vcROHT by 1
		set theVehicle aID = vcROHT
		set theVehicle aAssign = 0								/* JobAssigned 1, ParkAssigned 2, etc. 3 */
		
		if theVehicle aID <= vnROHT then
		begin
			insert theVehicle into vlistROHT
			insert theVehicle into vlistROHT_Bat
			insert theVehicle into vlistOHTall
		end	
	end
	
	return true
end

begin pm task search procedure
	if this vehicle aID > vnOHT then    
	begin
		move into queue qDisable
		wait to be ordered on ol_Disable    /* If vnOHT > OHT# in Model, rest are disabled */
		return
	end

	if (this vehicle segments first color = blue violet or this vehicle segments first color = red) and this vehicle current schedjob = null then
	begin
		if this vehicle segments first color = red then
		begin
			set this vehicle segments first color = blue violet
			insert this vehicle into vlistOHT
		end
	
		if ac = 0 then
		begin
			set vi to 1 + 8 * u 0.5, 0.5
			print "pm.cp_Route_" vi to vstrTemp
			set vlocTemp(1) to vstrTemp
			dispatch this vehicle to vlocTemp(1) 
		end
		else if this vehicle current location path color = red then
		begin
			set k = 0
			while (k < vll_ABE size)
			begin			
				inc k by 1	
				set vrlDistance(k) to this vehicle current location path navigation distance to vll_ABE(k)
				set vllocation(k) to vll_ABE(k) 
				if vllocation(k) = this vehicle current location then
					set vrlDistance(k) to 999999999999
				set vilIndex(k) to k
			end	
		end	
		else
		begin			
			set k = 0
			while (k < vllChargeRoute size)
			begin			
				inc k by 1	
				set vrlDistance(k) to this vehicle current location path navigation distance to vllChargeRoute(k)
				set vllocation(k) to vllChargeRoute(k) 
				if vllocation(k) = this vehicle current location then
					set vrlDistance(k) to 999999999999
				set vilIndex(k) to k
			end	
		end
			
		call F_QuickSort(1, k)
		dispatch this vehicle to vllocation(1)
	end
	else if this vehicle segments first color = yellow and this vehicle current schedjob = null then
	begin
		print this vehicle current location to vstrTemp
		set vi to vstrTemp substring(13, 1)
		if vi < 8 and vi > 2 then
		begin
			inc vi by 1
			print "pm.cp_Route_" vi to vstrTemp
			set vlocTemp(1) to vstrTemp
			dispatch this vehicle to vlocTemp(1) 
		end
		else
			dispatch this vehicle to pm.cp_Route_3
	end
end

begin F_Dijkstra

	set vi = 0
	set vj = 0
	while vi < viSize do
	begin
		inc vi by 1
		set vrDist(vi) = vrDM(Arg_Start, vi)
		set vipred(vi) = Arg_Start
		set viFound(vi) = 0
	end
	
	set vi = 0
	while vi < viSize do
	begin
		inc vi by 1
		set uu = F_Choose()
		set viFound(uu) = 1
		
		while vj < viSize do
		begin
			inc vj by 1

			if vrDist(uu) + vrDM(uu, vj) < vrDist(vj) then
			begin
				set vrDist(vj) to vrDist(uu) + vrDM(uu, vj)
				set vipred(vj) = uu
			end
		end
				
		set vj = 0		
	end

//	print "Distance from " vllDM(Arg_Start) " to " vllDM(Arg_End) " = " vrDist(Arg_End) to message
//	print "Path = " vllDM(Arg_End) to message
	set vllRoute to null
	
	set vi = Arg_End
	
/*	if vi <= 1 then
	begin
		dispatch theVehicle to vllDM(Arg_End)
		return true
	end*/
	
	while vi != Arg_Start do
	begin
		set vi = vipred(vi)
		if vllDM(vi) != theVehicle current location
			insert vllDM(vi) into vllRoute at end
			
//		print "<- " vllDM(vi) to message
	end
	
	set vi = vllRoute size
	while vi > 0  do
	begin
		dispatch theVehicle to vllRoute(vi)
		dec vi by 1
	end
				
	if theVehicle color = blue violet then		
		dispatch theVehicle to vllDM(Arg_End)
	
//	print vllDM(Arg_Start), "\t", vllDM(Arg_End) to message			
	return true
end

begin F_Choose
	set vi_Ch = 0
	set vrMin = vrBigValue
	
	while vi_Ch < viSize do
	begin
		inc vi_Ch by 1
		if vrDist(vi_Ch) > 0 and vrDist(vi_Ch) < vrBigValue and vrDist(vi_Ch) < vrMin and viFound(vi_Ch) = 0 then
		begin
			set vrMin = vrDist(vi_Ch)
			set viMin_pos = vi_Ch
		end
	end
	
	return viMin_pos
end


begin pm decelerate to destination function

	if theVehicle aiRouteChange = 1 then
		set theVehicle aiRouteChange to 0

	if theVehicle segments first color != blue violet and theVehicle current schedjob type = "move" then
//	if theVehicle segments first color  = blue violet and theVehicle current schedjob type = "move" then
	begin
		set i to 0
		for each vJob in theVehicle schedjobs do
		begin
			inc i by 1
			if i > 1 then
			begin
				if vJob type = "move" then
				begin
					set theVehicle current schedjob to vJob
					for each vJob2 in theVehicle schedjobs do
					begin
						if vJob2 location = destLoc then
						begin
							cancel vJob2
							break
						end
					end	
					break
				end
			end
		end	
	end
	else if destLoc color = green 
	begin
		print destLoc to vsTemp(1)
		set vi to vsTemp(1) substring(13,1)
		if vi != 8 then
		begin
			inc vi by 1
			print "pm:cp_Route_" vi to vsTemp(2) 
			set vlocTemp(1) to vsTemp(2)
		end
		else if vi = 8 then
			set vlocTemp(1) to "pm:cp_Route_1"	

		dispatch theVehicle to vlocTemp(1)	
				
		for each vJob in theVehicle schedjobs do
		begin
			if vJob location = vlocTemp(1) then
				set theVehicle current schedjob to vJob 
		end

		for each vJob in theVehicle schedjobs do
		begin
			if vJob location = destLoc then
				cancel vJob	
		end				
	end
  
	return true
end

begin pm passing station function
/*	
	if theVehicle segments first color = goldenrod and theVehicle aiPathSearched = 0 then
	begin	
		set i = 0
		for each vlocTemp(1) in vllDM do
		begin
			inc i by 1
			set vrDistance(1) to stopLoc path distance to vlocTemp(1)
			
			if i = 1 then
			begin
				set vlocMin to vlocTemp(1)
				set viMinIndex to i
				set vrMinDist to vrDistance(1)
			end
			else
			begin
				if vrMinDist > vrDistance(1) then
				begin	
					set vlocMin to vlocTemp(1)
					set viMinIndex to i
					set vrMinDist to vrDistance(1)
				end
			end			
		end
		
		set o to viMinIndex
		
		set i = 0
		for each vlocTemp(1) in vllDM do
		begin
			inc i by 1
			set vrDistance(1) to theVehicle current schedjob location path distance to vlocTemp(1)
			
			if i = 1 then
			begin
				set vlocMin to vlocTemp(1)
				set viMinIndex to i
				set vrMinDist to vrDistance(1)
			end
			else
			begin
				if vrMinDist > vrDistance(1) then
				begin	
					set vlocMin to vlocTemp(1)
					set viMinIndex to i
					set vrMinDist to vrDistance(1)
				end
			end			
		end
		
		set k to viMinIndex	
			
		set theVehicle aiPathSearched = 1
					
		if o != 0 and k != 0 then
			call F_Dijkstra(o, k, theVehicle)
		else
			print k, "\t", o to message
						
		for each vJob in theVehicle schedjobs do
		begin
			if vJob type = "move" then
			begin
				set theVehicle current schedjob to vJob
				break
			end
		end		
	end
	else if stopLoc = pm.cp_BE_31 and theVehicle current schedjob type = "deliver" then
	begin
		for each vlocTemp(1) in theVehicle current route do
		begin
			if vlocTemp(1) = pm.cp_d_516 then
			begin
				dispatch theVehicle to pm.cp_d_498
				for each vJob in theVehicle schedjobs do
				begin
					if vJob location = pm.cp_d_498 then
						set theVehicle current schedjob to vJob
				end
				break
			end
		end
	end
*/
	return true
end

begin pm pickup procedure
	for each vJob in this vehicle schedjobs do
	begin
		if vJob type = "move" then
			cancel vJob
	end	

//	remove this vehicle closest schedjob load from vlistLoad(2)		/* Remove from Assigned Load List "vlistLoad(2)"_ line 210 */
	set this vehicle aAssign to 2
	if this vehicle current location capacity = 100 then
		wait for 6 sec
	else
		wait for 9 sec
	
	set this vehicle aSetdown to this vehicle closest schedjob load aSetdown
	set this vehicle closest schedjob load atUnload to ac
	set this vehicle segments first color to sea
	set this vehicle aiPathSearched to 0
	set this vehicle atBattery_Del to this vehicle atBattery
	tabulate (this vehicle atBattery -  this vehicle atBattery_Ret) in tBatteryChange_Ret	
/*
	set i = 0
	for each vlocTemp(1) in vllDM do
	begin
		inc i by 1
		set vrDistance(1) to this vehicle current location path distance to vlocTemp(1)
		
		if i = 1 then
		begin
			set vlocMin to vlocTemp(1)
			set viMinIndex to i
			set vrMinDist to vrDistance(1)
		end
		else
		begin
			if vrMinDist > vrDistance(1) then
			begin	
				set vlocMin to vlocTemp(1)
				set viMinIndex to i
				set vrMinDist to vrDistance(1)
			end
		end			
	end
	
	set o to viMinIndex
	
	set i = 0
	for each vlocTemp(1) in vllDM do
	begin
		inc i by 1
		set vrDistance(1) to this vehicle current schedjob load alocTo path distance to vlocTemp(1)
		
		if i = 1 then
		begin
			set vlocMin to vlocTemp(1)
			set viMinIndex to i
			set vrMinDist to vrDistance(1)
		end
		else
		begin
			if vrMinDist > vrDistance(1) then
			begin	
				set vlocMin to vlocTemp(1)
				set viMinIndex to i
				set vrMinDist to vrDistance(1)
			end
		end			
	end
	
	set k to viMinIndex	
						
	if o != 0 and k != 0 then
		call F_Dijkstra(o, k, this vehicle)
	else
		print k, "\t", o to message
*/
end

begin pm setdown procedure
	set atcheck to ac
	if this vehicle current location capacity = 100 then
		wait for 6 sec
	else
		wait for 9 sec
		
	set this vehicle aAssign = 0
	tabulate (this vehicle atBattery -  this vehicle atBattery_Del) in tBatteryChange_Del
	set this vehicle atBattery_Idle to this vehicle atBattery
	
	set k = 0
	while (k < vll_ABE size)
	begin			
		inc k by 1	
		set vrlDistance(k) to this vehicle current location path navigation distance to vll_ABE(k)
		set vllocation(k) to vll_ABE(k) 
		if vllocation(k) = this vehicle current location then
			set vrlDistance(k) to 99999
		set vilIndex(k) to k
	end	
	call F_QuickSort(1, k)
	dispatch this vehicle to vllocation(1)

			
	if (this vehicle atBattery < 3960 * vrRecharge and this vehicle type = "DefVehicle") or (this vehicle atBattery < 1980 and this vehicle type = "ROHT") then
	begin
		set this vehicle segments first color to yellow
		set this vehicle aiRecharge to 1
		inc cChargingOHT by 1
		print this vehicle, "\t", " need to charge" to message
	end
	else
	begin
		insert this vehicle into vlistOHT	
		set this vehicle segments first color to blue violet
	/*	if this vehicle current location path color = black then
		begin
			insert this vehicle into vlistOHT	
			set this vehicle segments first color to blue violet
		end
		else 
			set this vehicle segments first color to red*/
	end
end

begin pm job selection procedure

	if this vehicle current schedjob type = "deliver" or this vehicle current schedjob type = "retrieve" then
	begin
		for each vJob in this vehicle schedjobs do
		begin
			if vJob type = "move" then
			begin
				set this vehicle current schedjob to vJob
				break
			end
		end
	end	
end

begin pm.ROHT job finished procedure

	if this vehicle current location color = salmon then
	begin
		for each vJob in this vehicle schedjobs do
		begin
			cancel vJob
		end
		insert this vehicle into vlistROHT
	end
end

begin pIdleCheck arriving procedure
	while 1=1 do
	begin
		wait for 1 
		for each vohtTemp in vlistOHTall do
		begin
			if vohtTemp status = "Idle" then
			begin
				if vohtTemp type = "DefVehicle" then
				begin
					set k = 0
					while (k < vll_ABE size)
					begin			
						inc k by 1				
						if vohtTemp current location = null then
							break	
						else
						begin
							set vrlDistance(k) to vohtTemp current location path navigation distance to vll_ABE(k)
							set vllocation(k) to vll_ABE(k) 
							if vllocation(k) = vohtTemp current location then
								set vrlDistance(k) to 99999
							set vilIndex(k) to k
						end
					end
					set vohtTemp aAssign to 4	
					call F_QuickSort(1, k)
					
					set j to oneof(1:1, 1:2, 1:3)
					if vllocation(j) != vohtTemp current location
						dispatch vohtTemp to vllocation(j)
					else
						dispatch vohtTemp to vllocation(j+1)
				end
				else
				begin
					if (vohtTemp status = "Idle" and vohtTemp current location color != salmon) or (vohtTemp current schedjob != null and vohtTemp current schedjob location color != salmon) then
					begin
					/*	set vohtTemp segments first color to green yellow
						set vrDistance(1) to vohtTemp path distance to pm.cp_Rpark_1 
						set vrDistance(2) to vohtTemp path distance to pm.cp_Rpark_5 		
						if vrDistance(1) < vrDistance(2) then
							dispatch vohtTemp to oneof(1:pm.cp_Rpark_1, 1:pm.cp_Rpark_2, 1:pm.cp_Rpark_3 ,1:pm.cp_Rpark_4)
						else
							dispatch vohtTemp to oneof(1:pm.cp_Rpark_5, 1:pm.cp_Rpark_6, 1:pm.cp_Rpark_7 ,1:pm.cp_Rpark_8)*/
					end
				end
			end	
		end
	end
end

begin F_QuickSort 

	if Arg1 >= Arg2 then
	begin
		return true
	end
	else
	begin
		set vipivot to Arg1
		set vi to vipivot + 1
		set vj to Arg2
		
		while(vi <= vj) do
		begin
			while(vi <= Arg2 and vrlDistance(vi) <= vrlDistance(vipivot)) do
			begin
				inc vi by 1
			end
			
			while(vj > Arg1 and vrlDistance(vj) >= vrlDistance(vipivot)) do
			begin
				dec vj by 1
			end
			
			if vi >= vj then
				break
			
			set vrtemp = vrlDistance(vj)
			set vrlDistance(vj) = vrlDistance(vi)
			set vrlDistance(vi) = vrtemp	
	
			set vlocTemp(1) = vllocation(vj)
			set vllocation(vj) = vllocation(vi)
			set vllocation(vi) = vlocTemp(1)						
		end

		set vrtemp = vrlDistance(vj)
		set vrlDistance(vj) = vrlDistance(vipivot)
		set vrlDistance(vipivot) = vrtemp	
		
		set vlocTemp(1) = vllocation(vj)
		set vllocation(vj) = vllocation(vipivot)
		set vllocation(vipivot) = vlocTemp(1)
					
		call F_QuickSort(Arg1, vj - 1)
		call F_QuickSort(vj + 1, Arg2)
		
		return true
	end
end

/* Dispatching Rule */
begin pDispatch arriving procedure
	while 1=1 do
	begin
		wait for vtSchedule		/* set vtSchedule = 5 */
		
		while vlistOHT size > 0 and vlistLoad(1) size > 0 do	/* Check OHT number and load creation */
		begin
			set vlSelect = null
			set vvSelect = null
			set vtSelect = 0
			
			for each vohtTemp in vlistOHT do
			begin
				for each vlTemp in vlistLoad(1) do
				begin
					/* Setting starting point for distance measure */
					set vrDistance(1) = vohtTemp path distance to vlTemp alocFrom
					
					if vrDistance(1) < 200000.0  then
					begin
						/* Calculating weight value for load that is closest */
					//	set vtCost = 3000 - vtPriorityCost - ((ac - vlTemp atTR) * vnTimeWeight) + (vrDistance(1) / 1000 / vrNormalVelocity)
						set vtCost = 10000 - vtPriorityCost - ((ac - vlTemp atTR) * vnTimeWeight) + (vrDistance(1) / 1000 / vrNormalVelocity) - F_Sqrt(vohtTemp atBattery / 1.6)
						
						if vlSelect = null then
						begin
							set vlSelect = vlTemp
							set vvSelect = vohtTemp
							set vtSelect = vtCost
						end
						
						else if (ac - vlSelect atTR) < vtTimeLimit and (ac - vlTemp atTR) >= vtTimeLimit then	/* vtTimeLimit = 300 */
						begin
							set vlSelect = vlTemp
							set vvSelect = vohtTemp
							set vtSelect = vtCost
						end
						
						else if (ac - vlSelect atTR) < vtTimeLimit and (ac - vlTemp atTR) < vtTimeLimit then
						begin
							if vtCost < vtSelect then
							begin
								set vlSelect = vlTemp
								set vvSelect = vohtTemp
								set vtSelect = vtCost
							end
						end
						
						else if (ac - vlSelect atTR) >= vtTimeLimit and (ac - vlTemp atTR) >= vtTimeLimit then
						begin
							if vtCost < vtSelect then
							begin
								set vlSelect = vlTemp
								set vvSelect = vohtTemp
								set vtSelect = vtCost
							end
						end
					end
				end
			end
				
			if vlSelect <> null then
			begin
				claim vlSelect for vvSelect
			
				for each vJob in vvSelect schedjobs do
				begin
					if vJob type = "retrieve" then 
						set vvSelect current schedjob to vJob     
				end     
				
				for each vJob in vvSelect schedjobs do
				begin
					if vJob type = "move" then 
						cancel vJob     
				end 
				
				set vlSelect atAssign to ac			/* Calculate Total Assign Time */
				set vlSelect atAssignInit to ac		/* Calculate initial assigned time */

				set vvSelect aAssign = 1
				set vvSelect segments first color to goldenrod
				set vvSelect aRetDistance to vvSelect total distance traveled
				set vvSelect atBattery_Ret to vvSelect atBattery 
				tabulate vvSelect atBattery - vvSelect atBattery_Idle in tBatteryChange_Idle
				    
				remove vvSelect from vlistOHT
				remove vlSelect from vlistLoad(1)

//				set vlSelect avDispatch to vvSelect
//				insert vlSelect into vlistLoad(2)	/* Assigned Load */
			end
			else
				break
		end
	end
end

begin F_Sqrt

	set xr = input
	set yr = 1
	set er = 0.001
	
	while((xr - yr) > er) do
	begin
		set xr = (xr + yr) / 2
		set yr = input / xr
	end

	return xr
end

/* ReAssign Process */
begin pReAssign arriving procedure
	while 1=1 do
	begin
		wait for vtSchedule
		
		while vlistOHT size > 0 and vlistLoad(2) size > 0 do	/* Check OHT number and load creation */
		begin
			set vlSelect = null
			set vvSelect = null
			set vtSelect = 0
			
			for each vlTemp in vlistLoad(2) do
			begin
				set viCheck = 1
				for each vohtTemp in vlistOHT do
				begin
					begin
						set vrDistance(1) = vohtTemp path distance to vlTemp alocFrom  /* Setting starting point for distance measure */
						set vrDistance(2) = vlTemp avDispatch path distance to vlTemp alocFrom
					end
					
					if vrDistance(1) < vrDistance(2) then
					begin
						if viCheck = 1 then
						begin
							set vlSelect = vlTemp
							set vvSelect = vohtTemp
							set vrDistanceTemp to vrDistance(1)
							inc viCheck by 1       
						end
						
						else
						begin
							if vrDistance(1) < vrDistanceTemp then		/* check again */
							begin
								set vlSelect = vlTemp
								set vvSelect = vohtTemp 
								set vrDistanceTemp to vrDistance(1)            
							end
						end
					end
				end
			end
	
			if vlSelect <> null and vlSelect avDispatch <> vvSelect then
			begin
			
				/*-------Revised Code-------*/
				/* Dispatch Previous Job Assigned Vehicle to Random Park Location */
				set k = 1 + vlocParkList size * uniform 0.5,0.5		/* meaning of 0.5bay? */
				dispatch vlSelect avDispatch to vlocParkList(k)
				
				/* Swap current "Retrieve" job for "Move" job */
				for each vJob in vlSelect avDispatch schedjobs do
				begin
					if vJob type = "move" then 
						set vlSelect avDispatch current schedjob to vJob      
				end
				
				/* Cancel Remaining "Retrieve" job */
				for each vJob in vlSelect avDispatch schedjobs do
				begin
					if vJob type = "retrieve" then 
						cancel vJob      
				end
				/*-------------------------*/
				insert vlSelect avDispatch into vlistOHT
	
				set vlSelect avDispatch segments first color to blue violet
				set vlSelect avDispatch aAssign = 0
				
				claim vlSelect for vvSelect
				
				for each vJob in vvSelect schedjobs do
				begin
					if vJob type = "retrieve" then 
						set vvSelect current schedjob to vJob     
				end     
				
				for each vJob in vvSelect schedjobs do
				begin
					if vJob type = "move" then 
						cancel vJob     
				end 
		
				set vlSelect atAssign to ac
	
				set vvSelect aAssign = 1						/* JobAssigned 1, ParkAssigned 2, etc. 3 */
				set vvSelect segments first color to goldenrod
				set vvSelect aRetDistance to vvSelect total distance traveled
				
				remove vvSelect from vlistOHT
				set vlSelect avDispatch to vvSelect 
				set vrDistanceTemp to 0 
			end
		else
			break
		end
	end
end


begin pm work ok function
	return false
end

begin pm resume moving procedure
	wait for vtResume
end


begin pDispatchR arriving procedure
	while 1=1 do
	begin
		wait for vtSchedule		/* set vtSchedule = 5 */
		
		while vlistROHT size > 0 and vlistLoad(2) size > 0 do	/* Check OHT number and load creation */
		begin
			set vlSelect = null
			set vvSelect = null
			set vtSelect = 0
			
			for each vohtTemp in vlistROHT do
			begin
				for each vlTemp in vlistLoad(2) do
				begin
					/* Setting starting point for distance measure */
					set vrDistance(1) = vohtTemp path distance to vlTemp alocFrom
					/* Calculating weight value for load that is closest */
					set vtCost = 3000 - vtPriorityCost - ((ac - vlTemp atTR) * vnTimeWeight) + (vrDistance(1) / 1000 / vrNormalVelocity)
					
					if vlSelect = null then
					begin
						set vlSelect = vlTemp
						set vvSelect = vohtTemp
						set vtSelect = vtCost
					end
					
					else if (ac - vlSelect atTR) < vtTimeLimit and (ac - vlTemp atTR) >= vtTimeLimit then	/* vtTimeLimit = 300 */
					begin
						set vlSelect = vlTemp
						set vvSelect = vohtTemp
						set vtSelect = vtCost
					end
					
					else if (ac - vlSelect atTR) < vtTimeLimit and (ac - vlTemp atTR) < vtTimeLimit then
					begin
						if vtCost < vtSelect then
						begin
							set vlSelect = vlTemp
							set vvSelect = vohtTemp
							set vtSelect = vtCost
						end
					end
					
					else if (ac - vlSelect atTR) >= vtTimeLimit and (ac - vlTemp atTR) >= vtTimeLimit then
					begin
						if vtCost < vtSelect then
						begin
							set vlSelect = vlTemp
							set vvSelect = vohtTemp
							set vtSelect = vtCost
						end
					end
				end
			end
				
			if vlSelect <> null then
			begin
				claim vlSelect for vvSelect
			
				for each vJob in vvSelect schedjobs do
				begin
					if vJob type = "retrieve" then 
					set vvSelect current schedjob to vJob     
				end     
				
				for each vJob in vvSelect schedjobs do
				begin
					if vJob type = "move" then 
					cancel vJob     
				end 
				
				set vlSelect atAssign to ac			/* Calculate Total Assign Time */
				set vlSelect atAssignInit to ac		/* Calculate initial assigned time */

				set vvSelect aAssign = 1
				set vvSelect segments first color to goldenrod
				set vvSelect aRetDistance to vvSelect total distance traveled
				set vvSelect atBattery_Ret to vvSelect atBattery 
				tabulate vvSelect atBattery - vvSelect atBattery_Idle in tBatteryChange_Idle
				
				print ac, "\t", "JobAssigned", "\t", vvSelect, "\t", vvSelect atBattery to vfpOutResult(8)
				    
				remove vvSelect from vlistROHT
				remove vlSelect from vlistLoad(2)
				
//				set vlSelect avDispatch to vvSelect
//				insert vlSelect into vlistLoad(2)	/* Assigned Load */
			end
		end
	end
end

/*
begin pm.Route_check passing station function
	if theVehicle current schedjob type = "move" and theVehicle aiRouteChange = 0 then
	begin
		for vlocTemp(1) in theVehicle route to theVehicle current schedjob location do
		begin
			if vlocTemp(1) path color = red then
			begin
				set k = 0
				while (k < vll_RR size)
				begin			
					inc k by 1	
					set vrlDistance(k) to theVehicle path distance to vll_RR(k)
					set vllocation(k) to vll_RR(k) 
					if vllocation(k) = theVehicle current location then
						set vrlDistance(k) to 99999
					set vilIndex(k) to k
				end
				call F_QuickSort(1, k)	
				dispatch theVehicle to vllocation(1)		
				set theVehicle aiRouteChange to 1
				for each vJob in theVehicle schedjobs do
				begin
					if vJob location color = green then
						set theVehicle current schedjob to vJob
				end
				
				for each vJob in theVehicle schedjobs do
				begin
					if vJob location color != green then
						cancel vJob
				end
				break
			end
		end
	end

	return true
end

begin pm.DefVehicle path claimed function

	if theVehicle  = pm.DefVehicle(1) then
	begin
		if theVehicle current path != null and theVehicle current path color = black and thePath color = red then
			set theVehicle atRedStart to ac
	end

	return true
end

begin pm.DefVehicle path released function

	if theVehicle  = pm.DefVehicle(1) then
	begin
		if thePath color = red and theVehicle atRedStart > 0 then
		begin
			print ac - theVehicle atRedStart to vfpTimeInRed
			set theVehicle atRedStart to 0
		end
	end

	return true
end

begin pm.DefVehicle path released function 

	if ac > 3600 and theVehicle current path != null then
	begin
		if thePath color = black and theVehicle current path color = red then
			set theVehicle atNoHID_Start to ac
		else if thePath color = red and theVehicle current path color = black and theVehicle atNoHID_Start > 0 then
		begin
			print ac - theVehicle atNoHID_Start to vfpOutResult(9)
			set theVehicle atNoHID_Start to 0
		end
		else if thePath color = black and theVehicle current path color = red and theVehicle atNoHID_Start < 0 then
			print "Error\t", theVehicle, "\t", theVehicle atNoHID_Start to message
	end
			
	return true
end

begin pVehiclePathColor arriving procedure
	while 1=1 do
	begin
		wait for 0.1
		set i = 0
		while i < 1 do
		begin
			inc i by 1
			if pm.DefVehicle(i) current path != null and pm.DefVehicle(i) current path color = red then
			begin
				if pm.DefVehicle(i) atRedIn = 0 then
					set vtBatteryTemp(i) to pm.DefVehicle(i) atBattery
			
				inc pm.DefVehicle(i) atRedIn by 0.1 sec
				
				if pm.DefVehicle(i) atRedIn > vtRedInMax(i) then
				begin
					set vtRedInMax(i) to pm.DefVehicle(i) atRedIn
				end
			end
			else
			begin
				if vtBatteryTemp(i) > 0 then
					print ac, "\t", pm.DefVehicle(i), "\t", vtRedInMax(i), "\t", (pm.DefVehicle(i) atBattery - vtBatteryTemp(i)) to vfpOutResult(6)
					
				set pm.DefVehicle(i) atRedIn to 0.0
				set vtRedInMax(i) to 0
				set vtBatteryTemp(i) to 0
			end
		end
	end
end

begin pm block claimed function
	
	if theVehicle current schedjob type = "move"
		inc viBC_move by 1
	else if theVehicle current schedjob type = "retrieve"
		inc viBC_retrieve by 1
	else if theVehicle current schedjob type = "deliver"
		inc viBC_deliver by 1

	return true
end

begin pm block released function
	
	if theVehicle current schedjob type = "move"
		inc viBR_move by 1
	else if theVehicle current schedjob type = "retrieve"
		inc viBR_retrieve by 1
	else if theVehicle current schedjob type = "deliver"
		inc viBR_deliver by 1

	return true
end
*/

