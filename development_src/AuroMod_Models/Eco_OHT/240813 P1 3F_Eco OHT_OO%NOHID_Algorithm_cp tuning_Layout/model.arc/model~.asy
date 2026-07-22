VERSION 12.6.1.12
SYSTYPE Process
UNITS Millimeters Seconds
SYSDEF UtilByAvail off RefCheck on debugger on warningMessages off report standard
FLAGS
	System Inherit
	Text Invisible Red
	Resources Invisible Inherit
	Resource Names Invisible Red SCALE 0.5
	Queues Invisible Inherit
	Queue Names Invisible Red SCALE 0.5
	Queue Amounts Invisible Red SCALE 0.5
	Blocks Invisible Inherit
	Block Names Invisible LtYellow SCALE 0.5
	Labels Red
PROCDEF UserId 1
TYPE name IntegerList TYPEtype list Integer
	CTYPE "AM_IntegerList*"
	TYPE2STRING "AM_IntegerListToStr"
TYPE name RealList TYPEtype list Real
	CTYPE "AM_RealList*"
	TYPE2STRING "AM_RealListToStr"
TYPE name CounterList TYPEtype list CounterPtr
	CTYPE "AM_CounterList*"
	TYPE2STRING "AM_CounterListToStr"
PROC name pCreate 0 traf Infinite
PROC name pMakeRoute 0 traf Infinite
PROC name pMove 0 traf Infinite
PROC name pExit 0 traf Infinite
PROC name pDispatch 0 traf Infinite
PROC name pReAssign 0 traf Infinite
PROC name pBatteryCheck 0 traf Infinite
PROC name pIdleCheck 0 traf Infinite
PROC name pCapaUp 0 traf Infinite
PROC name pPathCount 0 traf Infinite
PROC name pVehiclePathColor 0 traf Infinite
PROC name pCreate2 0 traf Infinite
PROC name pDispatchR 0 traf Infinite
LDTYPE name lFOUP 0
picpos endx 1
 template Millimeters
700 17
2 2 0 1 1 none
1
310 0
1 1 1 1 1 0 0
end
LDTYPE name lCreate 0
picpos endx 1
 template Millimeters
700 17
2 2 0 1 1 none
1
310 0
1 1 1 1 1 0 0
end
		create con 0 Seconds stream stream_lCreate_1 foa con 0 Seconds stream stream_lCreate_1 First pCreate 0 Limit 1
		create con 0 Seconds stream stream_lCreate_2 foa con 0 Seconds stream stream_lCreate_2 First pDispatch 0 Limit 1
		create con 0 Seconds stream stream_lCreate_4 First pBatteryCheck 0 Limit 1
		create con 5 Seconds stream stream_lCreate_3 First pIdleCheck 0 Limit 0
		create con 5 Seconds stream stream_lCreate_5 First pCapaUp 0 Limit 0
		create con 3600 Seconds stream stream_lCreate_6 First pPathCount 0 Limit 0
		create con 0 Seconds stream stream_lCreate_7 First pVehiclePathColor 0 Limit 1
		create con 0 Seconds stream stream_lCreate_8 First pCreate2 0 Limit 0
		create con 0 Seconds stream stream_lCreate_9 First pDispatchR 0 Limit 0
		create con 0 Seconds stream stream_lCreate_10 First pMove 0 Limit 0
RSRC name rOHT 0 cap 2147483647 prtime con 5 Seconds stream stream_rOHT_1

	UserDef
		
QUEUE name qStorage 0 cap 2147483647

	UserDef

QUEUE name qSpace 0 cap 2147483647

	UserDef

QUEUE name qDisable 0 cap 2147483647

	UserDef

LABEL name lblName 0
 dis 0 picpos begx -451344.032 begy 181372 endx -451343.032 endy 181372 scx 10000 scy 8000

	UserDef color 4	template Millimeters
140 49
4 4 0 1 1 Label
ECO P5_1_38
end
LABEL name lblOHT 0
 dis 0 picpos begx -283978.016 begy 157759.008 endx -283977.016 endy 157759.008 scx 5000 scy 5000 scz 5000

	UserDef	template Millimeters
140 49
1 1 0 1 1 Label
Number of OHT:
end
LABEL name Label1 0
LABEL name lblCapa 0
 dis 0 picpos begx -283978.016 begy 166735.008 endx -283977.016 endy 166735.008 scx 5000 scy 5000 scz 5000

	UserDef	template Millimeters
140 49
1 1 0 1 1 Label
Capa : 
end
ORDER name ol_Disable 0
BLOCK name B_VehicleLift 50 cap 1
	color 1 4
	color 2 4
	color 3 4
	color 4 4
	color 5 4
	color 6 4
	color 7 4
	color 8 4
	color 9 4
	color 10 4
	color 11 4
	color 12 4
	color 13 4
	color 14 4
	color 15 4
	color 16 4
	color 17 4
	color 18 4
	color 19 4
	color 20 4
	color 21 4
	color 22 4
	color 23 4
	color 24 4
	color 25 4
	color 26 4
	color 27 4
	color 28 4
	color 40 1
	color 41 1
	color 42 1
	color 43 1
	color 44 1
	color 45 1
	color 46 1
	color 47 1
	color 48 1

	UserDef	template Millimeters
700 17
-1 -1 0 1 1 none
1
310 17
-1 -1 0 1 0 none
4 4 4 4 4 0 0
end
BLOCK name B_block 3 cap 2147483647
 dis 1 picpos begx -256371.008 begy 71594 endx -256370.008 endy 71594 scx 120000 scy 900 scz 100
 dis 2 picpos begx -255798 begy 132617 endx -255797 endy 132617 scx 120000 scy 900 scz 100
 dis 3 picpos begx -259495.008 begy 3446 endx -259494.008 endy 3446 scx 120000 scy 900 scz 100

	UserDef	template Millimeters
700 17
-1 -1 0 1 1 none
1
310 17
-1 -1 0 1 0 none
4 4 4 4 4 0 0
end
COUNT name cWIP 0 cap Infinite
COUNT name cLoadMakeID 10 cap Infinite
COUNT name cBatteryCycle 1000 cap Infinite
COUNT name cChargingOHT 0 cap Infinite
TABLE name tQT 0 bins 1 0 1
TABLE name tUTT 0 bins 1 0 1
TABLE name tLTT 0 bins 1 0 1
TABLE name tTT 0 bins 1 0 1
TABLE name tDT 0 bins 1 0 1
TABLE name tDelDistance 0 bins 1 0 1
TABLE name tRetDistance 0 bins 1 0 1
TABLE name tTotDistance 0 bins 1 0 1
TABLE name tAssign 0 bins 1 0 1
TABLE name tUnloadMove 0 bins 1 0 1
TABLE name tLoadMove 0 bins 1 0 1
TABLE name tAssignInit 0 bins 1 0 1
TABLE name tLoadMove2 0 bins 1 0 1
TABLE name tBatteryChange_Ret 0 bins 1 0 1
TABLE name tBatteryChange_Del 0 bins 1 0 1
TABLE name tBatteryChange_Idle 0 bins 1 0 1
ATT name anRoute 0 type Integer
ATT name atInitialCreated 0 type Time
ATT name arTimeGap 0 type Real
ATT name atAfterTimeGap 0 type Time
ATT name atCreate 0 type Time
ATT name anTransfer 0 type Integer
ATT name atTR 0 type Time
ATT name alocFrom 0 type Location
ATT name aDistance 0 type Distance
ATT name aRetDistance 0 type Distance
ATT name alocStorage 0 type Location
ATT name atLoad 0 type Time
ATT name aDelDistance 0 type Distance
ATT name aTotDistance 0 type Distance
ATT name alocTo 0 type Location
ATT name alocFromBay 0 type Integer
ATT name alocToBay 0 type Integer
ATT name atAssign 0 type Time
ATT name atUnload 0 type Time
ATT name aID 0 type Integer
ATT name aAssign 0 type Integer
ATT name aParkBay 0 type Integer
ATT name avDispatch 0 type VehiclePtr
ATT name aRoute_ToLoc 0 type LocationList
ATT name aRoute_FromLoc 0 type LocationList
ATT name anFromtoType 0 type Integer
ATT name alocPark 0 type Location
ATT name atAssignInit 0 type Time
ATT name aiSTKTL 1 2 type Integer
ATT name aPickup 0 type Real
ATT name aSetdown 0 type Real
ATT name atcheck 0 type Time
ATT name atLoad2 0 type Time
ATT name A_cgStopDelay 0 type Time
ATT name A_cgStopOccur 0 type Integer
ATT name A_cgStopTotalDelay 0 type Time
ATT name A_cgStopVeh 0 type VehiclePtr
ATT name atBattery 0 type Real
ATT name atOldtime 0 type Time
ATT name arOldaccel 0 type Real
ATT name arOldvelocity 0 type Real
ATT name aiIndex 0 type Integer
ATT name aiRecharge 0 type Integer
ATT name aiChargeIndex 0 type Integer
ATT name acOldpathcolor 0 type Color
ATT name arAddBattery 0 type Real
ATT name asOldstatus 0 type String
ATT name atChargetime 0 type Time
ATT name aiRouteChange 0 type Integer
ATT name atRedIn 0 type Time
ATT name atBatteryRedIn 0 type Time
ATT name atBalckIn 0 type Time
ATT name atBatteryBlackIn 0 type Time
ATT name atBlackIn 0 type Time
ATT name atBatteryRedkIn 0 type Time
ATT name atBattery_Del 0 type Time
ATT name atBattery_Ret 0 type Time
ATT name atBattery_Idle 0 type Time
ATT name aiLoadMakeID 0 type Integer
ATT name atNoHID_Start 0 type Time
ATT name aiPathSearched 0 type Integer
ATT name aiCheck 0 type Integer
ATT name aiUnder50 0 type Integer
ATT name atRedStart 0 type Time
VAR name vnRoute 0 type Integer
VAR name i 0 type Integer
VAR name vfpInFromto 0 type FilePtr
VAR name vfpInControl 0 type FilePtr
VAR name vfpInSTKTL 0 type FilePtr
VAR name vfpOutResult 1 20 type FilePtr
VAR name vsStream 1 3 type String
VAR name viaStream 1 5 type Integer
VAR name vsaStream 1 3 type String
VAR name vroute_Interval 2 3 99999 type Real
VAR name vroute_FromLoc 2 3 99999 type String
VAR name vroute_FromBay 2 2 99999 type Integer
VAR name vroute_ToLoc 2 3 99999 type String
VAR name vroute_ToBay 2 2 99999 type Integer
VAR name vrNormalVelocity 0 type Real
VAR name vrCurveVelocity 0 type Real
VAR name vrAcceleration 0 type Real
VAR name vrDeceleration 0 type Real
VAR name vrBrakeDistance 0 type Real
VAR name vrStopDistance 0 type Real
VAR name vtResume 0 type Time
VAR name vtLoading 1 2 type Time
VAR name vnOHT 0 type Integer
VAR name vtRun 0 type Time
VAR name vtSchedule 0 type Time
VAR name vtPriorityCost 0 type Time
VAR name vnTimeWeight 0 type Integer
VAR name vtTimeLimit 0 type Time
VAR name vnPark 0 type Integer
VAR name vlocTemp 1 10 type Location
VAR name vlocParkList 0 type LocationList
VAR name vnRequest 0 type Integer
VAR name vnComplete 0 type Integer
VAR name vnDelay 0 type Integer
VAR name vNum 0 type Integer
VAR name o 0 type Integer
VAR name vlistLoad 1 2 type LoadList
VAR name vstrTemp 0 type String
VAR name vstrTemp2 0 type String
VAR name vcOHT 0 type Integer
VAR name vlistOHT 0 type VehicleList
VAR name vlocSTKTL 0 type Location
VAR name vlocPark 0 type Location
VAR name vsParkBayNum 0 type String
VAR name viParkBayNum 0 type Integer
VAR name vlTemp2 0 type LoadPtr
VAR name vlSelect 0 type LoadPtr
VAR name vvSelect 0 type VehiclePtr
VAR name vtSelect 0 type Time
VAR name vohtTemp 0 type VehiclePtr
VAR name vlTemp 0 type LoadPtr
VAR name vrDistance 1 2 type Real
VAR name vtCost 0 type Time
VAR name vJob 0 type SchedJobPtr
VAR name viCheck 0 type Integer
VAR name vrDistanceTemp 0 type Real
VAR name k 0 type Integer
VAR name j 0 type Integer
VAR name vi 0 type Integer
VAR name vLocListpm 0 type LocationList
VAR name vfpInControl2 0 type FilePtr
VAR name viTemp 1 100 type Integer
VAR name vfpInFromto2 0 type FilePtr
VAR name vrOHTspec 0 type Real
VAR name vnCapa 0 type Integer
VAR name vsTemp 1 10 type String
VAR name viParkTemp 0 type Integer
VAR name vsParkPoint 0 type String
VAR name viSTKnum 0 type Integer
VAR name vrCapa 0 type Real
VAR name vraStream 1 10 type Real
VAR name vroute_Pickup 2 2 99999 type Real
VAR name vroute_Setdown 2 2 99999 type Real
VAR name vrTemp 0 type Real
VAR name vrTemp2 0 type Real
VAR name vtTemp 0 type Time
VAR name vfpCongLog 0 type FilePtr
VAR name vfpInFromto3 0 type FilePtr
VAR name vllpm 0 type LocationList
VAR name vohtTemp_Bat 0 type VehiclePtr
VAR name vlistOHT_Bat 0 type VehicleList
VAR name vrBatteryCapa 0 type Real
VAR name vrBattery_Pick 2 2 100 type Real
VAR name vrBattery_Idle 2 2 100 type Real
VAR name vrBattery_Move1 2 2 100 type Real
VAR name vrBattery_Move2 2 2 100 type Real
VAR name vrBattery_Move3 2 2 100 type Real
VAR name vrBattery_Dec 2 2 100 type Real
VAR name vrBattery_Move4 2 2 100 type Real
VAR name vtBatteryMax 0 type Time
VAR name vtBatteryMin 0 type Time
VAR name vfpBatcharge 0 type FilePtr
VAR name viTempBat 0 type Integer
VAR name vrRecharge 0 type Real
VAR name vfpAvoidingBayEnd 0 type FilePtr
VAR name vll_ABE 0 type LocationList
VAR name vllocation 1 2200 type Location
VAR name vrlDistance 1 99999 type Real
VAR name vilIndex 1 99999 type Integer
VAR name vipivot 0 type Integer
VAR name vj 0 type Integer
VAR name vrtemp 0 type Real
VAR name vfpReRoute 0 type FilePtr
VAR name vll_RR 0 type LocationList
VAR name vlistOHTall 0 type VehicleList
VAR name viBC_move 0 type Integer
VAR name viBC_retrieve 0 type Integer
VAR name viBC_deliver 0 type Integer
VAR name viBR_move 0 type Integer
VAR name viBR_retrieve 0 type Integer
VAR name viBR_deliver 0 type Integer
VAR name vtRedInMax 1 1000 type Time
VAR name vtBatteryTemp 1 1000 type Time
VAR name vllpurple 0 type LocationList
VAR name vcROHT 0 type Integer
VAR name vnROHT 0 type Integer
VAR name vlistROHT 0 type VehicleList
VAR name vlistROHT_Bat 0 type VehicleList
VAR name vfpAvoidingBayEnd_R 0 type FilePtr
VAR name vll_ABE_R 0 type LocationList
VAR name vrDistanceRpark 1 10 type Real
VAR name vrBigValue 0 type Real
VAR name vllDM 0 type LocationList
VAR name viSize 0 type Integer
VAR name vllTemp 0 type LocationList
VAR name vrDM 2 2200 2200 type Real
VAR name vrDist 1 2200 type Real
VAR name vipred 1 2200 type Integer
VAR name viFound 1 2200 type Integer
VAR name uu 0 type Integer
VAR name vllRoute 0 type LocationList
VAR name vi_Ch 0 type Integer
VAR name vrMin 0 type Real
VAR name viMin_pos 0 type Integer
VAR name vrMinDistance 0 type Real
VAR name viMinDistIndex 1 2200 type Integer
VAR name vloc_MinDist 0 type Location
VAR name vrMinDist 0 type Real
VAR name vrDistMin 0 type Real
VAR name vlocMin 0 type Location
VAR name vfpDistance 0 type FilePtr
VAR name vfpClosetNode 1 10 type FilePtr
VAR name vlocClosestFr 2 2 3500 type Location
VAR name vlocClosestTo 2 2 3500 type Location
VAR name viClosetFr 2 2 3000 type Integer
VAR name viClosetTo 2 2 3000 type Integer
VAR name vfpVLLDM 0 type FilePtr
VAR name viMinIndex 0 type Integer
VAR name vfpOutFroomto 0 type FilePtr
VAR name vfpTemp 0 type FilePtr
VAR name vllInherit 0 type LocationList
VAR name vnRequest2 0 type Integer
VAR name vllLower 0 type LocationList
VAR name vllUpper 0 type LocationList
VAR name vrEfficiency 0 type Real
VAR name vJob2 0 type SchedJobPtr
VAR name vllChargeRoute 0 type LocationList
VAR name vfpTimeInRed 0 type FilePtr
VAR name xr 0 type Real
VAR name yr 0 type Real
VAR name er 0 type Real
RNSTREAM stream0 0 type CMRG flags 1
	cmrgseed 1 12345 12345 12345 12345 12345 12345
RNSTREAM stream_LoadType1_1 0 type CMRG flags 1
	title "Generated automatically for LoadType1"
	cmrgseed 1 3692455944 1366884236 2968912127 335948734 4161675175 475798818
RNSTREAM stream_rOHT_1 0 type CMRG flags 1
	title "Generated automatically for rOHT"
	cmrgseed 1 1015873554 1310354410 2249465273 994084013 2912484720 3876682925
RNSTREAM stream_lCreate_1 0 type CMRG flags 1
	title "Generated automatically for lCreate"
	cmrgseed 1 2338701263 1119171942 2570676563 317077452 3194180850 618832124
RNSTREAM stream_lCreate_2 0 type CMRG flags 1
	title "Generated automatically for lCreate"
	cmrgseed 1 1597262096 3906379055 3312112953 1016013135 4099474108 275305423
RNSTREAM stream_lCreate_4 0 type CMRG flags 1
	title "Generated automatically for lCreate"
	cmrgseed 1 796079799 2105258207 955365076 2923159030 4116632677 3067683584
RNSTREAM stream_lCreate_3 0 type CMRG flags 1
	title "Generated automatically for lCreate"
	cmrgseed 1 3281794178 2616230133 1457051261 2762791137 2480527362 2282316169
RNSTREAM stream_lCreate_5 0 type CMRG flags 1
	title "Generated automatically for lCreate"
	cmrgseed 1 3777646647 1837464056 4204654757 664239048 4190510072 2959195122
RNSTREAM stream_lCreate_6 0 type CMRG flags 1
	title "Generated automatically for lCreate"
	cmrgseed 1 4215590817 3862461878 1087200967 1544910132 936383720 1611370123
RNSTREAM stream_lCreate_7 0 type CMRG flags 1
	title "Generated automatically for lCreate"
	cmrgseed 1 1683636369 362165168 814316280 869382050 980203903 2062101717
RNSTREAM stream_lCreate_8 0 type CMRG flags 1
	title "Generated automatically for lCreate"
	cmrgseed 1 272317999 166758548 310112982 201045826 1680231254 118290799
RNSTREAM stream_lCreate_9 0 type CMRG flags 1
	title "Generated automatically for lCreate"
	cmrgseed 1 2245755202 1652682525 2865544364 721509566 209733568 592362218
RNSTREAM stream_lCreate_10 0 type CMRG flags 1
	title "Generated automatically for lCreate"
	cmrgseed 1 3003961408 3529909391 14538032 3603919910 566682685 1235016484
RNSTATE 596094074 2279636413 3050913596 1739649456 2368706608 3058697049
GRAPH  bgOHT_QSize timeline every 1 Minutes x 195 y 570 width 600 height 350 ymax 1000 ymin 0 yinc 100 xmin 0 xmax 9 xinc 1 xunits Hours
 include AGVS pm loadclaimed cur title "Lot (Waited)"
 include Process model cWIP cur title "Lot (Total)"
GRAPH  bgOHT_TT timeline every 1 Minutes x 195 y 570 width 600 height 350 ymax 240 ymin 0 yinc 50 xmin 0 xmax 9 xinc 1 xunits Hours
 include Process model tQT 0 mean_r title "QT"
 include Process model tUTT 0 mean_r title "UTT"
 include Process model tLTT 0 mean_r title "LTT"
 include Process model tTT 0 mean_r title "TT"
 include Process model tDT 0 mean_r title "DT"
GRAPH  bgOHT_Util timeline every 1 Minutes x 195 y 570 width 600 height 350 ymax 100 ymin 0 yinc 20 xmin 0 xmax 9 xinc 1 xunits Hours
FUNC name fsetValuable_FilePtr type Integer
FUNC name freadFromto type Integer
FUNC name freadOHTSpec type Integer
FUNC name freadControl type Integer
FUNC name freadSTKTL type Integer
FUNC name fDispatchToNextPark type Integer PARAM name theVehicle type VehiclePtr PARAM name theCurrentBay type Integer
FUNC name freadFromto2 type Integer
FUNC name freadFromto3 type Integer
FUNC name freadBatchare type Integer
FUNC name freadBatcharge type Integer
FUNC name F_QuickSort type Integer PARAM name Arg1 type Integer PARAM name Arg2 type Integer
FUNC name fDistanceMatrix type Integer
FUNC name F_Dijkstra type Integer PARAM name Arg_Start type Integer PARAM name Arg_End type Integer PARAM name theVehicle type VehiclePtr
FUNC name F_Choose type Integer
FUNC name F_Sqrt type Real PARAM name input type Real
SUBRTN name sSetFromLocation
SUBRTN name sSetToLocation
SUBRTN name sReport
SUBRTN name sCheckSTKTL
SUBRTN name sSetStorageLocation
SUBRTN name sSetUnloadLoad
SFileBegin	name init.m
begin model initialization function
	set vnRoute = 40723			/* Numbers of line in Fromto File */
	set vrCapa = 1.64			/* Needs to check */
	set vnOHT = 600				/* Input Numbers of OHT */
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


#@!
SFileBegin	name logic.m
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
	
	if alocFrom color = cyan or alocTo color = cyan then
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
	send to pExit
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

	

#@!
SFileBegin	name vehicle.m
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

#@!
SFileBegin	name battery.m
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
				





#@!
SFileBegin	name pathcount.m
/*begin pPathCount arriving procedure
print
pm.path4147 relative total, "\t",
pm.path3674 relative total, "\t",
pm.path4755 relative total, "\t",
pm.path6430 relative total, "\t",
pm.path3194 relative total, "\t",
pm.path5331 relative total, "\t",
pm.path7082 relative total, "\t",
pm.path5786 relative total, "\t",
pm.path6075 relative total, "\t",
pm.path2606 relative total, "\t",
pm.path6699 relative total, "\t",
pm.path2140 relative total, "\t",
pm.path7747 relative total, "\t",
pm.path1558 relative total, "\t",
pm.path7607 relative total, "\t",
pm.path4841 relative total, "\t",
pm.path1365 relative total, "\t",
pm.path4241 relative total, "\t",
pm.path1057 relative total, "\t",
pm.path8792 relative total, "\t",
pm.path9799 relative total, "\t",
pm.path10800 relative total, "\t",
pm.path615 relative total, "\t",
pm.path9202 relative total, "\t",
pm.path3934 relative total, "\t",
pm.path9639 relative total, "\t",
pm.path9061 relative total, "\t",
pm.path287 relative total, "\t",
pm.path11916 relative total, "\t",
pm.path7568 relative total, "\t",
pm.path2740 relative total, "\t",
pm.path90 relative total, "\t",
pm.path1595 relative total, "\t",
pm.path5268 relative total, "\t",
pm.path1097 relative total, "\t",
pm.path10508 relative total, "\t",
pm.path12565 relative total, "\t",
pm.path324 relative total, "\t",
pm.path10131 relative total, "\t",
pm.path572 relative total, "\t",
pm.path482 relative total, "\t",
pm.path3995 relative total, "\t",
pm.path11258 relative total, "\t",
pm.path3135 relative total, "\t",
pm.path13317 relative total, "\t",
pm.path132 relative total, "\t",
pm.path9570 relative total, "\t",
pm.path8802 relative total, "\t",
pm.path13231 relative total, "\t",
pm.path115 relative total, "\t",
pm.path2182 relative total, "\t",
pm.path12059 relative total, "\t",
pm.path7629 relative total, "\t",
pm.path506 relative total, "\t",
pm.path12740 relative total, "\t",
pm.path1992 relative total, "\t",
pm.path1088 relative total, "\t",
pm.path13241 relative total, "\t",
pm.path6509 relative total, "\t",
pm.path5139 relative total, "\t",
pm.path1203 relative total, "\t",
pm.path2950 relative total, "\t",
pm.path2573 relative total, "\t",
pm.path4405 relative total, "\t",
pm.path1150 relative total, "\t",
pm.path1208 relative total, "\t",
pm.path4016 relative total, "\t",
pm.path4535 relative total, "\t",
pm.path3148 relative total, "\t",
pm.path3854 relative total, "\t",
pm.path4932 relative total, "\t",
pm.path2011 relative total, "\t",
pm.path5646 relative total, "\t",
pm.path5771 relative total, "\t",
pm.path2804 relative total, "\t",
pm.path2919 relative total, "\t",
pm.path6922 relative total, "\t",
pm.path3322 relative total, "\t",
pm.path3326 relative total, "\t",
pm.path4691 relative total, "\t",
pm.path7186 relative total, "\t",
pm.path7832 relative total, "\t",
pm.path7719 relative total, "\t",
pm.path4377 relative total, "\t",
pm.path8092 relative total, "\t",
pm.path8313 relative total, "\t",
pm.path5850 relative total, "\t",
pm.path5472 relative total, "\t",
pm.path8959 relative total, "\t",
pm.path8864 relative total, "\t",
pm.path9464 relative total, "\t",
pm.path7144 relative total, "\t",
pm.path9536 relative total, "\t",
pm.path9827 relative total, "\t",
pm.path6875 relative total, "\t",
pm.path10299 relative total, "\t",
pm.path10382 relative total, "\t",
pm.path10464 relative total, "\t",
pm.path7901 relative total, "\t",
pm.path8510 relative total, "\t",
pm.path9506 relative total, "\t",
pm.path10665 relative total, "\t",
pm.path10997 relative total, "\t",
pm.path10986 relative total, "\t",
pm.path10351 relative total, "\t",
pm.path11410 relative total, "\t",
pm.path11535 relative total, "\t",
pm.path7402 relative total, "\t",
pm.path11667 relative total, "\t",
pm.path11775 relative total, "\t",
pm.path10967 relative total, "\t",
pm.path12324 relative total, "\t",
pm.path8817 relative total, "\t",
pm.path12693 relative total, "\t",
pm.path12792 relative total, "\t",
pm.path9867 relative total, "\t",
pm.path12307 relative total, "\t",
pm.path13215 relative total, "\t",
pm.path13017 relative total, "\t",
pm.path10434 relative total, "\t",
pm.path13384 relative total, "\t",
pm.path13399 relative total, "\t",
pm.path13376 relative total, "\t",
pm.path11285 relative total, "\t",
pm.path13475 relative total, "\t",
pm.path13929 relative total, "\t",
pm.path13831 relative total, "\t",
pm.path11838 relative total, "\t",
pm.path14583 relative total, "\t",
pm.path12503 relative total, "\t",
pm.path14641 relative total, "\t",
pm.path14929 relative total, "\t",
pm.path12921 relative total, "\t",
pm.path15066 relative total, "\t",
pm.path13356 relative total, "\t",
pm.path15254 relative total, "\t",
pm.path13730 relative total, "\t",
pm.path15659 relative total, "\t",
pm.path15957 relative total, "\t",
pm.path14319 relative total, "\t",
pm.path16100 relative total, "\t",
pm.path16491 relative total, "\t",
pm.path16607 relative total, "\t",
pm.path14976 relative total, "\t",
pm.path16729 relative total, "\t",
pm.path15304 relative total, "\t",
pm.path15718 relative total, "\t",
pm.path15996 relative total, "\t",
pm.path17124 relative total, "\t",
pm.path16975 relative total, "\t",
pm.path16405 relative total, "\t",
pm.path16695 relative total, "\t",
pm.path10838 relative total, "\t",
pm.path10839 relative total, "\t"

	
	to vfpOutResult(5)

end

*/

#@!
