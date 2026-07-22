begin pm park ok function
	if vVehicleOrTime = 1 then
	begin
		if theVehicle type = "DefVehicle" then
		begin
			if theVehicle current distance parkLoc > 50000 mm then
			begin
				if parkLoc current > 1 then 
					return false
					
				for each vParkLocFoup in vParkListFoup do
				begin
					if vParkLocFoup = parkLoc then return false
				end
				
				insert parkLoc into vParkListFoup at end
				
				if vParkListFoup size > 1 then
					remove first object from vParkListFoup
				
				set theVehicle color to blue
				return true
			end
			
			return false
		end
		
		return false
	end
	return false
end

begin pm work ok function
	set theVehicle color to red
	return true
end

