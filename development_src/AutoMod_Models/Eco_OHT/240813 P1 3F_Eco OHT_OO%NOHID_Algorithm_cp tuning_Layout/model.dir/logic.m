/*Loads based*/
begin pCreate arriving procedure
	set i = 1
	set aiLoadMakeID to 1

	set i = 1
	while i <= 1 do 
	begin
		set anRoute = 0
		while anRoute < vnRoute do
		
		begin
			inc anRoute by 1
			inc vNum by 1
			
			if vNum <= vnRoute then
			begin
				set anFromtoType = 1
				clone 1 load to pMakeRoute nlt lFOUP	/* nlt : New load type */
			end
			
			else if vNum <= (vnRoute*2-1) then
			begin
				set anFromtoType = 2
				clone 1 load to pMakeRoute nlt lFOUP
			end
			else if vNum <= (vnRoute*3-1) then
			begin
				set anFromtoType = 3
				clone 1 load to pMakeRoute nlt lFOUP
			end
			
		end	
		inc i by 1
	end
	print i to message
end

begin pMakeRoute arriving procedure
	set alocFrom to vroute_FromLoc(anFromtoType,anRoute)
	set alocTo to vroute_ToLoc(anFromtoType,anRoute)
	
	wait for uniform vroute_Interval(anFromtoType,anRoute)/2, vroute_Interval(anFromtoType,anRoute)/2 sec
	set o to 0
	while 1 = 1 do	
	begin
		if o = 0 then												/* Check if this is the first round. Proceed if it is. */
		begin
			set arTimeGap to atInitialCreated						/* Time the first round is created */
			clone 1 load to pMove									/* Load Creation */
			wait for vroute_Interval(anFromtoType,anRoute) - arTimeGap sec
			set atAfterTimeGap to ac
			wait for uniform vroute_Interval(anFromtoType,anRoute)/2, vroute_Interval(anFromtoType,anRoute)/2 sec
			inc o by 1
		end
		
		if o <> 0 then												/* Check if this is the first round. Proceed if it is not. */
		begin            
			set atCreate to ac										/* Time the nth round is created */
			set arTimeGap to atCreate - atAfterTimeGap				/* Time the nth round has waited before being created */
			clone 1 load to pMove									/* Load Creation */
			wait for vroute_Interval(anFromtoType,anRoute) - arTimeGap sec
			set atAfterTimeGap to ac								/* Time at the end of nth round interval */
			wait for u vroute_Interval(anFromtoType,anRoute)/2, vroute_Interval(anFromtoType,anRoute)/2 sec  /* Time until the next creation */
			inc o by 1
		end
	end
end

begin pCreate2 arriving procedure
	while 1=1 do
	begin
//		wait for u 3.6, 3.6 / 2
		wait for 3.6 / vrCapa
		set i to oneof(1:1, 1:2)
		if i = 1 then
		begin
			set alocFrom to vllpurple(1 + vllpurple size * u 0.5, 0.5)
			set alocTo to vllInherit(1 + vllInherit size * u 0.5, 0.5)
		end
		else
		begin
			set alocFrom to vllInherit(1 + vllInherit size * u 0.5, 0.5)
			set alocTo to vllpurple(1 + vllpurple size * u 0.5, 0.5)
		end
		clone 1 load to pMove
		inc vnRequest2 by 1
	end
end

begin pMove arriving procedure

/*	if this load index = 40733 then
		print this load to message

	if alocFrom = null then
		set alocTo to vllpm(1 + vllpm size * u 0.5, 0.5)
	else
		set alocFrom to vllpm(1 + vllpm size * u 0.5, 0.5)
	*/		
	/* Transfer */
	inc vnRequest by 1	
	
/*	if alocFrom color = cyan or alocTo color = cyan then
	begin
		insert this load into vlistLoad(2)
	end
	else 
		insert this load into vlistLoad(1)
		
	set anTransfer = 1												/* From Eq move */
	set atTR to ac													/* Time load is created */
	
	move into alocFrom
	set aDistance to this vehicle total distance traveled			/* distance measured until load placed at from location */
	set aRetDistance to aDistance - this vehicle aRetDistance		/* subtract distance between initial and assign position */
	
	travel to alocTo 
//	set atLoad to ac + this vehicle aSetdown
	set atLoad to ac + 9
	set this vehicle aSetdown to 0
	set aDelDistance to this vehicle total distance traveled - aDistance
	set aTotDistance to aRetDistance + aDelDistance
	
	call sReport
	send to pExit*/
end

begin pExit arriving procedure
	move into qSpace
	send to die
end

/* Subroutines */
begin sSetFromLocation  
	print "pm:cp_" vroute_FromLoc(anFromtoType,anRoute) to vstrTemp
	print vroute_FromBay(anFromtoType,anRoute) to vstrTemp2
	set alocFrom to vstrTemp
	set alocFromBay to vstrTemp2
end

begin sSetToLocation
	print "pm:cp_" vroute_ToLoc(anFromtoType,anRoute) to vstrTemp
	print vroute_ToBay(anFromtoType,anRoute) to vstrTemp2
	set alocTo to vstrTemp
	set alocToBay to vstrTemp2
end

begin sSetUnloadLoad
	set aPickup to vroute_Pickup(anFromtoType,anRoute)
	set aSetdown to vroute_Setdown(anFromtoType,anRoute)
end

begin sReport
	/*Distance*/
	tabulate aDelDistance in tDelDistance				/* calculate Delivery Distance */
	tabulate aRetDistance in tRetDistance				/* calculate Retreive Distance */
	tabulate aTotDistance in tTotDistance				/* calculate Total Distance */
	
	/*time*/
	tabulate atAssignInit - atTR in tAssignInit			/* calculate initial assigned time */
	tabulate atAssign - atTR in tAssign					/* calculate Total Assign Time */
	tabulate atUnload - atAssign in tUnloadMove			/* calculate moving time without load */
	tabulate atLoad - atUnload in tLoadMove				/* calculate moving time with load */
	
	inc vnComplete by 1
	if atLoad - atTR > 5 min then
		inc vnDelay by 1								/* calculate number of load delayed for more than 5 minutes */
end

	

