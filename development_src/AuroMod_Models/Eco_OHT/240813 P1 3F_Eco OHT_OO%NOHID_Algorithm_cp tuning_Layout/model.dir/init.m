begin model initialization function
	set vnRoute = 40723			/* Numbers of line in Fromto File */
	set vrCapa = 1.64			/* Needs to check */
	set vnOHT = 0				/* Input Numbers of OHT */
	set vnROHT = 0
	set vrOHTspec = 0.6	/* Normaly applying specification of P1,2,3,4 */
	set vrEfficiency = 0.6
	set vllpm = pm locations
	
	for each vlocTemp(1) in vllpm do 
	begin
		if vlocTemp(1) color = blue then
			insert vlocTemp(1) into vllpurple
		else if vlocTemp(1) color = inherit then
			insert vlocTemp(1) into vllInherit	
		else if vlocTemp(1) color = green then
			insert vlocTemp(1) into vllChargeRoute
		
		if vlocTemp(1) color != dkgrey then
		begin
			if vlocTemp(1) capacity = 10000 then
				insert vlocTemp(1) into vllLower
			else 
				insert vlocTemp(1) into vllUpper
		end
	end

	open "arc/result/distance.txt" for writing save result as vfpDistance
	
	set vnCapa to vrCapa*100	/* Needs to check */
	set vrBatteryCapa = 3960
	set vtBatteryMax = vrBatteryCapa * 0.8 // 3168
	set vtBatteryMin = vrBatteryCapa * 0.2 // 792
	set vrRecharge = 0.2
	call fsetValuable_FilePtr() /* Call Text Files */
	call freadFromto()     		/* Read Fromto Data */
//	call freadFromto2()     		/* Read Fromto Data */
//	call freadFromto3()     		/* Read Fromto Data */
	call freadOHTSpec()
	call freadControl()
	call freadBatcharge()
	call fDistanceMatrix()
	
   return true /* Function needs to put return value */
end

begin fDistanceMatrix
	set vrBigValue = 999999999
	set i = 0
	set j = 0

	set viSize = vllDM size
	
	for each vlocTemp(1) in vllDM do
	begin	
		inc i by 1
		for each vlocTemp(2) in vllDM do
		begin
			inc j by 1
			if vlocTemp(1) != vlocTemp(2) then
			begin
				set vllTemp to vlocTemp(1) route to vlocTemp(2)	
				
				for each vlocTemp(3) in vllTemp do
				begin	
					if vlocTemp(3) color != dkgray then
						remove vlocTemp(3) from vllTemp
				end						

				if vllTemp size != 0 then
				begin
					set vrDM(i, j) to vrBigValue
				end
				else
				begin
					if (vllDM(i) path color = black and vllDM(j) path color = black) then
						set vrDM(i, j) to (vlocTemp(1) path distance to vlocTemp(2))/1000				
					else if (vllDM(i) path color = black and vllDM(j) path color = red) then
						set vrDM(i, j) to vlocTemp(1) path distance to vlocTemp(2)				
					else if (vllDM(i) path color = red and vllDM(j) path color = black) then
						set vrDM(i, j) to (vlocTemp(1) path distance to vlocTemp(2))/1000		
					else if (vllDM(i) path color = red and vllDM(j) path color = red) then
						set vrDM(i, j) to vlocTemp(1) path distance to vlocTemp(2)
						
					if vllDM(i) capacity = 1500 or vllDM(j) capacity = 1500 then
						set vrDM(i, j) to vrDM(i, j) * 1.5
				end
			end
		end
		set j = 0
	end	
		
	return true
end

begin fsetValuable_FilePtr
	/* reading input text files */
	open "arc/data/fromto_renew.txt" for reading save result as vfpInFromto		/* Fromto */
//	open "arc/data/fromto_gap.txt" for reading save result as vfpInFromto3		/* Fromto */
//	open "arc/data/control.txt" for reading save result as vfpInFromto2		/* Fromto */
	open "arc/data/BatteryCharge.txt" for reading save result as  vfpBatcharge 
	open "arc/data/AvoidingBayEnd.txt" for reading save result as  vfpAvoidingBayEnd
	open "arc/data/AvoidingBayEnd_R.txt" for reading save result as  vfpAvoidingBayEnd_R
	open "arc/data/Reroute.txt" for reading save result as  vfpReRoute
	open "arc/data/closest_nodes.txt" for reading save result as vfpClosetNode(1)
	open "arc/data/vllDM.txt" for reading save result as vfpVLLDM
	
	/* writing output */
	open "arc/result/CongLog.txt" for writing save result as vfpCongLog		/*What's CongLog?*/
	open "arc/result/output.txt" for writing save result as vfpOutResult(1)
	open "arc/result/Battery.txt" for writing save result as vfpOutResult(2)
	open "arc/result/Battery_Change.txt" for writing save result as vfpOutResult(3)
	open "arc/result/Block_Count.txt" for writing save result as vfpOutResult(4)
	open "arc/result/Path_Count.txt" for writing save result as vfpOutResult(5)
	open "arc/result/InRed.txt" for writing save result as vfpOutResult(6)
	open "arc/result/Battery_R.txt" for writing save result as vfpOutResult(7)
	open "arc/result/ROHT_Trace.txt" for writing save result as vfpOutResult(8)
	open "arc/result/Time_in_NoHID.txt" for writing save result as vfpOutResult(9)
	open "arc/result/Battery_Cycles.txt" for writing save result as vfpOutResult(11)
	open "arc/result/TimeInRed.txt" for writing save result as vfpTimeInRed
//	open "arc/result/fromto.txt" for writing save result as vfpTemp
	
	print "tLMD", "\t", "tRetDistance", "\t", "tTotDistance", "\t", "tIAssign", "\t",
		"tAssign", "\t", "tUnloadMove", "\t", "tLoadMove", "\t", 
		"vnRequest", "\t", "vnComplete", "\t", "vnDelay"  to vfpOutResult(1)
		
	print "theVehicle" as 15 "\t", "Delayed Node" as 15 "\t" "theVehicle A_cgStopOccur" as 10 "\t" "Stop Duration" as 15 to vfpCongLog 
	/*"\t" : New tab, "\n" : New lines*/
	
	return true
end

/*Read 1st Fromto file*/
begin freadFromto
	set i = 1
	while vfpInFromto eof = 0 do
	begin
		read vsStream(1) from vfpInFromto with delimiter "\n"
		read vraStream(1), vsaStream(1), vsaStream(2) from vsStream(1) with delimiter "\t"
		
		set vroute_Interval(1,i) to vraStream(1)/vrCapa			/* Load creation interval - FAB */		
		set vroute_FromLoc(1,i) to vsaStream(1)     			/* From Location */
		set vroute_ToLoc(1,i) to vsaStream(2)      				/* To Location */
		
			
		inc i by 1
	end 
	return true
end

/*Read 2nd Fromto file*/
begin freadFromto2
	set i = 1
	while vfpInFromto2 eof = 0 do
	
	begin
		read vsStream(2) from vfpInFromto2 with delimiter "\n"
		read vraStream(1), vsaStream(1), vsaStream(2) from vsStream(2) with delimiter "\t"
	
		set vroute_Interval(2,i) to vraStream(1)/vrCapa			/* Load creation interval - FAB */		
		set vroute_FromLoc(2,i) to vsaStream(1)     			/* From Location */
		set vroute_ToLoc(2,i) to vsaStream(2)      				/* To Location */
		inc i by 1
	end 
	return true
end

/*Apply OHT specification*/
begin freadOHTSpec
	set vrNormalVelocity = 3.3
	set vrCurveVelocity = 1.0 * vrOHTspec
	set vrAcceleration = 2 * vrOHTspec
	set vrDeceleration = 3 * vrOHTspec
	set vrBrakeDistance = 4.5
	set vrStopDistance = 0.38
	set vtResume = 0.5
	set vtLoading(1) = 9
	
	print "Number of OHT: " vnOHT to lblOHT		/* Labeling OHT No. on model */
	print "Capa : " vnCapa to lblCapa			/* Labeling Capa on model */
	
	return true
end

begin freadControl
	set vtRun = 1     				/* Time Unit for Printing Run Result */
	set vtSchedule = 5				/* Time Interval between assigning out loads */
	set vtPriorityCost = 100  		/* Needs to check */
	set vnTimeWeight = 1.0			/* Needs to check */
	set vtTimeLimit = 300   		/* Needs to check */
	set vnPark = 195     			/* Number of parking points */
	
	while vfpAvoidingBayEnd eof = 0 do
	begin
		read vsStream(1) from vfpAvoidingBayEnd with delimiter "\n"
		set vlocTemp(1) to vsStream(1)
		if vlocTemp(1) != null then
			insert vlocTemp(1) into vll_ABE
	end 

	while vfpAvoidingBayEnd_R eof = 0 do
	begin
		read vsStream(1) from vfpAvoidingBayEnd_R with delimiter "\n"
		set vlocTemp(1) to vsStream(1)
		if vlocTemp(1) != null then
			insert vlocTemp(1) into vll_ABE_R
	end 

	set i to 0
	while vfpClosetNode(1) eof = 0 do
	begin
		inc i by 1
		read vsStream(1) from vfpClosetNode(1) with delimiter "\n"
		read vsaStream(1), vsaStream(2), viaStream(1), viaStream(2) from vsStream(1) with delimiter "\t"
		set vlocClosestFr(1, i) to vsaStream(1)
		set vlocClosestTo(1, i) to vsaStream(2)
	//	set viClosetFr(1, i) to viaStream(1)
	//	set viClosetTo(1, i) to viaStream(2)
	end

	set i to 0
	while vfpVLLDM eof = 0 do
	begin
		inc i by 1
		read vsStream(1) from vfpVLLDM with delimiter "\n"
		set vlocTemp(1) to vsStream(1)
		if vlocTemp(1) != null then
			insert vlocTemp(1) into vllDM
	end
	

	
	return true
end

begin freadBatcharge
	set i = 0
	while vfpBatcharge eof = 0 do
	begin
		read vsStream(1) from vfpBatcharge with delimiter "\n"
		
		if i=0 then 
			set viTempBat to vsStream(1)
		
		else if i < viTempBat +1 then 
		begin 
			read vraStream(1), vraStream(2), vraStream(3), vraStream(4), vraStream(5), vraStream(6), vraStream(7) from vsStream(1) with delimiter "\t"
		
			set vrBattery_Idle(1,i) to vraStream(1)		 * vrEfficiency 	/* Idle */		
			set vrBattery_Move1(1,i) to vraStream(2)	 * vrEfficiency		/* 0 ~1.2[m/s] */	
			set vrBattery_Move2(1,i) to vraStream(3)	 * vrEfficiency		/* 1.2 ~ 3.3[m/s] */	
			set vrBattery_Move3(1,i) to vraStream(4)	 					/* 3.3~5[m/s] */	
			set vrBattery_Move4(1,i) to vraStream(5)	 * vrEfficiency		/* 5 m/s velocity */	
			set vrBattery_Dec(1,i) to vraStream(6)		 * vrEfficiency		/* decelerate */	
			set vrBattery_Pick(1,i) to vraStream(7)		 * vrEfficiency		/* pick place */
		end
		else
		begin 
			read vraStream(1), vraStream(2), vraStream(3), vraStream(4), vraStream(5), vraStream(6), vraStream(7) from vsStream(1) with delimiter "\t"
		
			set vrBattery_Idle(2,i-viTempBat) to vraStream(1)	 	/* Idle */		
			set vrBattery_Move1(2,i-viTempBat) to vraStream(2)	 	/* 0 ~1.2[m/s] */	
			set vrBattery_Move2(2,i-viTempBat) to vraStream(3)	 	/* 1.2 ~ 3.3[m/s] */	
			set vrBattery_Move3(2,i-viTempBat) to vraStream(4)	 	/* 3.3~5[m/s] */	
			set vrBattery_Move4(2,i-viTempBat) to vraStream(5)	 	/* 5 m/s velocity */	
			set vrBattery_Dec(2,i-viTempBat) to vraStream(6)	* vrEfficiency			/* decelerate */	
			set vrBattery_Pick(2,i-viTempBat) to vraStream(7)	 		/* pick place */
		end
		inc i by 1
	
	end 
	return true
end

begin model snap function 
	
	print "ROHT Jobs\t", vlistROHT size to message
	
	print cLoadMakeID(1) current, "\t", cLoadMakeID(2) current, "\t", cLoadMakeID(3) current to message
	
	print tDelDistance relative average, "\t", tRetDistance relative average, "\t", 
	      tTotDistance relative average, "\t", tAssignInit relative average, "\t" tAssign relative average, "\t", 
	      tUnloadMove relative average, "\t", tLoadMove relative average, "\t", 
	      vnRequest / vtRun, "\t", vnComplete / vtRun, "\t", vnDelay / vtRun to vfpOutResult(1)

	print tBatteryChange_Idle relative average, "\t", tBatteryChange_Ret relative average, "\t", tBatteryChange_Del relative average, "\t", tBatteryChange_Ret relative average + tBatteryChange_Del relative average to vfpOutResult(3)

	      
	print "\n", "IAT: ", tAssignInit relative average, "\t", "FAT: ", tAssign relative average, "\n", "\t",
		  "UMT: ", (tUnloadMove relative average + tAssign relative average - tAssignInit relative average), "\t", "LMT: ", tLoadMove relative average, "\n", "\t"
	      "TT: ", (tUnloadMove relative average + tAssign relative average - tAssignInit relative average + tLoadMove relative average), "\t", 
	      "DT: ", (tUnloadMove relative average + tAssign relative average + tLoadMove relative average), "\n", "\t"
	      "Request: ", vnRequest / vtRun, "\t", "Complete: ", vnComplete / vtRun to message


	print viBC_move, "\t", viBC_retrieve, "\t", viBC_deliver, "\t", viBR_move, "\t", viBR_retrieve, "\t", viBR_deliver to vfpOutResult(4)
	print viBC_move, "\t", viBC_retrieve, "\t", viBC_deliver, "\t", viBR_move, "\t", viBR_retrieve, "\t", viBR_deliver to message
	set viBC_move to 0
	set viBC_retrieve to 0
	set viBC_deliver to 0
	set viBR_move to 0
	set viBR_retrieve to 0
	set viBR_deliver to 0

	print cChargingOHT current to vfpOutResult(6)

	set vnRequest = 0			/* Reset when each snap is finished */
	set vnComplete = 0
	set vnDelay = 0  

	return true
end


begin model finished function

	set i to 0
	while i < vnOHT do
	begin
		inc i by 1
		print i, "\t", cBatteryCycle(i) current to vfpOutResult(11)
	end
	
	return true

end


