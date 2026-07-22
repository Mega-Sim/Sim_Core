begin pBatteryCheck arriving procedure												
	while 1=1 do											
	begin											
		wait for 10 sec	

		if ac > 3600 then
		begin	
			set i = 0	
			for each vohtTemp in vlistOHTall do
			begin
				inc i by 1
				if vohtTemp atBattery < 3960 * 0.5 then
					set vohtTemp aiUnder50 to 1
				else if vohtTemp atBattery = 3960 * 0.8 and vohtTemp aiUnder50 = 1 then
				begin
					set vohtTemp aiUnder50 to 0
					inc cBatteryCycle(i) by 1	
				end
			end		
			
			for each vohtTemp_Bat in vlistOHT_Bat do
			begin
				print ac, "\t", vohtTemp_Bat aID, "\t", vohtTemp_Bat atBattery to vfpOutResult(2)
			end
			
			for each vohtTemp_Bat in vlistROHT_Bat do
			begin
				print ac, "\t", vohtTemp_Bat aID, "\t", vohtTemp_Bat atBattery to vfpOutResult(7)
			end
		end

	end
end
		
begin pm speed changed function

	if(theVehicle atOldtime = 0) then	
	begin 
		set theVehicle atOldtime to ac
		set theVehicle arOldaccel to theVehicle current acceleration
		set theVehicle arOldvelocity to theVehicle current velocity		
		return true 
	end 		
/*	if(theVehicle aID <= 100 and theVehicle aID > 200) then 
		return true*/
	
	if theVehicle atBattery < vrBatteryCapa*0.45  then				
	begin 			
		set theVehicle aiIndex to 1
	end	
	else if theVehicle atBattery < vrBatteryCapa*0.50  then				
	begin 
		set theVehicle aiIndex to 2
	end 	
	else if theVehicle atBattery < vrBatteryCapa*0.55  then				
	begin 
	 	set theVehicle aiIndex to 3	
	end 	
	else if theVehicle atBattery < vrBatteryCapa*0.60  then				
	begin 
		set theVehicle aiIndex to 4
		if theVehicle type = "DefVehicle" and theVehicle aiRecharge = 1 then
		begin
			set theVehicle segments first color to blue violet
			set theVehicle aiRecharge to 0
			insert theVehicle into vlistOHT
			if cChargingOHT current > 0 then
				dec cChargingOHT by 1
			else
				print "Charging OHT Count Error" to message
			print theVehicle, "\t", "return to work" to message
		end
	end 	
	else if theVehicle atBattery < vrBatteryCapa*0.65  then				
	begin 
		set theVehicle aiIndex to 5
	end 	
	else if theVehicle atBattery < vrBatteryCapa*0.70  then				
	begin 
		set theVehicle aiIndex to 6
		if theVehicle type = "ROHT" and theVehicle aiRecharge = 1 then
		begin
			set theVehicle aiRecharge to 0
			set theVehicle segments first color to blue violet
			insert theVehicle into vlistOHT
			print theVehicle, "\t", "return to work" to message
		end
	end 	
	else if theVehicle atBattery < vrBatteryCapa*0.75  then				
	begin 
		set theVehicle aiIndex to 7
	end 	
	else if theVehicle atBattery < vrBatteryCapa*0.80  then				
	begin 
		set theVehicle aiIndex to 8
	end 							
	else 
	begin
		set theVehicle aiIndex to 8
	end 
				
	
	if (theVehicle current path color = black or theVehicle current path color = white)						
		set theVehicle aiChargeIndex to 1
	else if  (theVehicle current path color = blue)
		set theVehicle aiChargeIndex to 1
	else if (theVehicle current path color = red)						
		set theVehicle aiChargeIndex to 2
	else 
		set theVehicle aiChargeIndex to 2
		
	if(theVehicle acOldpathcolor = red)
		set theVehicle aiChargeIndex to 2
				
	set theVehicle arAddBattery = 0
	

	if(theVehicle arOldvelocity = 0) then 
	begin 
		if(theVehicle arOldaccel =0) then 
		begin 
			if(theVehicle current velocity =0) then
			begin 
				if(theVehicle current acceleration > 0) then // acc start 
				begin 														
					if ( theVehicle asOldstatus = "Retrieve Pickup" or theVehicle asOldstatus = "Deliver Setdown")then
						set theVehicle arAddBattery to (vrBattery_Pick(theVehicle aiChargeIndex, theVehicle aiIndex) * (ac-theVehicle atOldtime))
					else 	
						set theVehicle arAddBattery to (vrBattery_Idle(theVehicle aiChargeIndex, theVehicle aiIndex) * (ac-theVehicle atOldtime))
						
					set theVehicle atBattery to theVehicle atBattery - theVehicle arAddBattery
					
					if(theVehicle arAddBattery > 0)
						set theVehicle atChargetime to  theVehicle atChargetime + (ac-theVehicle atOldtime)
								
					set theVehicle atOldtime to ac
					set theVehicle arOldaccel to theVehicle current acceleration
					set theVehicle arOldvelocity to theVehicle current velocity
					set theVehicle acOldpathcolor to theVehicle current path color
				end 
				else 
					return true
				
			end 
			else 
				return true
		end 
		else if(theVehicle arOldaccel > 0) then 
		begin 
			if(theVehicle current velocity > 0) then
			begin 
				if(theVehicle current acceleration <= 0 or (theVehicle acOldpathcolor <> theVehicle current path color)) then // acc end, constand move or dec
				begin 
				 	if(theVehicle current velocity <= 1.2 m per sec)
				 	begin 
				 		set theVehicle arAddBattery to vrBattery_Move1(theVehicle aiChargeIndex, theVehicle aiIndex)
				 		
				 		                                                 
				 	end 				
				 	else if(theVehicle current velocity <= 3.3  m per sec)
				 	begin 
				 		set theVehicle arAddBattery to ( vrBattery_Move1(theVehicle aiChargeIndex, theVehicle aiIndex)
						                               + vrBattery_Move2(theVehicle aiChargeIndex, theVehicle aiIndex))	
				 	end 
				 	else // v <= 5 m per sec
				 	begin 
				 		set theVehicle arAddBattery to (vrBattery_Move1(theVehicle aiChargeIndex, theVehicle aiIndex)
				                                        + vrBattery_Move2(theVehicle aiChargeIndex, theVehicle aiIndex)	
				                                        + vrBattery_Move3(theVehicle aiChargeIndex, theVehicle aiIndex))							
				 	end
				 	
				 	set theVehicle atBattery to theVehicle atBattery - theVehicle arAddBattery
				 	
					if(theVehicle arAddBattery > 0)
						set theVehicle atChargetime to  theVehicle atChargetime + (ac-theVehicle atOldtime)
				
				 	if(theVehicle current acceleration < 0 and theVehicle current velocity = 3.3 m per sec)	// Regenerative 5m/s
					begin  
						set theVehicle arAddBattery to vrBattery_Dec(theVehicle aiChargeIndex, theVehicle aiIndex)
						set theVehicle atBattery to theVehicle atBattery - theVehicle arAddBattery
						
						if(theVehicle arAddBattery > 0)
							set theVehicle atChargetime to  theVehicle atChargetime + (ac-theVehicle atOldtime)
					end 				 					 	
										
					set theVehicle atOldtime to ac
					set theVehicle arOldaccel to theVehicle current acceleration
					set theVehicle arOldvelocity to theVehicle current velocity   
					set theVehicle acOldpathcolor to theVehicle current path color			 	
				end 
				else 
				begin 					
					return true //3
				end 					
			end 
			else 
				return true //4			
		end 
		else 
			return true 
	end 
	else if(theVehicle arOldvelocity > 0) then 
	begin 
		if(theVehicle arOldaccel = 0) then 
		begin 	
			if(theVehicle current velocity > 0) then
			begin 
				if(theVehicle current acceleration > 0) then // acc start
				begin 
					set theVehicle arAddBattery to ((vrBattery_Move4(theVehicle aiChargeIndex, theVehicle aiIndex) * (ac-theVehicle atOldtime)))
					set theVehicle atBattery to theVehicle atBattery - theVehicle arAddBattery
					
					if(theVehicle arAddBattery > 0)
						set theVehicle atChargetime to  theVehicle atChargetime + (ac-theVehicle atOldtime)
					
					set theVehicle atOldtime to ac
					set theVehicle arOldaccel to theVehicle current acceleration
					set theVehicle arOldvelocity to theVehicle current velocity
					set theVehicle acOldpathcolor to theVehicle current path color
				end 
				else if(theVehicle current acceleration < 0) then // dec start
				begin 
					set theVehicle arAddBattery to ((vrBattery_Move4(theVehicle aiChargeIndex, theVehicle aiIndex) * (ac-theVehicle atOldtime)))
					set theVehicle atBattery to theVehicle atBattery - theVehicle arAddBattery
					
					if(theVehicle arAddBattery > 0)
						set theVehicle atChargetime to  theVehicle atChargetime + (ac-theVehicle atOldtime)
										
					if(theVehicle current velocity = 3.3 m per sec) then // Regenerative 5m/s 
					begin
						set theVehicle arAddBattery to vrBattery_Dec(theVehicle aiChargeIndex, theVehicle aiIndex)	
						set theVehicle atBattery to theVehicle atBattery - theVehicle arAddBattery
						
						if(theVehicle arAddBattery > 0)
							set theVehicle atChargetime to  theVehicle atChargetime + (ac-theVehicle atOldtime)
					end
					 
					set theVehicle atOldtime to ac
					set theVehicle arOldaccel to theVehicle current acceleration
					set theVehicle arOldvelocity to theVehicle current velocity
					set theVehicle acOldpathcolor to theVehicle current path color
						
				end	
				else 
					return true 			
			end 
			else 
				return true 
		end 
		else if(theVehicle arOldaccel > 0) then 		
		begin 
			if(theVehicle current velocity > 0) then
			begin 
				if(theVehicle current acceleration <= 0 or (theVehicle acOldpathcolor <> theVehicle current path color)) then // contant move or dec // add acc gap
				begin 
					if(theVehicle current velocity <= 1.2 m per sec) then
				 	begin 
				 		set theVehicle arAddBattery to vrBattery_Move1(theVehicle aiChargeIndex, theVehicle aiIndex)    
						                                            
				 	end 				
				 	else if(theVehicle current velocity <= 3.3 m per sec)
				 	begin 
				 		if(theVehicle arOldvelocity < 1.2 m per sec) then 
				 		begin 
					 		set theVehicle arAddBattery to (vrBattery_Move1(theVehicle aiChargeIndex, theVehicle aiIndex)
							                              + vrBattery_Move2(theVehicle aiChargeIndex, theVehicle aiIndex))
						end 
						else 
						begin 						
							set theVehicle arAddBattery to vrBattery_Move2(theVehicle aiChargeIndex, theVehicle aiIndex)	
							
						end 						                                                   
				 	end 
				 	else // v <= 5
				 	begin 
				 		if(theVehicle arOldvelocity < 1.2 m per sec) then 
				 		begin 
					 		set theVehicle arAddBattery to (vrBattery_Move1(theVehicle aiChargeIndex, theVehicle aiIndex)
		                                                 	+ vrBattery_Move2(theVehicle aiChargeIndex, theVehicle aiIndex)	
		                                                    + vrBattery_Move3(theVehicle aiChargeIndex, theVehicle aiIndex))
						end 
						else if(theVehicle arOldvelocity < 3.3 m per sec) then 
				 		begin 
					 		set theVehicle arAddBattery to (vrBattery_Move2(theVehicle aiChargeIndex, theVehicle aiIndex)	
							                                 + vrBattery_Move3(theVehicle aiChargeIndex, theVehicle aiIndex))
						end 
						else
						begin 
					 		set theVehicle arAddBattery to vrBattery_Move3(theVehicle aiChargeIndex, theVehicle aiIndex)
						end		
																										                                                     
				 	end 
				 	
				 	set theVehicle atBattery to theVehicle atBattery - theVehicle arAddBattery
				 	
					if(theVehicle arAddBattery > 0)
						set theVehicle atChargetime to  theVehicle atChargetime + (ac-theVehicle atOldtime)
						
				 	if(theVehicle current acceleration < 0 and theVehicle current velocity = 3.3 m per sec)	// Regenerative 5m/s
					begin  
						set theVehicle arAddBattery to vrBattery_Dec(theVehicle aiChargeIndex, theVehicle aiIndex)
						set theVehicle atBattery to theVehicle atBattery - theVehicle arAddBattery
						
						if(theVehicle arAddBattery > 0)
							set theVehicle atChargetime to  theVehicle atChargetime + (ac-theVehicle atOldtime)
					end 	
					
				 	set theVehicle atOldtime to ac  
				 	set theVehicle arOldaccel to theVehicle current acceleration
					set theVehicle arOldvelocity to theVehicle current velocity
					set theVehicle acOldpathcolor to theVehicle current path color
				end 
				else 
				begin 										
					return true	//8			
				end 	
			end 
			else 
				return true	
		end 
		else if(theVehicle arOldaccel < 0) then 		
		begin 
			if(theVehicle current acceleration >= 0) then			
			begin
				set theVehicle atOldtime to ac	
				set theVehicle arOldaccel to theVehicle current acceleration
				set theVehicle arOldvelocity to theVehicle current velocity
				set theVehicle acOldpathcolor to theVehicle current path color
			end
			else 
				return true//10
		end		
		else 
			return true								
	end 		
	
	if theVehicle atBattery > vtBatteryMax then				
		set theVehicle atBattery to vtBatteryMax	
									
	return true
end
				





