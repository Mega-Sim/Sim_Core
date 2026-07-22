begin pStart arriving
    
    clone 1 load to pTimeDel
	/*변수 설정*/
	open "arc/eqToeq.dat" for reading save result as vfpRead
	
	/*fromto 파일 읽어들이기*/
	set vi to 1
	while vfpRead eof = 0 do
	begin
		read vStrTmp from vfpRead with delimiter "\n"
		read vFromEqsName, vToEqsName,	vLotPerHour from vStrTmp with delimiter "\t"
			/*
			vFromEqsName = From 설비군 명(Str)  
			vToEqsName = To 설비군 명(Str)
			vLotPerHour = 시간당 Lot 수(int)
			*/
		
		if vFromEqsName index("-") <= vFromEqsName length then
			set vFromEqsName substring(vFromEqsName index("-"), 1) = "_"
			
		if vToEqsName index("-") <= vToEqsName length then
			set vToEqsName substring(vToEqsName index("-"), 1) = "_"
			
		if vFromEqsName substring(1,1) <> "*" then
		begin		
			print "pm:cp_"vFromEqsName to vStrTmp
			set lapFromEq to vStrTmp
			print "pm:cp_"vToEqsName to vStrTmp
			set lapToEq to vStrTmp
			set larLotPerHour to vLotPerHour
			clone 1 load to pPreFromTo
				
/*			wait for 86400 * 3.0 / vFromToCnt sec	*/
/*			wait for (1 + 86400 * 15.0 * u 0.5, 0.5) sec	*/
			wait for 0.1 sec
			inc vi by 1
		end
		else
		begin
			if vFromEqsName substring(1,6) = "* From" then
			begin
				set vFromToCnt to vLotPerHour
			end
		end
		
	end

end

begin pPreFromTo arriving
	wait for (1 + 86400 * 15.0 * u 0.5, 0.5) sec
	clone 1 load to pFromTo
end

begin pFromTo arriving
	while 1 = 1 do
	begin
		clone 1 load to pMove
		wait for n 60*60 / larLotPerHour, 60*60 / (larLotPerHour * 10) sec
	end
end



begin pMove arriving
	if lapFromEq <> null and lapToEq <> null then
	begin
		inc cWIP by 1
		if vVehicleOrTime = 1 then
		begin
    		move into lapFromEq
    		travel to lapToEq
    	end
    	else
    	begin
    		use rOHT for vOHTDel_Time sec
    	end
    	
		dec cWIP by 1
		move into qOut	
	end
	
end

begin pTimeDel arriving
    wait for vInitDel_Time sec
    set vVehicleOrTime = 1
end

