// vehicle.c
// AutoMod 12.6.1 Generated File
// Build: 12.6.1.12
// Model name:	model
// Model path:	D:\Project\5. ECO OHT\models\240807~\240813 P1 3F_Eco OHT_OO%NOHID_Algorithm_cp tuning_Layout\model.dir\
// Generated:	Tue Aug 13 10:52:53 2024
// Applied/AutoMod Licensee Confidential
// NO DISTRIBUTION OR REPRODUCTION RIGHTS GRANTED!
// Copyright (c) 1988-2015 Applied Materials All rights reserved.
//
// All Rights Reserved.  Reproduction or transmission in whole or
// in part, in any form or by any means, electronic, mechanical or
// otherwise, is prohibited without the prior written consent of
// copyright owner.
//
// Licensed Material - Property of Applied Materials, Inc.
//
// Applied Materials, Inc.
// 3050 Bowers Drive
// P.O. Box 58039
// Santa Clara, CA 95054-3299
// U.S.A.
//


#include "cdecls.h"

#undef F_Dijkstra
static int32 F_Dijkstra(int32, int32, vehicle*);
#undef F_Choose
static int32 F_Choose(void);
#undef F_QuickSort
static int32 F_QuickSort(int32, int32);
#undef F_Sqrt
static double F_Sqrt(double);

static int32
pm_vehinit(vehicle* am_theVehicle)
{
	load* localactor = (load*)am_theVehicle;
	AMDebuggerBeginRoutine("vehicle.m", "Vehicle initialization function", "model.pm", localactor);
	{
		char*	names[1];
		void*	ptrs[1];
		char*	(*valstrfuncs[1])(void*);
		
		names[0] = "theVehicle";
		ptrs[0] = &am_theVehicle;
		valstrfuncs[0] = VehiclePtr_valstrfunc;
		AMDebuggerParams("model.pm", pm_vehinit, localactor, 1, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 4);
			ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_A_cgStopDelay = ToModelTime( -1, UNITSECONDS);
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 6);
			VehSetDefForNormalVel(ValidPtr(am_theVehicle, 81, vehicle*), ToModelRate(ToModelDistance(am2_vrNormalVelocity, UNITMETERS), UNITSECONDS));
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 7);
			VehSetDefForCurveVel(ValidPtr(am_theVehicle, 81, vehicle*), ToModelRate(ToModelDistance(am2_vrCurveVelocity, UNITMETERS), UNITSECONDS));
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 8);
			VehSetDefForSpurVel(ValidPtr(am_theVehicle, 81, vehicle*), ToModelRate(ToModelDistance(am2_vrCurveVelocity, UNITMETERS), UNITSECONDS));
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 10);
			VehSetDefRevNormalVel(ValidPtr(am_theVehicle, 81, vehicle*), ToModelRate(ToModelDistance(am2_vrNormalVelocity, UNITMETERS), UNITSECONDS));
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 11);
			VehSetDefRevCurveVel(ValidPtr(am_theVehicle, 81, vehicle*), ToModelRate(ToModelDistance(am2_vrCurveVelocity, UNITMETERS), UNITSECONDS));
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 12);
			VehSetDefRevSpurVel(ValidPtr(am_theVehicle, 81, vehicle*), ToModelRate(ToModelDistance(am2_vrCurveVelocity, UNITMETERS), UNITSECONDS));
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 14);
			VehSetDefAccel(ValidPtr(am_theVehicle, 81, vehicle*), FromModelTime(ToModelRate(ToModelDistance(am2_vrAcceleration, UNITMETERS), UNITSECONDS), UNITSECONDS));
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 15);
			VehSetDefDecel(ValidPtr(am_theVehicle, 81, vehicle*), FromModelTime(ToModelRate(ToModelDistance(am2_vrDeceleration, UNITMETERS), UNITSECONDS), UNITSECONDS));
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 17);
			VehSetDefBrakeDist(ValidPtr(am_theVehicle, 81, vehicle*), ToModelDistance(am2_vrBrakeDistance, UNITMETERS));
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 18);
			VehSetDefStopDist(ValidPtr(am_theVehicle, 81, vehicle*), ToModelDistance(am2_vrStopDistance, UNITMETERS));
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 20);
			ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery = am2_vrBatteryCapa * 0.80000000000000004;
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 22);
			if (StringCompare(VehGetType(ValidPtr(am_theVehicle, 81, vehicle*)), "DefVehicle") == 0) {
				{
					AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 24);
					VsegSetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(ValidPtr(am_theVehicle, 81, vehicle*))), 84, VehSeg*), 21);
					EntityChanged(0x01000040);
				}
				{
					AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 25);
					am2_vcOHT += 1;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 26);
					ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aID = am2_vcOHT;
					EntityChanged(0x00000040);
				}
				{
					AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 27);
					ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aAssign = 0;
					EntityChanged(0x00000040);
				}
				{
					AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 29);
					if (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aID <= am2_vnOHT) {
						{
							AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 31);
							ListAppendItem(VehicleList, am2_vlistOHT, am_theVehicle);	// append item to end of list
						}
						{
							AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 32);
							ListAppendItem(VehicleList, am2_vlistOHTall, am_theVehicle);	// append item to end of list
						}
						{
							AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 34);
							if (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aID <= am2_vnOHT - 400) {
								AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 35);
								ListAppendItem(VehicleList, am2_vlistOHT_Bat, am_theVehicle);	// append item to end of list
							}
						}
					}
				}
			}
			else {
				{
					AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 40);
					VsegSetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(ValidPtr(am_theVehicle, 81, vehicle*))), 84, VehSeg*), 36);
					EntityChanged(0x01000040);
				}
				{
					AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 41);
					am2_vcROHT += 1;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 42);
					ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aID = am2_vcROHT;
					EntityChanged(0x00000040);
				}
				{
					AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 43);
					ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aAssign = 0;
					EntityChanged(0x00000040);
				}
				{
					AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 45);
					if (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aID <= am2_vnROHT) {
						{
							AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 47);
							ListAppendItem(VehicleList, am2_vlistROHT, am_theVehicle);	// append item to end of list
						}
						{
							AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 48);
							ListAppendItem(VehicleList, am2_vlistROHT_Bat, am_theVehicle);	// append item to end of list
						}
						{
							AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 49);
							ListAppendItem(VehicleList, am2_vlistOHTall, am_theVehicle);	// append item to end of list
						}
					}
				}
			}
		}
		{
			AMDebugger("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor, 53);
			AMDebuggerEndRoutine("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("vehicle.m", "Vehicle initialization function", "model.pm", pm_vehinit, localactor);
} /* end of pm_vehinit */

static int32
pm_task(vehicle* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("vehicle.m", "Task search procedure", "model.pm", localactor);
	{
		char*	names[1];
		void*	ptrs[1];
		char*	(*valstrfuncs[1])(void*);
		
		names[0] = "Current";
		ptrs[0] = &this->curlocdata.sloc;
		valstrfuncs[0] = Location_valstrfunc;
		AMDebuggerParams("model.pm", pm_task, localactor, 1, names, ptrs, valstrfuncs);
	}
	switch (step) { /* Make the step switcher */
	case Step 1: goto Label1;
	case Step 2: goto Label2;
	case Step 3: goto Label3;
	default: message("Bad step number %ld.", step);
	}
	retval = Error;
	goto LabelRet;
Label1: ;  /* Step1 */
	{
		{
			AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 57);
			if (this->load.attribute->am2_aID > am2_vnOHT) {
				{
					AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 59);
					pushppa(this, pm_task, Step 2, am_localargs);
					pushppa(this, inqueue, Step 1, am2_qDisable);
					return Continue; // go move into territory
Label2: ; // Step 2
				}
				{
					AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 60);
					return waitorder(am2_ol_Disable, this, pm_task, Step 3, am_localargs);
Label3: ; // Step 3
				}
				{
					AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 61);
					{
							retval = Continue;
							goto LabelRet;
					}
				}
			}
		}
		{
			AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 64);
			if ((VsegGetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(this)), 84, VehSeg*)) == 21 || VsegGetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(this)), 84, VehSeg*)) == 1) && VehGetCurSchedJob(this) == NULL) {
				{
					AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 66);
					if (VsegGetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(this)), 84, VehSeg*)) == 1) {
						{
							AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 68);
							VsegSetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(this)), 84, VehSeg*), 21);
							EntityChanged(0x00000040);
						}
						{
							AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 69);
							ListAppendItem(VehicleList, am2_vlistOHT, this);	// append item to end of list
						}
					}
				}
				{
					AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 72);
					if (ASIclock == ToModelTime(0, UNITSECONDS)) {
						{
							AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 74);
							am2_vi = 1 + 8 * uniform1(am2_stream0, 0.50000000000000000, 0.50000000000000000);
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 75);
							{
								char* pArg1 = "pm.cp_Route_";
								int32 pArg2 = am2_vi;

								char* am_tmp;
								am_tmp = bufsprintf("%s%d", pArg1, pArg2);
								SetString(&am2_vstrTemp, am_tmp);
								EntityChanged(0x01000000);
							}
						}
						{
							AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 76);
							am2_vlocTemp[1] = str2Location(am2_vstrTemp);
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 77);
							veh_dispatch(this, am2_vlocTemp[1], 0, NULL, 0);
						}
					}
					else {
						AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 79);
						if (PthGetColor(ValidPtr(LocGetCurPath(ValidPtr(VehGetCurLoc(this), 40, simloc*)), 43, Path*)) == 1) {
							{
								AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 81);
								am2_k = 0;
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 82);
								while ((am2_k < Size(List, LocationList, am2_vll_ABE))) {
									{
										AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 84);
										am2_k += 1;
										EntityChanged(0x01000000);
									}
									{
										AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 85);
										am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_k, 99999)] = FromModelDistance(LocGetNavDistToLoc(ValidPtr(VehGetCurLoc(this), 40, simloc*), ValidPtr(ListIndexItem(LocationList, am2_vll_ABE, am2_k), 40, simloc*)), UNITMILLIMETERS);
										EntityChanged(0x01000000);
									}
									{
										AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 86);
										am2_vllocation[ValidIndex("am_model.am_vllocation", am2_k, 2200)] = ListIndexItem(LocationList, am2_vll_ABE, am2_k);
										EntityChanged(0x01000000);
									}
									{
										AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 87);
										if (LocCompare(am2_vllocation[ValidIndex("am_model.am_vllocation", am2_k, 2200)], VehGetCurLoc(this)) == 0) {
											AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 88);
											am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_k, 99999)] = 2147483647;
											EntityChanged(0x01000000);
										}
									}
									{
										AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 89);
										am2_vilIndex[ValidIndex("am_model.am_vilIndex", am2_k, 99999)] = am2_k;
										EntityChanged(0x01000000);
									}
								}
							}
						}
						else {
							{
								AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 94);
								am2_k = 0;
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 95);
								while ((am2_k < Size(List, LocationList, am2_vllChargeRoute))) {
									{
										AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 97);
										am2_k += 1;
										EntityChanged(0x01000000);
									}
									{
										AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 98);
										am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_k, 99999)] = FromModelDistance(LocGetNavDistToLoc(ValidPtr(VehGetCurLoc(this), 40, simloc*), ValidPtr(ListIndexItem(LocationList, am2_vllChargeRoute, am2_k), 40, simloc*)), UNITMILLIMETERS);
										EntityChanged(0x01000000);
									}
									{
										AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 99);
										am2_vllocation[ValidIndex("am_model.am_vllocation", am2_k, 2200)] = ListIndexItem(LocationList, am2_vllChargeRoute, am2_k);
										EntityChanged(0x01000000);
									}
									{
										AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 100);
										if (LocCompare(am2_vllocation[ValidIndex("am_model.am_vllocation", am2_k, 2200)], VehGetCurLoc(this)) == 0) {
											AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 101);
											am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_k, 99999)] = 2147483647;
											EntityChanged(0x01000000);
										}
									}
									{
										AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 102);
										am2_vilIndex[ValidIndex("am_model.am_vilIndex", am2_k, 99999)] = am2_k;
										EntityChanged(0x01000000);
									}
								}
							}
						}
					}
				}
				{
					AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 106);
					F_QuickSort(1, am2_k);
				}
				{
					AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 107);
					veh_dispatch(this, am2_vllocation[1], 0, NULL, 0);
				}
			}
			else {
				AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 109);
				if (VsegGetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(this)), 84, VehSeg*)) == 3 && VehGetCurSchedJob(this) == NULL) {
					{
						AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 111);
						{
							char* pArg1 = rel_simlocname(VehGetCurLoc(this), am_model.$sys);

							char* am_tmp;
							am_tmp = bufsprintf("%s", pArg1);
							SetString(&am2_vstrTemp, am_tmp);
							EntityChanged(0x01000000);
						}
					}
					{
						AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 112);
						am2_vi = str2Integer(StrGetSubStr(am2_vstrTemp, 13, 1));
						EntityChanged(0x01000000);
					}
					{
						AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 113);
						if (am2_vi < 8 && am2_vi > 2) {
							{
								AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 115);
								am2_vi += 1;
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 116);
								{
									char* pArg1 = "pm.cp_Route_";
									int32 pArg2 = am2_vi;

									char* am_tmp;
									am_tmp = bufsprintf("%s%d", pArg1, pArg2);
									SetString(&am2_vstrTemp, am_tmp);
									EntityChanged(0x01000000);
								}
							}
							{
								AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 117);
								am2_vlocTemp[1] = str2Location(am2_vstrTemp);
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 118);
								veh_dispatch(this, am2_vlocTemp[1], 0, NULL, 0);
							}
						}
						else {
							AMDebugger("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor, 121);
							veh_dispatch(this, LocGetQualifier(am_model.am_pm.am_cp_Route_3, -9999), 0, NULL, 0);
						}
					}
				}
			}
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("vehicle.m", "Task search procedure", "model.pm", pm_task, localactor);
	return retval;
} /* end of pm_task */

static int32
F_Dijkstra(int32 am_Arg_Start, int32 am_Arg_End, vehicle* am_theVehicle)
{
	load* localactor = NULL;
	AMDebuggerBeginRoutine("vehicle.m", "Function", "model.F_Dijkstra", localactor);
	{
		char*	names[3];
		void*	ptrs[3];
		char*	(*valstrfuncs[3])(void*);
		
		names[0] = "Arg_Start";
		ptrs[0] = &am_Arg_Start;
		valstrfuncs[0] = Integer_valstrfunc;
		names[1] = "Arg_End";
		ptrs[1] = &am_Arg_End;
		valstrfuncs[1] = Integer_valstrfunc;
		names[2] = "theVehicle";
		ptrs[2] = &am_theVehicle;
		valstrfuncs[2] = VehiclePtr_valstrfunc;
		AMDebuggerParams("model.F_Dijkstra", F_Dijkstra, localactor, 3, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 127);
			am2_vi = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 128);
			am2_vj = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 129);
			while (am2_vi < am2_viSize) {
				{
					AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 131);
					am2_vi += 1;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 132);
					am2_vrDist[ValidIndex("am_model.am_vrDist", am2_vi, 2200)] = am2_vrDM[ValidIndex("am_model.am_vrDM", am_Arg_Start, 2200)][ValidIndex("am_model.am_vrDM", am2_vi, 2200)];
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 133);
					am2_vipred[ValidIndex("am_model.am_vipred", am2_vi, 2200)] = am_Arg_Start;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 134);
					am2_viFound[ValidIndex("am_model.am_viFound", am2_vi, 2200)] = 0;
					EntityChanged(0x01000000);
				}
			}
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 137);
			am2_vi = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 138);
			while (am2_vi < am2_viSize) {
				{
					AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 140);
					am2_vi += 1;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 141);
					am2_uu = F_Choose();
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 142);
					am2_viFound[ValidIndex("am_model.am_viFound", am2_uu, 2200)] = 1;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 144);
					while (am2_vj < am2_viSize) {
						{
							AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 146);
							am2_vj += 1;
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 148);
							if (am2_vrDist[ValidIndex("am_model.am_vrDist", am2_uu, 2200)] + am2_vrDM[ValidIndex("am_model.am_vrDM", am2_uu, 2200)][ValidIndex("am_model.am_vrDM", am2_vj, 2200)] < am2_vrDist[ValidIndex("am_model.am_vrDist", am2_vj, 2200)]) {
								{
									AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 150);
									am2_vrDist[ValidIndex("am_model.am_vrDist", am2_vj, 2200)] = am2_vrDist[ValidIndex("am_model.am_vrDist", am2_uu, 2200)] + am2_vrDM[ValidIndex("am_model.am_vrDM", am2_uu, 2200)][ValidIndex("am_model.am_vrDM", am2_vj, 2200)];
									EntityChanged(0x01000000);
								}
								{
									AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 151);
									am2_vipred[ValidIndex("am_model.am_vipred", am2_vj, 2200)] = am2_uu;
									EntityChanged(0x01000000);
								}
							}
						}
					}
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 155);
					am2_vj = 0;
					EntityChanged(0x01000000);
				}
			}
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 160);
			ListCopy(LocationList, am2_vllRoute, NULL);
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 162);
			am2_vi = am_Arg_End;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 170);
			while (am2_vi != am_Arg_Start) {
				{
					AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 172);
					am2_vi = am2_vipred[ValidIndex("am_model.am_vipred", am2_vi, 2200)];
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 173);
					if (LocCompare(ListIndexItem(LocationList, am2_vllDM, am2_vi), VehGetCurLoc(ValidPtr(am_theVehicle, 81, vehicle*))) != 0) {
						AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 174);
						ListAppendItem(LocationList, am2_vllRoute, ListIndexItem(LocationList, am2_vllDM, am2_vi));	// append item to end of list
					}
				}
			}
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 179);
			am2_vi = Size(List, LocationList, am2_vllRoute);
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 180);
			while (am2_vi > 0) {
				{
					AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 182);
					veh_dispatch(am_theVehicle, ListIndexItem(LocationList, am2_vllRoute, am2_vi), 0, NULL, 0);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 183);
					am2_vi -= 1;
					EntityChanged(0x01000000);
				}
			}
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 186);
			if (VehGetColor(ValidPtr(am_theVehicle, 81, vehicle*)) == 21) {
				AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 187);
				veh_dispatch(am_theVehicle, ListIndexItem(LocationList, am2_vllDM, am_Arg_End), 0, NULL, 0);
			}
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor, 190);
			AMDebuggerEndRoutine("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("vehicle.m", "Function", "model.F_Dijkstra", F_Dijkstra, localactor);
} /* end of F_Dijkstra */

static int
dispatch_F_Dijkstra(int nParams, int* argTypes, void** argVals, void** retVal)
{
	static char buf[512];
	int retType;
	int32 arg1;
	int32 arg2;
	vehicle* arg3;
	static int32 ret;

	if (nParams != 3) {
		message("The function F_Dijkstra was called from the ActiveX interface with %d parameters, while 3 are required.", nParams);
		return 0;
	}
	switch (argTypes[0]) {
	case 1:
		arg1 = *(int*)argVals[0];
		break;
	case 2:
		arg1 = *(double*)argVals[0];
		break;
	case 3:
		arg1 = atoi((char*)argVals[0]);
		break;
	default:
		message("Internal Error: Unknown value type for parameter Arg_Start in dispatch function for F_Dijkstra: %d",
			argTypes[0]);
		return 0;
	}
	switch (argTypes[1]) {
	case 1:
		arg2 = *(int*)argVals[1];
		break;
	case 2:
		arg2 = *(double*)argVals[1];
		break;
	case 3:
		arg2 = atoi((char*)argVals[1]);
		break;
	default:
		message("Internal Error: Unknown value type for parameter Arg_End in dispatch function for F_Dijkstra: %d",
			argTypes[1]);
		return 0;
	}
	switch (argTypes[2]) {
	case 1:
		sprintf(buf, "%d", *(int*)argVals[2]);
		break;
	case 2:
		sprintf(buf, "%lg", *(double*)argVals[2]);
		break;
	case 3:
		strcpy(buf, (char*)argVals[2]);
		break;
	default:
		message("Internal Error: Unknown value type in dispatch function: %d param F_DijkstratheVehicle",
			argTypes[2]);
		return 0;
	}
	if (strcmp(buf, "null") == 0)
		arg3 = NULL;
	else
		arg3 = str2VehiclePtr(buf);
	ret = F_Dijkstra(arg1, arg2, arg3);
	*retVal = &ret;
	return 1;
}

static int32
F_Choose()
{
	load* localactor = NULL;
	AMDebuggerBeginRoutine("vehicle.m", "Function", "model.F_Choose", localactor);
	{
		char*	names[1];
		void*	ptrs[1];
		char*	(*valstrfuncs[1])(void*);
		
		AMDebuggerParams("model.F_Choose", F_Choose, localactor, 0, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("vehicle.m", "Function", "model.F_Choose", F_Choose, localactor, 194);
			am2_vi_Ch = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Choose", F_Choose, localactor, 195);
			am2_vrMin = am2_vrBigValue;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Choose", F_Choose, localactor, 197);
			while (am2_vi_Ch < am2_viSize) {
				{
					AMDebugger("vehicle.m", "Function", "model.F_Choose", F_Choose, localactor, 199);
					am2_vi_Ch += 1;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_Choose", F_Choose, localactor, 200);
					if (am2_vrDist[ValidIndex("am_model.am_vrDist", am2_vi_Ch, 2200)] > 0 && am2_vrDist[ValidIndex("am_model.am_vrDist", am2_vi_Ch, 2200)] < am2_vrBigValue && am2_vrDist[ValidIndex("am_model.am_vrDist", am2_vi_Ch, 2200)] < am2_vrMin && am2_viFound[ValidIndex("am_model.am_viFound", am2_vi_Ch, 2200)] == 0) {
						{
							AMDebugger("vehicle.m", "Function", "model.F_Choose", F_Choose, localactor, 202);
							am2_vrMin = am2_vrDist[ValidIndex("am_model.am_vrDist", am2_vi_Ch, 2200)];
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Function", "model.F_Choose", F_Choose, localactor, 203);
							am2_viMin_pos = am2_vi_Ch;
							EntityChanged(0x01000000);
						}
					}
				}
			}
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Choose", F_Choose, localactor, 207);
			AMDebuggerEndRoutine("vehicle.m", "Function", "model.F_Choose", F_Choose, localactor);
			return am2_viMin_pos;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("vehicle.m", "Function", "model.F_Choose", F_Choose, localactor);
} /* end of F_Choose */

static int
dispatch_F_Choose(int nParams, int* argTypes, void** argVals, void** retVal)
{
	static char buf[512];
	int retType;
	static int32 ret;

	if (nParams != 0) {
		message("The function F_Choose was called from the ActiveX interface with %d parameters, while 0 are required.", nParams);
		return 0;
	}
	ret = F_Choose();
	*retVal = &ret;
	return 1;
}

static int32
pm_destdecel(vehicle* am_theVehicle, simloc* am_destLoc)
{
	AMSchedJobListItem* am_lv85; // 'for each' loop variable
	AMSchedJobList* am_ls85 = NULL; // 'for each' list
	AMSchedJobListItem* am_lv86; // 'for each' loop variable
	AMSchedJobList* am_ls86 = NULL; // 'for each' list
	AMSchedJobListItem* am_lv87; // 'for each' loop variable
	AMSchedJobList* am_ls87 = NULL; // 'for each' list
	AMSchedJobListItem* am_lv88; // 'for each' loop variable
	AMSchedJobList* am_ls88 = NULL; // 'for each' list

	load* localactor = (load*)am_theVehicle;
	AMDebuggerBeginRoutine("vehicle.m", "Decelerate to destination function", "model.pm", localactor);
	{
		char*	names[2];
		void*	ptrs[2];
		char*	(*valstrfuncs[2])(void*);
		
		names[0] = "theVehicle";
		ptrs[0] = &am_theVehicle;
		valstrfuncs[0] = VehiclePtr_valstrfunc;
		names[1] = "destLoc";
		ptrs[1] = &am_destLoc;
		valstrfuncs[1] = Location_valstrfunc;
		AMDebuggerParams("model.pm", pm_destdecel, localactor, 2, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 213);
			if (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiRouteChange == 1) {
				AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 214);
				ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiRouteChange = 0;
				EntityChanged(0x00000040);
			}
		}
		{
			AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 216);
			if (VsegGetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(ValidPtr(am_theVehicle, 81, vehicle*))), 84, VehSeg*)) != 21 && StringCompare(JobGetType(ValidPtr(VehGetCurSchedJob(ValidPtr(am_theVehicle, 81, vehicle*)), 58, SchedJob*)), "move") == 0) {
				{
					AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 219);
					am2_i = 0;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 220);
					am_ls85 = 0;
					ListCopy(SchedJobList, am_ls85, VehGetJobList(ValidPtr(am_theVehicle, 81, vehicle*)));
					for (am_lv85 = (am_ls85) ? (am_ls85)->first : NULL; am_lv85; am_lv85 = am_lv85->next) {
						am2_vJob = am_lv85->item;
						{
							{
								AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 222);
								am2_i += 1;
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 223);
								if (am2_i > 1) {
									{
										AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 225);
										if (StringCompare(JobGetType(ValidPtr(am2_vJob, 58, SchedJob*)), "move") == 0) {
											{
												AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 227);
												VehSetCurSchedJob(ValidPtr(am_theVehicle, 81, vehicle*), am2_vJob);
												EntityChanged(0x01000000);
											}
											{
												AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 228);
												am_ls86 = 0;
												ListCopy(SchedJobList, am_ls86, VehGetJobList(ValidPtr(am_theVehicle, 81, vehicle*)));
												for (am_lv86 = (am_ls86) ? (am_ls86)->first : NULL; am_lv86; am_lv86 = am_lv86->next) {
													am2_vJob2 = am_lv86->item;
													{
														{
															AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 230);
															if (LocCompare(JobGetDest(ValidPtr(am2_vJob2, 58, SchedJob*)), am_destLoc) == 0) {
																{
																	AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 232);
																	veh_cancel(am2_vJob2);
																}
																{
																	AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 233);
																	break;
																}
															}
														}
													}
												}
												ListRemoveAllAndFree(SchedJobList, am_ls86); /* End of for each */
											}
											{
												AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 236);
												break;
											}
										}
									}
								}
							}
						}
					}
					ListRemoveAllAndFree(SchedJobList, am_ls85); /* End of for each */
				}
			}
			else {
				AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 241);
				if (LocGetColor(ValidPtr(am_destLoc, 40, simloc*)) == 2) {
					{
						AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 243);
						{
							char* pArg1 = rel_simlocname(am_destLoc, am_model.$sys);

							char* am_tmp;
							am_tmp = bufsprintf("%s", pArg1);
							SetString(&am2_vsTemp[1], am_tmp);
							EntityChanged(0x01000000);
						}
					}
					{
						AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 244);
						am2_vi = str2Integer(StrGetSubStr(am2_vsTemp[1], 13, 1));
						EntityChanged(0x01000000);
					}
					{
						AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 245);
						if (am2_vi != 8) {
							{
								AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 247);
								am2_vi += 1;
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 248);
								{
									char* pArg1 = "pm:cp_Route_";
									int32 pArg2 = am2_vi;

									char* am_tmp;
									am_tmp = bufsprintf("%s%d", pArg1, pArg2);
									SetString(&am2_vsTemp[2], am_tmp);
									EntityChanged(0x01000000);
								}
							}
							{
								AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 249);
								am2_vlocTemp[1] = str2Location(am2_vsTemp[2]);
								EntityChanged(0x01000000);
							}
						}
						else {
							AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 251);
							if (am2_vi == 8) {
								AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 252);
								am2_vlocTemp[1] = str2Location("pm:cp_Route_1");
								EntityChanged(0x01000000);
							}
						}
					}
					{
						AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 254);
						veh_dispatch(am_theVehicle, am2_vlocTemp[1], 0, NULL, 0);
					}
					{
						AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 256);
						am_ls87 = 0;
						ListCopy(SchedJobList, am_ls87, VehGetJobList(ValidPtr(am_theVehicle, 81, vehicle*)));
						for (am_lv87 = (am_ls87) ? (am_ls87)->first : NULL; am_lv87; am_lv87 = am_lv87->next) {
							am2_vJob = am_lv87->item;
							{
								{
									AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 258);
									if (LocCompare(JobGetDest(ValidPtr(am2_vJob, 58, SchedJob*)), am2_vlocTemp[1]) == 0) {
										AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 259);
										VehSetCurSchedJob(ValidPtr(am_theVehicle, 81, vehicle*), am2_vJob);
										EntityChanged(0x01000000);
									}
								}
							}
						}
						ListRemoveAllAndFree(SchedJobList, am_ls87); /* End of for each */
					}
					{
						AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 262);
						am_ls88 = 0;
						ListCopy(SchedJobList, am_ls88, VehGetJobList(ValidPtr(am_theVehicle, 81, vehicle*)));
						for (am_lv88 = (am_ls88) ? (am_ls88)->first : NULL; am_lv88; am_lv88 = am_lv88->next) {
							am2_vJob = am_lv88->item;
							{
								{
									AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 264);
									if (LocCompare(JobGetDest(ValidPtr(am2_vJob, 58, SchedJob*)), am_destLoc) == 0) {
										AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 265);
										veh_cancel(am2_vJob);
									}
								}
							}
						}
						ListRemoveAllAndFree(SchedJobList, am_ls88); /* End of for each */
					}
				}
			}
		}
		{
			AMDebugger("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor, 269);
	ListRemoveAllAndFree(SchedJobList, am_ls85);
	ListRemoveAllAndFree(SchedJobList, am_ls86);
	ListRemoveAllAndFree(SchedJobList, am_ls87);
	ListRemoveAllAndFree(SchedJobList, am_ls88);
			AMDebuggerEndRoutine("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("vehicle.m", "Decelerate to destination function", "model.pm", pm_destdecel, localactor);
} /* end of pm_destdecel */

static int32
pm_pass(vehicle* am_theVehicle, simloc* am_stopLoc)
{
	load* localactor = (load*)am_theVehicle;
	AMDebuggerBeginRoutine("vehicle.m", "Passing station function", "model.pm", localactor);
	{
		char*	names[2];
		void*	ptrs[2];
		char*	(*valstrfuncs[2])(void*);
		
		names[0] = "theVehicle";
		ptrs[0] = &am_theVehicle;
		valstrfuncs[0] = VehiclePtr_valstrfunc;
		names[1] = "stopLoc";
		ptrs[1] = &am_stopLoc;
		valstrfuncs[1] = Location_valstrfunc;
		AMDebuggerParams("model.pm", pm_pass, localactor, 2, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("vehicle.m", "Passing station function", "model.pm", pm_pass, localactor, 359);
			AMDebuggerEndRoutine("vehicle.m", "Passing station function", "model.pm", pm_pass, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("vehicle.m", "Passing station function", "model.pm", pm_pass, localactor);
} /* end of pm_pass */

static int32
pm_pickup(vehicle* this, int32 step, void* args)
{
	struct _localargs {
		AMSchedJobListItem* lv89; // 'for each' loop variable
		AMSchedJobList* ls89; // 'for each' list
	} *am_localargs = (struct _localargs*)args;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("vehicle.m", "Pickup procedure", "model.pm", localactor);
	{
		char*	names[2];
		void*	ptrs[2];
		char*	(*valstrfuncs[2])(void*);
		
		names[0] = "Load";
		ptrs[0] = &Front(List, SchedJobList, &this->jobs)->theload;
		valstrfuncs[0] = LoadPtr_valstrfunc;
		names[1] = "Current";
		ptrs[1] = &this->curlocdata.sloc;
		valstrfuncs[1] = Location_valstrfunc;
		AMDebuggerParams("model.pm", pm_pickup, localactor, 2, names, ptrs, valstrfuncs);
	}
	switch (step) { /* Make the step switcher */
	case Step 1: goto Label1;
	case Step 2: goto Label2;
	case Step 3: goto Label3;
	default: message("Bad step number %ld.", step);
	}
	retval = Error;
	goto LabelRet;
Label1: ;  /* Step1 */
	am_localargs = (struct _localargs*)xcalloc(1, sizeof(struct _localargs));
	{
		{
			AMDebugger("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor, 363);
			am_localargs->ls89 = 0;
			ListCopy(SchedJobList, am_localargs->ls89, VehGetJobList(this));
			for (am_localargs->lv89 = (am_localargs->ls89) ? (am_localargs->ls89)->first : NULL; am_localargs->lv89; am_localargs->lv89 = am_localargs->lv89->next) {
				am2_vJob = am_localargs->lv89->item;
				{
					{
						AMDebugger("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor, 365);
						if (StringCompare(JobGetType(ValidPtr(am2_vJob, 58, SchedJob*)), "move") == 0) {
							AMDebugger("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor, 366);
							veh_cancel(am2_vJob);
						}
					}
				}
			}
			ListRemoveAllAndFree(SchedJobList, am_localargs->ls89); /* End of for each */
		}
		{
			AMDebugger("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor, 370);
			this->load.attribute->am2_aAssign = 2;
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor, 371);
			if (LocGetCapacity(ValidPtr(VehGetCurLoc(this), 40, simloc*)) == 100) {
				AMDebugger("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor, 372);
				if (waitfor(ToModelTime(6, UNITSECONDS), this, pm_pickup, Step 2, am_localargs) == Delayed)
					return Delayed;
Label2: ; // Step 2
			}
			else {
				AMDebugger("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor, 374);
				if (waitfor(ToModelTime(9, UNITSECONDS), this, pm_pickup, Step 3, am_localargs) == Delayed)
					return Delayed;
Label3: ; // Step 3
			}
		}
		{
			AMDebugger("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor, 376);
			this->load.attribute->am2_aSetdown = ValidPtr(JobGetLoad(ValidPtr(VehGetClosestJob(this), 58, SchedJob*)), 32, load*)->attribute->am2_aSetdown;
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor, 377);
			ValidPtr(JobGetLoad(ValidPtr(VehGetClosestJob(this), 58, SchedJob*)), 32, load*)->attribute->am2_atUnload = ASIclock;
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor, 378);
			VsegSetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(this)), 84, VehSeg*), 63);
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor, 379);
			this->load.attribute->am2_aiPathSearched = 0;
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor, 380);
			this->load.attribute->am2_atBattery_Del = ToModelTime(this->load.attribute->am2_atBattery, UNITSECONDS);
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor, 381);
			tabulate(am2_tBatteryChange_Ret, (this->load.attribute->am2_atBattery - FromModelTime(this->load.attribute->am2_atBattery_Ret, UNITSECONDS)));	// Tabulate the value
		}
	}
LabelRet: ;
	ListRemoveAllAndFree(SchedJobList, am_localargs->ls89);
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("vehicle.m", "Pickup procedure", "model.pm", pm_pickup, localactor);
	return retval;
} /* end of pm_pickup */

static int32
pm_setdown(vehicle* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("vehicle.m", "Setdown procedure", "model.pm", localactor);
	{
		char*	names[2];
		void*	ptrs[2];
		char*	(*valstrfuncs[2])(void*);
		
		names[0] = "Load";
		ptrs[0] = &Front(List, SchedJobList, &this->jobs)->theload;
		valstrfuncs[0] = LoadPtr_valstrfunc;
		names[1] = "Current";
		ptrs[1] = &this->curlocdata.sloc;
		valstrfuncs[1] = Location_valstrfunc;
		AMDebuggerParams("model.pm", pm_setdown, localactor, 2, names, ptrs, valstrfuncs);
	}
	switch (step) { /* Make the step switcher */
	case Step 1: goto Label1;
	case Step 2: goto Label2;
	case Step 3: goto Label3;
	case Step 4: goto Label4;
	default: message("Bad step number %ld.", step);
	}
	retval = Error;
	goto LabelRet;
Label1: ;  /* Step1 */
	{
		{
			AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 441);
			this->load.attribute->am2_atcheck = ASIclock;
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 442);
			if (LocGetCapacity(ValidPtr(VehGetCurLoc(this), 40, simloc*)) == 100) {
				AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 443);
				if (waitfor(ToModelTime(6, UNITSECONDS), this, pm_setdown, Step 2, am_localargs) == Delayed)
					return Delayed;
Label2: ; // Step 2
			}
			else {
				AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 445);
				if (waitfor(ToModelTime(9, UNITSECONDS), this, pm_setdown, Step 3, am_localargs) == Delayed)
					return Delayed;
Label3: ; // Step 3
			}
		}
		{
			AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 447);
			this->load.attribute->am2_aAssign = 0;
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 448);
			tabulate(am2_tBatteryChange_Del, (this->load.attribute->am2_atBattery - FromModelTime(this->load.attribute->am2_atBattery_Del, UNITSECONDS)));	// Tabulate the value
		}
		{
			AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 449);
			this->load.attribute->am2_atBattery_Idle = ToModelTime(this->load.attribute->am2_atBattery, UNITSECONDS);
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 451);
			am2_k = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 452);
			while ((am2_k < Size(List, LocationList, am2_vll_ABE))) {
				{
					AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 454);
					am2_k += 1;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 455);
					am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_k, 99999)] = FromModelDistance(LocGetNavDistToLoc(ValidPtr(VehGetCurLoc(this), 40, simloc*), ValidPtr(ListIndexItem(LocationList, am2_vll_ABE, am2_k), 40, simloc*)), UNITMILLIMETERS);
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 456);
					am2_vllocation[ValidIndex("am_model.am_vllocation", am2_k, 2200)] = ListIndexItem(LocationList, am2_vll_ABE, am2_k);
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 457);
					if (LocCompare(am2_vllocation[ValidIndex("am_model.am_vllocation", am2_k, 2200)], VehGetCurLoc(this)) == 0) {
						AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 458);
						am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_k, 99999)] = 99999;
						EntityChanged(0x01000000);
					}
				}
				{
					AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 459);
					am2_vilIndex[ValidIndex("am_model.am_vilIndex", am2_k, 99999)] = am2_k;
					EntityChanged(0x01000000);
				}
			}
		}
		{
			AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 461);
			F_QuickSort(1, am2_k);
		}
		{
			AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 462);
			veh_dispatch(this, am2_vllocation[1], 0, NULL, 0);
		}
		{
			AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 465);
			if ((this->load.attribute->am2_atBattery < 3960 * am2_vrRecharge && StringCompare(VehGetType(this), "DefVehicle") == 0) || (this->load.attribute->am2_atBattery < 1980 && StringCompare(VehGetType(this), "ROHT") == 0)) {
				{
					AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 467);
					VsegSetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(this)), 84, VehSeg*), 3);
					EntityChanged(0x00000040);
				}
				{
					AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 468);
					this->load.attribute->am2_aiRecharge = 1;
					EntityChanged(0x00000040);
				}
				{
					AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 469);
					{
						int result = inccount(am2_cChargingOHT, 1, this, pm_setdown, Step 4, am_localargs);
						if (result != Continue) return result;
Label4: ;	// Step 4
					}
				}
				{
					AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 470);
					{
						char* pArg1 = rel_actorname(this, am_model.$sys);
						char* pArg2 = " ";
						char* pArg3 = "\t";
						char* pArg4 = " ";
						char* pArg5 = " need to charge";

						message("%s%s%s%s%s", pArg1, pArg2, pArg3, pArg4, pArg5);
					}
				}
			}
			else {
				{
					AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 474);
					ListAppendItem(VehicleList, am2_vlistOHT, this);	// append item to end of list
				}
				{
					AMDebugger("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor, 475);
					VsegSetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(this)), 84, VehSeg*), 21);
					EntityChanged(0x00000040);
				}
			}
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("vehicle.m", "Setdown procedure", "model.pm", pm_setdown, localactor);
	return retval;
} /* end of pm_setdown */

static int32
pm_jobselect(vehicle* this, int32 step, void* args)
{
	struct _localargs {
		AMSchedJobListItem* lv90; // 'for each' loop variable
		AMSchedJobList* ls90; // 'for each' list
	} *am_localargs = (struct _localargs*)args;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("vehicle.m", "Job selection procedure", "model.pm", localactor);
	AMDebuggerParams("model.pm", pm_jobselect, localactor, 0, NULL, NULL, NULL);
	am_localargs = (struct _localargs*)xcalloc(1, sizeof(struct _localargs));
	{
		{
			AMDebugger("vehicle.m", "Job selection procedure", "model.pm", pm_jobselect, localactor, 488);
			if (StringCompare(JobGetType(ValidPtr(VehGetCurSchedJob(this), 58, SchedJob*)), "deliver") == 0 || StringCompare(JobGetType(ValidPtr(VehGetCurSchedJob(this), 58, SchedJob*)), "retrieve") == 0) {
				{
					AMDebugger("vehicle.m", "Job selection procedure", "model.pm", pm_jobselect, localactor, 490);
					am_localargs->ls90 = 0;
					ListCopy(SchedJobList, am_localargs->ls90, VehGetJobList(this));
					for (am_localargs->lv90 = (am_localargs->ls90) ? (am_localargs->ls90)->first : NULL; am_localargs->lv90; am_localargs->lv90 = am_localargs->lv90->next) {
						am2_vJob = am_localargs->lv90->item;
						{
							{
								AMDebugger("vehicle.m", "Job selection procedure", "model.pm", pm_jobselect, localactor, 492);
								if (StringCompare(JobGetType(ValidPtr(am2_vJob, 58, SchedJob*)), "move") == 0) {
									{
										AMDebugger("vehicle.m", "Job selection procedure", "model.pm", pm_jobselect, localactor, 494);
										VehSetCurSchedJob(this, am2_vJob);
										EntityChanged(0x00000040);
									}
									{
										AMDebugger("vehicle.m", "Job selection procedure", "model.pm", pm_jobselect, localactor, 495);
										break;
									}
								}
							}
						}
					}
					ListRemoveAllAndFree(SchedJobList, am_localargs->ls90); /* End of for each */
				}
			}
		}
	}
LabelRet: ;
	ListRemoveAllAndFree(SchedJobList, am_localargs->ls90);
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("vehicle.m", "Job selection procedure", "model.pm", pm_jobselect, localactor);
	return retval;
} /* end of pm_jobselect */

static int32
pm_ROHT_jobfinish(vehicle* this, int32 step, void* args)
{
	struct _localargs {
		AMSchedJobListItem* lv91; // 'for each' loop variable
		AMSchedJobList* ls91; // 'for each' list
	} *am_localargs = (struct _localargs*)args;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("vehicle.m", "Job finished procedure", "model.pm.ROHT", localactor);
	AMDebuggerParams("model.pm.ROHT", pm_ROHT_jobfinish, localactor, 0, NULL, NULL, NULL);
	am_localargs = (struct _localargs*)xcalloc(1, sizeof(struct _localargs));
	{
		{
			AMDebugger("vehicle.m", "Job finished procedure", "model.pm.ROHT", pm_ROHT_jobfinish, localactor, 503);
			if (LocGetColor(ValidPtr(VehGetCurLoc(this), 40, simloc*)) == 62) {
				{
					AMDebugger("vehicle.m", "Job finished procedure", "model.pm.ROHT", pm_ROHT_jobfinish, localactor, 505);
					am_localargs->ls91 = 0;
					ListCopy(SchedJobList, am_localargs->ls91, VehGetJobList(this));
					for (am_localargs->lv91 = (am_localargs->ls91) ? (am_localargs->ls91)->first : NULL; am_localargs->lv91; am_localargs->lv91 = am_localargs->lv91->next) {
						am2_vJob = am_localargs->lv91->item;
						{
							{
								AMDebugger("vehicle.m", "Job finished procedure", "model.pm.ROHT", pm_ROHT_jobfinish, localactor, 507);
								veh_cancel(am2_vJob);
							}
						}
					}
					ListRemoveAllAndFree(SchedJobList, am_localargs->ls91); /* End of for each */
				}
				{
					AMDebugger("vehicle.m", "Job finished procedure", "model.pm.ROHT", pm_ROHT_jobfinish, localactor, 509);
					ListAppendItem(VehicleList, am2_vlistROHT, this);	// append item to end of list
				}
			}
		}
	}
LabelRet: ;
	ListRemoveAllAndFree(SchedJobList, am_localargs->ls91);
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("vehicle.m", "Job finished procedure", "model.pm.ROHT", pm_ROHT_jobfinish, localactor);
	return retval;
} /* end of pm_ROHT_jobfinish */


typedef struct {
	double freq;
	int32 value;
} Oneof0;

static Oneof0 List0[] = {
	{ 1, 1},
	{ 2, 2},
	{ 3, 3}
};

static int32
oneofFunc0(load* this)
{
	int ind = 0;
	Oneof0* list = List0;
	double sample = getdrand(am2_stream0) * 3;

	tprintf(tfp, "In oneof\n");
	while (list->freq < sample) {
		ind++;
		list++;
	}
	return List0[ind].value;
}

static int32
pIdleCheck_arriving(load* this, int32 step, void* args)
{
	struct _localargs {
		AMVehicleListItem* lv92; // 'for each' loop variable
		AMVehicleList* ls92; // 'for each' list
	} *am_localargs = (struct _localargs*)args;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("vehicle.m", "Arriving procedure", "model.pIdleCheck", localactor);
	AMDebuggerParams("model.pIdleCheck", pIdleCheck_arriving, localactor, 0, NULL, NULL, NULL);
	switch (step) { /* Make the step switcher */
	case Step 1: goto Label1;
	case Step 2: goto Label2;
	default: message("Bad step number %ld.", step);
	}
	retval = Error;
	goto LabelRet;
Label1: ;  /* Step1 */
	am_localargs = (struct _localargs*)xcalloc(1, sizeof(struct _localargs));
	{
		{
			AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 514);
			while (1 == 1) {
				{
					AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 516);
					if (waitfor(ToModelTime(1, UNITSECONDS), this, pIdleCheck_arriving, Step 2, am_localargs) == Delayed)
						return Delayed;
Label2: ; // Step 2
				}
				{
					AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 517);
					am_localargs->ls92 = 0;
					ListCopy(VehicleList, am_localargs->ls92, am2_vlistOHTall);
					for (am_localargs->lv92 = (am_localargs->ls92) ? (am_localargs->ls92)->first : NULL; am_localargs->lv92; am_localargs->lv92 = am_localargs->lv92->next) {
						am2_vohtTemp = am_localargs->lv92->item;
						{
							{
								AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 519);
								if (StringCompare(VehGetStatus(ValidPtr(am2_vohtTemp, 81, vehicle*)), "Idle") == 0) {
									{
										AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 521);
										if (StringCompare(VehGetType(ValidPtr(am2_vohtTemp, 81, vehicle*)), "DefVehicle") == 0) {
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 523);
												am2_k = 0;
												EntityChanged(0x01000000);
											}
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 524);
												while ((am2_k < Size(List, LocationList, am2_vll_ABE))) {
													{
														AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 526);
														am2_k += 1;
														EntityChanged(0x01000000);
													}
													{
														AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 527);
														if (LocCompare(VehGetCurLoc(ValidPtr(am2_vohtTemp, 81, vehicle*)), NULL) == 0) {
															AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 528);
															break;
														}
														else {
															{
																AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 531);
																am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_k, 99999)] = FromModelDistance(LocGetNavDistToLoc(ValidPtr(VehGetCurLoc(ValidPtr(am2_vohtTemp, 81, vehicle*)), 40, simloc*), ValidPtr(ListIndexItem(LocationList, am2_vll_ABE, am2_k), 40, simloc*)), UNITMILLIMETERS);
																EntityChanged(0x01000000);
															}
															{
																AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 532);
																am2_vllocation[ValidIndex("am_model.am_vllocation", am2_k, 2200)] = ListIndexItem(LocationList, am2_vll_ABE, am2_k);
																EntityChanged(0x01000000);
															}
															{
																AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 533);
																if (LocCompare(am2_vllocation[ValidIndex("am_model.am_vllocation", am2_k, 2200)], VehGetCurLoc(ValidPtr(am2_vohtTemp, 81, vehicle*))) == 0) {
																	AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 534);
																	am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_k, 99999)] = 99999;
																	EntityChanged(0x01000000);
																}
															}
															{
																AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 535);
																am2_vilIndex[ValidIndex("am_model.am_vilIndex", am2_k, 99999)] = am2_k;
																EntityChanged(0x01000000);
															}
														}
													}
												}
											}
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 538);
												ValidPtr(am2_vohtTemp, 81, vehicle*)->load.attribute->am2_aAssign = 4;
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 539);
												F_QuickSort(1, am2_k);
											}
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 541);
												am2_j = oneofFunc0(this);
												EntityChanged(0x01000000);
											}
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 542);
												if (LocCompare(am2_vllocation[ValidIndex("am_model.am_vllocation", am2_j, 2200)], VehGetCurLoc(ValidPtr(am2_vohtTemp, 81, vehicle*))) != 0) {
													AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 543);
													veh_dispatch(am2_vohtTemp, am2_vllocation[ValidIndex("am_model.am_vllocation", am2_j, 2200)], 0, NULL, 0);
												}
												else {
													AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 545);
													veh_dispatch(am2_vohtTemp, am2_vllocation[ValidIndex("am_model.am_vllocation", am2_j + 1, 2200)], 0, NULL, 0);
												}
											}
										}
										else {
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor, 549);
												if ((StringCompare(VehGetStatus(ValidPtr(am2_vohtTemp, 81, vehicle*)), "Idle") == 0 && LocGetColor(ValidPtr(VehGetCurLoc(ValidPtr(am2_vohtTemp, 81, vehicle*)), 40, simloc*)) != 62) || (VehGetCurSchedJob(ValidPtr(am2_vohtTemp, 81, vehicle*)) != NULL && LocGetColor(ValidPtr(JobGetDest(ValidPtr(VehGetCurSchedJob(ValidPtr(am2_vohtTemp, 81, vehicle*)), 58, SchedJob*)), 40, simloc*)) != 62)) {
												}
											}
										}
									}
								}
							}
						}
					}
					ListRemoveAllAndFree(VehicleList, am_localargs->ls92); /* End of for each */
				}
			}
		}
	}
LabelRet: ;
	ListRemoveAllAndFree(VehicleList, am_localargs->ls92);
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("vehicle.m", "Arriving procedure", "model.pIdleCheck", pIdleCheck_arriving, localactor);
	return retval;
} /* end of pIdleCheck_arriving */

static int32
F_QuickSort(int32 am_Arg1, int32 am_Arg2)
{
	load* localactor = NULL;
	AMDebuggerBeginRoutine("vehicle.m", "Function", "model.F_QuickSort", localactor);
	{
		char*	names[2];
		void*	ptrs[2];
		char*	(*valstrfuncs[2])(void*);
		
		names[0] = "Arg1";
		ptrs[0] = &am_Arg1;
		valstrfuncs[0] = Integer_valstrfunc;
		names[1] = "Arg2";
		ptrs[1] = &am_Arg2;
		valstrfuncs[1] = Integer_valstrfunc;
		AMDebuggerParams("model.F_QuickSort", F_QuickSort, localactor, 2, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 567);
			if (am_Arg1 >= am_Arg2) {
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 569);
					AMDebuggerEndRoutine("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor);
					return 1;
				}
			}
			else {
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 573);
					am2_vipivot = am_Arg1;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 574);
					am2_vi = am2_vipivot + 1;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 575);
					am2_vj = am_Arg2;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 577);
					while ((am2_vi <= am2_vj)) {
						{
							AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 579);
							while ((am2_vi <= am_Arg2 && am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_vi, 99999)] <= am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_vipivot, 99999)])) {
								{
									AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 581);
									am2_vi += 1;
									EntityChanged(0x01000000);
								}
							}
						}
						{
							AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 584);
							while ((am2_vj > am_Arg1 && am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_vj, 99999)] >= am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_vipivot, 99999)])) {
								{
									AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 586);
									am2_vj -= 1;
									EntityChanged(0x01000000);
								}
							}
						}
						{
							AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 589);
							if (am2_vi >= am2_vj) {
								AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 590);
								break;
							}
						}
						{
							AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 592);
							am2_vrtemp = am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_vj, 99999)];
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 593);
							am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_vj, 99999)] = am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_vi, 99999)];
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 594);
							am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_vi, 99999)] = am2_vrtemp;
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 596);
							am2_vlocTemp[1] = am2_vllocation[ValidIndex("am_model.am_vllocation", am2_vj, 2200)];
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 597);
							am2_vllocation[ValidIndex("am_model.am_vllocation", am2_vj, 2200)] = am2_vllocation[ValidIndex("am_model.am_vllocation", am2_vi, 2200)];
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 598);
							am2_vllocation[ValidIndex("am_model.am_vllocation", am2_vi, 2200)] = am2_vlocTemp[1];
							EntityChanged(0x01000000);
						}
					}
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 601);
					am2_vrtemp = am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_vj, 99999)];
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 602);
					am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_vj, 99999)] = am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_vipivot, 99999)];
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 603);
					am2_vrlDistance[ValidIndex("am_model.am_vrlDistance", am2_vipivot, 99999)] = am2_vrtemp;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 605);
					am2_vlocTemp[1] = am2_vllocation[ValidIndex("am_model.am_vllocation", am2_vj, 2200)];
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 606);
					am2_vllocation[ValidIndex("am_model.am_vllocation", am2_vj, 2200)] = am2_vllocation[ValidIndex("am_model.am_vllocation", am2_vipivot, 2200)];
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 607);
					am2_vllocation[ValidIndex("am_model.am_vllocation", am2_vipivot, 2200)] = am2_vlocTemp[1];
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 609);
					F_QuickSort(am_Arg1, am2_vj - 1);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 610);
					F_QuickSort(am2_vj + 1, am_Arg2);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor, 612);
					AMDebuggerEndRoutine("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor);
					return 1;
				}
			}
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("vehicle.m", "Function", "model.F_QuickSort", F_QuickSort, localactor);
} /* end of F_QuickSort */

static int
dispatch_F_QuickSort(int nParams, int* argTypes, void** argVals, void** retVal)
{
	static char buf[512];
	int retType;
	int32 arg1;
	int32 arg2;
	static int32 ret;

	if (nParams != 2) {
		message("The function F_QuickSort was called from the ActiveX interface with %d parameters, while 2 are required.", nParams);
		return 0;
	}
	switch (argTypes[0]) {
	case 1:
		arg1 = *(int*)argVals[0];
		break;
	case 2:
		arg1 = *(double*)argVals[0];
		break;
	case 3:
		arg1 = atoi((char*)argVals[0]);
		break;
	default:
		message("Internal Error: Unknown value type for parameter Arg1 in dispatch function for F_QuickSort: %d",
			argTypes[0]);
		return 0;
	}
	switch (argTypes[1]) {
	case 1:
		arg2 = *(int*)argVals[1];
		break;
	case 2:
		arg2 = *(double*)argVals[1];
		break;
	case 3:
		arg2 = atoi((char*)argVals[1]);
		break;
	default:
		message("Internal Error: Unknown value type for parameter Arg2 in dispatch function for F_QuickSort: %d",
			argTypes[1]);
		return 0;
	}
	ret = F_QuickSort(arg1, arg2);
	*retVal = &ret;
	return 1;
}

static int32
pDispatch_arriving(load* this, int32 step, void* args)
{
	struct _localargs {
		AMVehicleListItem* lv93; // 'for each' loop variable
		AMVehicleList* ls93; // 'for each' list
		AMLoadListItem* lv94; // 'for each' loop variable
		AMLoadList* ls94; // 'for each' list
		AMSchedJobListItem* lv95; // 'for each' loop variable
		AMSchedJobList* ls95; // 'for each' list
		AMSchedJobListItem* lv96; // 'for each' loop variable
		AMSchedJobList* ls96; // 'for each' list
	} *am_localargs = (struct _localargs*)args;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("vehicle.m", "Arriving procedure", "model.pDispatch", localactor);
	AMDebuggerParams("model.pDispatch", pDispatch_arriving, localactor, 0, NULL, NULL, NULL);
	switch (step) { /* Make the step switcher */
	case Step 1: goto Label1;
	case Step 2: goto Label2;
	default: message("Bad step number %ld.", step);
	}
	retval = Error;
	goto LabelRet;
Label1: ;  /* Step1 */
	am_localargs = (struct _localargs*)xcalloc(1, sizeof(struct _localargs));
	{
		{
			AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 618);
			while (1 == 1) {
				{
					AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 620);
					if (waitfor(am2_vtSchedule, this, pDispatch_arriving, Step 2, am_localargs) == Delayed)
						return Delayed;
Label2: ; // Step 2
				}
				{
					AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 622);
					while (Size(List, VehicleList, am2_vlistOHT) > 0 && Size(List, LoadList, am2_vlistLoad[1]) > 0) {
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 624);
							am2_vlSelect = NULL;
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 625);
							am2_vvSelect = NULL;
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 626);
							am2_vtSelect = ToModelTime(0, UNITSECONDS);
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 628);
							am_localargs->ls93 = 0;
							ListCopy(VehicleList, am_localargs->ls93, am2_vlistOHT);
							for (am_localargs->lv93 = (am_localargs->ls93) ? (am_localargs->ls93)->first : NULL; am_localargs->lv93; am_localargs->lv93 = am_localargs->lv93->next) {
								am2_vohtTemp = am_localargs->lv93->item;
								{
									{
										AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 630);
										am_localargs->ls94 = 0;
										ListCopy(LoadList, am_localargs->ls94, am2_vlistLoad[1]);
										for (am_localargs->lv94 = (am_localargs->ls94) ? (am_localargs->ls94)->first : NULL; am_localargs->lv94; am_localargs->lv94 = am_localargs->lv94->next) {
											am2_vlTemp = am_localargs->lv94->item;
											{
												{
													AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 633);
													am2_vrDistance[1] = FromModelDistance(VehGetDistToLoc(ValidPtr(am2_vohtTemp, 81, vehicle*), ValidPtr(ValidPtr(am2_vlTemp, 32, load*)->attribute->am2_alocFrom, 40, simloc*)), UNITMILLIMETERS);
													EntityChanged(0x01000000);
												}
												{
													AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 635);
													if (am2_vrDistance[1] < 200000.00000000000) {
														{
															AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 639);
															am2_vtCost = ToModelTime(10000 - FromModelTime(am2_vtPriorityCost, UNITSECONDS) - FromModelTime(((ASIclock - ValidPtr(am2_vlTemp, 32, load*)->attribute->am2_atTR) * am2_vnTimeWeight), UNITSECONDS) + (am2_vrDistance[1] / 1000 / am2_vrNormalVelocity) - F_Sqrt(ValidPtr(am2_vohtTemp, 81, vehicle*)->load.attribute->am2_atBattery / 1.6000000000000001), UNITSECONDS);
															EntityChanged(0x01000000);
														}
														{
															AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 641);
															if (am2_vlSelect == NULL) {
																{
																	AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 643);
																	am2_vlSelect = am2_vlTemp;
																	EntityChanged(0x01000000);
																}
																{
																	AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 644);
																	am2_vvSelect = am2_vohtTemp;
																	EntityChanged(0x01000000);
																}
																{
																	AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 645);
																	am2_vtSelect = am2_vtCost;
																	EntityChanged(0x01000000);
																}
															}
															else {
																AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 648);
																if ((ASIclock - ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_atTR) < am2_vtTimeLimit && (ASIclock - ValidPtr(am2_vlTemp, 32, load*)->attribute->am2_atTR) >= am2_vtTimeLimit) {
																	{
																		AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 650);
																		am2_vlSelect = am2_vlTemp;
																		EntityChanged(0x01000000);
																	}
																	{
																		AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 651);
																		am2_vvSelect = am2_vohtTemp;
																		EntityChanged(0x01000000);
																	}
																	{
																		AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 652);
																		am2_vtSelect = am2_vtCost;
																		EntityChanged(0x01000000);
																	}
																}
																else {
																	AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 655);
																	if ((ASIclock - ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_atTR) < am2_vtTimeLimit && (ASIclock - ValidPtr(am2_vlTemp, 32, load*)->attribute->am2_atTR) < am2_vtTimeLimit) {
																		{
																			AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 657);
																			if (am2_vtCost < am2_vtSelect) {
																				{
																					AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 659);
																					am2_vlSelect = am2_vlTemp;
																					EntityChanged(0x01000000);
																				}
																				{
																					AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 660);
																					am2_vvSelect = am2_vohtTemp;
																					EntityChanged(0x01000000);
																				}
																				{
																					AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 661);
																					am2_vtSelect = am2_vtCost;
																					EntityChanged(0x01000000);
																				}
																			}
																		}
																	}
																	else {
																		AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 665);
																		if ((ASIclock - ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_atTR) >= am2_vtTimeLimit && (ASIclock - ValidPtr(am2_vlTemp, 32, load*)->attribute->am2_atTR) >= am2_vtTimeLimit) {
																			{
																				AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 667);
																				if (am2_vtCost < am2_vtSelect) {
																					{
																						AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 669);
																						am2_vlSelect = am2_vlTemp;
																						EntityChanged(0x01000000);
																					}
																					{
																						AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 670);
																						am2_vvSelect = am2_vohtTemp;
																						EntityChanged(0x01000000);
																					}
																					{
																						AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 671);
																						am2_vtSelect = am2_vtCost;
																						EntityChanged(0x01000000);
																					}
																				}
																			}
																		}
																	}
																}
															}
														}
													}
												}
											}
										}
										ListRemoveAllAndFree(LoadList, am_localargs->ls94); /* End of for each */
									}
								}
							}
							ListRemoveAllAndFree(VehicleList, am_localargs->ls93); /* End of for each */
						}
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 678);
							if (am2_vlSelect != NULL) {
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 680);
									ClaimLoad(am2_vvSelect, am2_vlSelect, FALSE);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 682);
									am_localargs->ls95 = 0;
									ListCopy(SchedJobList, am_localargs->ls95, VehGetJobList(ValidPtr(am2_vvSelect, 81, vehicle*)));
									for (am_localargs->lv95 = (am_localargs->ls95) ? (am_localargs->ls95)->first : NULL; am_localargs->lv95; am_localargs->lv95 = am_localargs->lv95->next) {
										am2_vJob = am_localargs->lv95->item;
										{
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 684);
												if (StringCompare(JobGetType(ValidPtr(am2_vJob, 58, SchedJob*)), "retrieve") == 0) {
													AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 685);
													VehSetCurSchedJob(ValidPtr(am2_vvSelect, 81, vehicle*), am2_vJob);
													EntityChanged(0x01000000);
												}
											}
										}
									}
									ListRemoveAllAndFree(SchedJobList, am_localargs->ls95); /* End of for each */
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 688);
									am_localargs->ls96 = 0;
									ListCopy(SchedJobList, am_localargs->ls96, VehGetJobList(ValidPtr(am2_vvSelect, 81, vehicle*)));
									for (am_localargs->lv96 = (am_localargs->ls96) ? (am_localargs->ls96)->first : NULL; am_localargs->lv96; am_localargs->lv96 = am_localargs->lv96->next) {
										am2_vJob = am_localargs->lv96->item;
										{
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 690);
												if (StringCompare(JobGetType(ValidPtr(am2_vJob, 58, SchedJob*)), "move") == 0) {
													AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 691);
													veh_cancel(am2_vJob);
												}
											}
										}
									}
									ListRemoveAllAndFree(SchedJobList, am_localargs->ls96); /* End of for each */
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 694);
									ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_atAssign = ASIclock;
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 695);
									ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_atAssignInit = ASIclock;
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 697);
									ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_aAssign = 1;
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 698);
									VsegSetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(ValidPtr(am2_vvSelect, 81, vehicle*))), 84, VehSeg*), 34);
									EntityChanged(0x01000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 699);
									ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_aRetDistance = VehGetTotDistA(ValidPtr(am2_vvSelect, 81, vehicle*));
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 700);
									ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_atBattery_Ret = ToModelTime(ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_atBattery, UNITSECONDS);
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 701);
									tabulate(am2_tBatteryChange_Idle, ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_atBattery - FromModelTime(ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_atBattery_Idle, UNITSECONDS));	// Tabulate the value
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 703);
									ListRemoveFirstMatch(VehicleList, am2_vlistOHT, am2_vvSelect);	// remove first match from list
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 704);
									ListRemoveFirstMatch(LoadList, am2_vlistLoad[1], am2_vlSelect);	// remove first match from list
								}
							}
							else {
								AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor, 710);
								break;
							}
						}
					}
				}
			}
		}
	}
LabelRet: ;
	ListRemoveAllAndFree(VehicleList, am_localargs->ls93);
	ListRemoveAllAndFree(LoadList, am_localargs->ls94);
	ListRemoveAllAndFree(SchedJobList, am_localargs->ls95);
	ListRemoveAllAndFree(SchedJobList, am_localargs->ls96);
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("vehicle.m", "Arriving procedure", "model.pDispatch", pDispatch_arriving, localactor);
	return retval;
} /* end of pDispatch_arriving */

static double
F_Sqrt(double am_input)
{
	load* localactor = NULL;
	AMDebuggerBeginRoutine("vehicle.m", "Function", "model.F_Sqrt", localactor);
	{
		char*	names[1];
		void*	ptrs[1];
		char*	(*valstrfuncs[1])(void*);
		
		names[0] = "input";
		ptrs[0] = &am_input;
		valstrfuncs[0] = Real_valstrfunc;
		AMDebuggerParams("model.F_Sqrt", F_Sqrt, localactor, 1, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("vehicle.m", "Function", "model.F_Sqrt", F_Sqrt, localactor, 717);
			am2_xr = am_input;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Sqrt", F_Sqrt, localactor, 718);
			am2_yr = 1;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Sqrt", F_Sqrt, localactor, 719);
			am2_er = 0.0010000000000000000;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Sqrt", F_Sqrt, localactor, 721);
			while (((am2_xr - am2_yr) > am2_er)) {
				{
					AMDebugger("vehicle.m", "Function", "model.F_Sqrt", F_Sqrt, localactor, 723);
					am2_xr = (am2_xr + am2_yr) / 2;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("vehicle.m", "Function", "model.F_Sqrt", F_Sqrt, localactor, 724);
					am2_yr = am_input / am2_xr;
					EntityChanged(0x01000000);
				}
			}
		}
		{
			AMDebugger("vehicle.m", "Function", "model.F_Sqrt", F_Sqrt, localactor, 727);
			AMDebuggerEndRoutine("vehicle.m", "Function", "model.F_Sqrt", F_Sqrt, localactor);
			return am2_xr;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("vehicle.m", "Function", "model.F_Sqrt", F_Sqrt, localactor);
} /* end of F_Sqrt */

static int
dispatch_F_Sqrt(int nParams, int* argTypes, void** argVals, void** retVal)
{
	static char buf[512];
	int retType;
	double arg1;
	static double ret;

	if (nParams != 1) {
		message("The function F_Sqrt was called from the ActiveX interface with %d parameters, while 1 are required.", nParams);
		return 0;
	}
	switch (argTypes[0]) {
	case 1:
		arg1 = *(int*)argVals[0];
		break;
	case 2:
		arg1 = *(double*)argVals[0];
		break;
	case 3:
		arg1 = atof((char*)argVals[0]);
		break;
	default:
		message("Internal Error: Unknown value type in dispatch function: %d param F_Sqrtinput",
			argTypes[0]);
		return 0;
	}
	ret = F_Sqrt(arg1);
	*retVal = &ret;
	return 2;
}

static int32
pReAssign_arriving(load* this, int32 step, void* args)
{
	struct _localargs {
		AMLoadListItem* lv97; // 'for each' loop variable
		AMLoadList* ls97; // 'for each' list
		AMVehicleListItem* lv98; // 'for each' loop variable
		AMVehicleList* ls98; // 'for each' list
		AMSchedJobListItem* lv99; // 'for each' loop variable
		AMSchedJobList* ls99; // 'for each' list
		AMSchedJobListItem* lv100; // 'for each' loop variable
		AMSchedJobList* ls100; // 'for each' list
		AMSchedJobListItem* lv101; // 'for each' loop variable
		AMSchedJobList* ls101; // 'for each' list
		AMSchedJobListItem* lv102; // 'for each' loop variable
		AMSchedJobList* ls102; // 'for each' list
	} *am_localargs = (struct _localargs*)args;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("vehicle.m", "Arriving procedure", "model.pReAssign", localactor);
	AMDebuggerParams("model.pReAssign", pReAssign_arriving, localactor, 0, NULL, NULL, NULL);
	switch (step) { /* Make the step switcher */
	case Step 1: goto Label1;
	case Step 2: goto Label2;
	default: message("Bad step number %ld.", step);
	}
	retval = Error;
	goto LabelRet;
Label1: ;  /* Step1 */
	am_localargs = (struct _localargs*)xcalloc(1, sizeof(struct _localargs));
	{
		{
			AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 732);
			while (1 == 1) {
				{
					AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 734);
					if (waitfor(am2_vtSchedule, this, pReAssign_arriving, Step 2, am_localargs) == Delayed)
						return Delayed;
Label2: ; // Step 2
				}
				{
					AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 736);
					while (Size(List, VehicleList, am2_vlistOHT) > 0 && Size(List, LoadList, am2_vlistLoad[2]) > 0) {
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 738);
							am2_vlSelect = NULL;
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 739);
							am2_vvSelect = NULL;
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 740);
							am2_vtSelect = ToModelTime(0, UNITSECONDS);
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 742);
							am_localargs->ls97 = 0;
							ListCopy(LoadList, am_localargs->ls97, am2_vlistLoad[2]);
							for (am_localargs->lv97 = (am_localargs->ls97) ? (am_localargs->ls97)->first : NULL; am_localargs->lv97; am_localargs->lv97 = am_localargs->lv97->next) {
								am2_vlTemp = am_localargs->lv97->item;
								{
									{
										AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 744);
										am2_viCheck = 1;
										EntityChanged(0x01000000);
									}
									{
										AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 745);
										am_localargs->ls98 = 0;
										ListCopy(VehicleList, am_localargs->ls98, am2_vlistOHT);
										for (am_localargs->lv98 = (am_localargs->ls98) ? (am_localargs->ls98)->first : NULL; am_localargs->lv98; am_localargs->lv98 = am_localargs->lv98->next) {
											am2_vohtTemp = am_localargs->lv98->item;
											{
												{
													{
														AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 748);
														am2_vrDistance[1] = FromModelDistance(VehGetDistToLoc(ValidPtr(am2_vohtTemp, 81, vehicle*), ValidPtr(ValidPtr(am2_vlTemp, 32, load*)->attribute->am2_alocFrom, 40, simloc*)), UNITMILLIMETERS);
														EntityChanged(0x01000000);
													}
													{
														AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 749);
														am2_vrDistance[2] = FromModelDistance(VehGetDistToLoc(ValidPtr(ValidPtr(am2_vlTemp, 32, load*)->attribute->am2_avDispatch, 81, vehicle*), ValidPtr(ValidPtr(am2_vlTemp, 32, load*)->attribute->am2_alocFrom, 40, simloc*)), UNITMILLIMETERS);
														EntityChanged(0x01000000);
													}
												}
												{
													AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 752);
													if (am2_vrDistance[1] < am2_vrDistance[2]) {
														{
															AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 754);
															if (am2_viCheck == 1) {
																{
																	AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 756);
																	am2_vlSelect = am2_vlTemp;
																	EntityChanged(0x01000000);
																}
																{
																	AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 757);
																	am2_vvSelect = am2_vohtTemp;
																	EntityChanged(0x01000000);
																}
																{
																	AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 758);
																	am2_vrDistanceTemp = am2_vrDistance[1];
																	EntityChanged(0x01000000);
																}
																{
																	AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 759);
																	am2_viCheck += 1;
																	EntityChanged(0x01000000);
																}
															}
															else {
																{
																	AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 764);
																	if (am2_vrDistance[1] < am2_vrDistanceTemp) {
																		{
																			AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 766);
																			am2_vlSelect = am2_vlTemp;
																			EntityChanged(0x01000000);
																		}
																		{
																			AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 767);
																			am2_vvSelect = am2_vohtTemp;
																			EntityChanged(0x01000000);
																		}
																		{
																			AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 768);
																			am2_vrDistanceTemp = am2_vrDistance[1];
																			EntityChanged(0x01000000);
																		}
																	}
																}
															}
														}
													}
												}
											}
										}
										ListRemoveAllAndFree(VehicleList, am_localargs->ls98); /* End of for each */
									}
								}
							}
							ListRemoveAllAndFree(LoadList, am_localargs->ls97); /* End of for each */
						}
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 775);
							if (am2_vlSelect != NULL && ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_avDispatch != am2_vvSelect) {
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 780);
									am2_k = 1 + Size(List, LocationList, am2_vlocParkList) * uniform1(am2_stream0, 0.50000000000000000, 0.50000000000000000);
									EntityChanged(0x01000000);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 781);
									veh_dispatch(ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_avDispatch, ListIndexItem(LocationList, am2_vlocParkList, am2_k), 0, NULL, 0);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 784);
									am_localargs->ls99 = 0;
									ListCopy(SchedJobList, am_localargs->ls99, VehGetJobList(ValidPtr(ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_avDispatch, 81, vehicle*)));
									for (am_localargs->lv99 = (am_localargs->ls99) ? (am_localargs->ls99)->first : NULL; am_localargs->lv99; am_localargs->lv99 = am_localargs->lv99->next) {
										am2_vJob = am_localargs->lv99->item;
										{
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 786);
												if (StringCompare(JobGetType(ValidPtr(am2_vJob, 58, SchedJob*)), "move") == 0) {
													AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 787);
													VehSetCurSchedJob(ValidPtr(ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_avDispatch, 81, vehicle*), am2_vJob);
													EntityChanged(0x01000000);
												}
											}
										}
									}
									ListRemoveAllAndFree(SchedJobList, am_localargs->ls99); /* End of for each */
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 791);
									am_localargs->ls100 = 0;
									ListCopy(SchedJobList, am_localargs->ls100, VehGetJobList(ValidPtr(ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_avDispatch, 81, vehicle*)));
									for (am_localargs->lv100 = (am_localargs->ls100) ? (am_localargs->ls100)->first : NULL; am_localargs->lv100; am_localargs->lv100 = am_localargs->lv100->next) {
										am2_vJob = am_localargs->lv100->item;
										{
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 793);
												if (StringCompare(JobGetType(ValidPtr(am2_vJob, 58, SchedJob*)), "retrieve") == 0) {
													AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 794);
													veh_cancel(am2_vJob);
												}
											}
										}
									}
									ListRemoveAllAndFree(SchedJobList, am_localargs->ls100); /* End of for each */
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 797);
									ListAppendItem(VehicleList, am2_vlistOHT, ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_avDispatch);	// append item to end of list
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 799);
									VsegSetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(ValidPtr(ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_avDispatch, 81, vehicle*))), 84, VehSeg*), 21);
									EntityChanged(0x01000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 800);
									ValidPtr(ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_avDispatch, 81, vehicle*)->load.attribute->am2_aAssign = 0;
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 802);
									ClaimLoad(am2_vvSelect, am2_vlSelect, FALSE);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 804);
									am_localargs->ls101 = 0;
									ListCopy(SchedJobList, am_localargs->ls101, VehGetJobList(ValidPtr(am2_vvSelect, 81, vehicle*)));
									for (am_localargs->lv101 = (am_localargs->ls101) ? (am_localargs->ls101)->first : NULL; am_localargs->lv101; am_localargs->lv101 = am_localargs->lv101->next) {
										am2_vJob = am_localargs->lv101->item;
										{
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 806);
												if (StringCompare(JobGetType(ValidPtr(am2_vJob, 58, SchedJob*)), "retrieve") == 0) {
													AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 807);
													VehSetCurSchedJob(ValidPtr(am2_vvSelect, 81, vehicle*), am2_vJob);
													EntityChanged(0x01000000);
												}
											}
										}
									}
									ListRemoveAllAndFree(SchedJobList, am_localargs->ls101); /* End of for each */
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 810);
									am_localargs->ls102 = 0;
									ListCopy(SchedJobList, am_localargs->ls102, VehGetJobList(ValidPtr(am2_vvSelect, 81, vehicle*)));
									for (am_localargs->lv102 = (am_localargs->ls102) ? (am_localargs->ls102)->first : NULL; am_localargs->lv102; am_localargs->lv102 = am_localargs->lv102->next) {
										am2_vJob = am_localargs->lv102->item;
										{
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 812);
												if (StringCompare(JobGetType(ValidPtr(am2_vJob, 58, SchedJob*)), "move") == 0) {
													AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 813);
													veh_cancel(am2_vJob);
												}
											}
										}
									}
									ListRemoveAllAndFree(SchedJobList, am_localargs->ls102); /* End of for each */
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 816);
									ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_atAssign = ASIclock;
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 818);
									ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_aAssign = 1;
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 819);
									VsegSetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(ValidPtr(am2_vvSelect, 81, vehicle*))), 84, VehSeg*), 34);
									EntityChanged(0x01000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 820);
									ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_aRetDistance = VehGetTotDistA(ValidPtr(am2_vvSelect, 81, vehicle*));
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 822);
									ListRemoveFirstMatch(VehicleList, am2_vlistOHT, am2_vvSelect);	// remove first match from list
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 823);
									ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_avDispatch = am2_vvSelect;
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 824);
									am2_vrDistanceTemp = 0;
									EntityChanged(0x01000000);
								}
							}
							else {
								AMDebugger("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor, 827);
								break;
							}
						}
					}
				}
			}
		}
	}
LabelRet: ;
	ListRemoveAllAndFree(LoadList, am_localargs->ls97);
	ListRemoveAllAndFree(VehicleList, am_localargs->ls98);
	ListRemoveAllAndFree(SchedJobList, am_localargs->ls99);
	ListRemoveAllAndFree(SchedJobList, am_localargs->ls100);
	ListRemoveAllAndFree(SchedJobList, am_localargs->ls101);
	ListRemoveAllAndFree(SchedJobList, am_localargs->ls102);
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("vehicle.m", "Arriving procedure", "model.pReAssign", pReAssign_arriving, localactor);
	return retval;
} /* end of pReAssign_arriving */

static int32
pm_work(vehicle* am_theVehicle, simloc* am_loadLoc, load* am_theLoad)
{
	load* localactor = (load*)am_theVehicle;
	AMDebuggerBeginRoutine("vehicle.m", "Work OK function", "model.pm", localactor);
	{
		char*	names[3];
		void*	ptrs[3];
		char*	(*valstrfuncs[3])(void*);
		
		names[0] = "theVehicle";
		ptrs[0] = &am_theVehicle;
		valstrfuncs[0] = VehiclePtr_valstrfunc;
		names[1] = "loadLoc";
		ptrs[1] = &am_loadLoc;
		valstrfuncs[1] = Location_valstrfunc;
		names[2] = "theLoad";
		ptrs[2] = &am_theLoad;
		valstrfuncs[2] = LoadPtr_valstrfunc;
		AMDebuggerParams("model.pm", pm_work, localactor, 3, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("vehicle.m", "Work OK function", "model.pm", pm_work, localactor, 834);
			AMDebuggerEndRoutine("vehicle.m", "Work OK function", "model.pm", pm_work, localactor);
			return 0;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("vehicle.m", "Work OK function", "model.pm", pm_work, localactor);
} /* end of pm_work */

static int32
pm_resumemove(vehicle* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("vehicle.m", "Resume moving procedure", "model.pm", localactor);
	AMDebuggerParams("model.pm", pm_resumemove, localactor, 0, NULL, NULL, NULL);
	switch (step) { /* Make the step switcher */
	case Step 1: goto Label1;
	case Step 2: goto Label2;
	default: message("Bad step number %ld.", step);
	}
	retval = Error;
	goto LabelRet;
Label1: ;  /* Step1 */
	{
		{
			AMDebugger("vehicle.m", "Resume moving procedure", "model.pm", pm_resumemove, localactor, 838);
			if (waitfor(am2_vtResume, this, pm_resumemove, Step 2, am_localargs) == Delayed)
				return Delayed;
Label2: ; // Step 2
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("vehicle.m", "Resume moving procedure", "model.pm", pm_resumemove, localactor);
	return retval;
} /* end of pm_resumemove */

static int32
pDispatchR_arriving(load* this, int32 step, void* args)
{
	struct _localargs {
		AMVehicleListItem* lv103; // 'for each' loop variable
		AMVehicleList* ls103; // 'for each' list
		AMLoadListItem* lv104; // 'for each' loop variable
		AMLoadList* ls104; // 'for each' list
		AMSchedJobListItem* lv105; // 'for each' loop variable
		AMSchedJobList* ls105; // 'for each' list
		AMSchedJobListItem* lv106; // 'for each' loop variable
		AMSchedJobList* ls106; // 'for each' list
	} *am_localargs = (struct _localargs*)args;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("vehicle.m", "Arriving procedure", "model.pDispatchR", localactor);
	AMDebuggerParams("model.pDispatchR", pDispatchR_arriving, localactor, 0, NULL, NULL, NULL);
	switch (step) { /* Make the step switcher */
	case Step 1: goto Label1;
	case Step 2: goto Label2;
	default: message("Bad step number %ld.", step);
	}
	retval = Error;
	goto LabelRet;
Label1: ;  /* Step1 */
	am_localargs = (struct _localargs*)xcalloc(1, sizeof(struct _localargs));
	{
		{
			AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 843);
			while (1 == 1) {
				{
					AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 845);
					if (waitfor(am2_vtSchedule, this, pDispatchR_arriving, Step 2, am_localargs) == Delayed)
						return Delayed;
Label2: ; // Step 2
				}
				{
					AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 847);
					while (Size(List, VehicleList, am2_vlistROHT) > 0 && Size(List, LoadList, am2_vlistLoad[2]) > 0) {
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 849);
							am2_vlSelect = NULL;
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 850);
							am2_vvSelect = NULL;
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 851);
							am2_vtSelect = ToModelTime(0, UNITSECONDS);
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 853);
							am_localargs->ls103 = 0;
							ListCopy(VehicleList, am_localargs->ls103, am2_vlistROHT);
							for (am_localargs->lv103 = (am_localargs->ls103) ? (am_localargs->ls103)->first : NULL; am_localargs->lv103; am_localargs->lv103 = am_localargs->lv103->next) {
								am2_vohtTemp = am_localargs->lv103->item;
								{
									{
										AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 855);
										am_localargs->ls104 = 0;
										ListCopy(LoadList, am_localargs->ls104, am2_vlistLoad[2]);
										for (am_localargs->lv104 = (am_localargs->ls104) ? (am_localargs->ls104)->first : NULL; am_localargs->lv104; am_localargs->lv104 = am_localargs->lv104->next) {
											am2_vlTemp = am_localargs->lv104->item;
											{
												{
													AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 858);
													am2_vrDistance[1] = FromModelDistance(VehGetDistToLoc(ValidPtr(am2_vohtTemp, 81, vehicle*), ValidPtr(ValidPtr(am2_vlTemp, 32, load*)->attribute->am2_alocFrom, 40, simloc*)), UNITMILLIMETERS);
													EntityChanged(0x01000000);
												}
												{
													AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 860);
													am2_vtCost = ToModelTime(3000 - FromModelTime(am2_vtPriorityCost, UNITSECONDS) - FromModelTime(((ASIclock - ValidPtr(am2_vlTemp, 32, load*)->attribute->am2_atTR) * am2_vnTimeWeight), UNITSECONDS) + (am2_vrDistance[1] / 1000 / am2_vrNormalVelocity), UNITSECONDS);
													EntityChanged(0x01000000);
												}
												{
													AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 862);
													if (am2_vlSelect == NULL) {
														{
															AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 864);
															am2_vlSelect = am2_vlTemp;
															EntityChanged(0x01000000);
														}
														{
															AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 865);
															am2_vvSelect = am2_vohtTemp;
															EntityChanged(0x01000000);
														}
														{
															AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 866);
															am2_vtSelect = am2_vtCost;
															EntityChanged(0x01000000);
														}
													}
													else {
														AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 869);
														if ((ASIclock - ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_atTR) < am2_vtTimeLimit && (ASIclock - ValidPtr(am2_vlTemp, 32, load*)->attribute->am2_atTR) >= am2_vtTimeLimit) {
															{
																AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 871);
																am2_vlSelect = am2_vlTemp;
																EntityChanged(0x01000000);
															}
															{
																AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 872);
																am2_vvSelect = am2_vohtTemp;
																EntityChanged(0x01000000);
															}
															{
																AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 873);
																am2_vtSelect = am2_vtCost;
																EntityChanged(0x01000000);
															}
														}
														else {
															AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 876);
															if ((ASIclock - ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_atTR) < am2_vtTimeLimit && (ASIclock - ValidPtr(am2_vlTemp, 32, load*)->attribute->am2_atTR) < am2_vtTimeLimit) {
																{
																	AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 878);
																	if (am2_vtCost < am2_vtSelect) {
																		{
																			AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 880);
																			am2_vlSelect = am2_vlTemp;
																			EntityChanged(0x01000000);
																		}
																		{
																			AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 881);
																			am2_vvSelect = am2_vohtTemp;
																			EntityChanged(0x01000000);
																		}
																		{
																			AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 882);
																			am2_vtSelect = am2_vtCost;
																			EntityChanged(0x01000000);
																		}
																	}
																}
															}
															else {
																AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 886);
																if ((ASIclock - ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_atTR) >= am2_vtTimeLimit && (ASIclock - ValidPtr(am2_vlTemp, 32, load*)->attribute->am2_atTR) >= am2_vtTimeLimit) {
																	{
																		AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 888);
																		if (am2_vtCost < am2_vtSelect) {
																			{
																				AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 890);
																				am2_vlSelect = am2_vlTemp;
																				EntityChanged(0x01000000);
																			}
																			{
																				AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 891);
																				am2_vvSelect = am2_vohtTemp;
																				EntityChanged(0x01000000);
																			}
																			{
																				AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 892);
																				am2_vtSelect = am2_vtCost;
																				EntityChanged(0x01000000);
																			}
																		}
																	}
																}
															}
														}
													}
												}
											}
										}
										ListRemoveAllAndFree(LoadList, am_localargs->ls104); /* End of for each */
									}
								}
							}
							ListRemoveAllAndFree(VehicleList, am_localargs->ls103); /* End of for each */
						}
						{
							AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 898);
							if (am2_vlSelect != NULL) {
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 900);
									ClaimLoad(am2_vvSelect, am2_vlSelect, FALSE);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 902);
									am_localargs->ls105 = 0;
									ListCopy(SchedJobList, am_localargs->ls105, VehGetJobList(ValidPtr(am2_vvSelect, 81, vehicle*)));
									for (am_localargs->lv105 = (am_localargs->ls105) ? (am_localargs->ls105)->first : NULL; am_localargs->lv105; am_localargs->lv105 = am_localargs->lv105->next) {
										am2_vJob = am_localargs->lv105->item;
										{
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 904);
												if (StringCompare(JobGetType(ValidPtr(am2_vJob, 58, SchedJob*)), "retrieve") == 0) {
													AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 905);
													VehSetCurSchedJob(ValidPtr(am2_vvSelect, 81, vehicle*), am2_vJob);
													EntityChanged(0x01000000);
												}
											}
										}
									}
									ListRemoveAllAndFree(SchedJobList, am_localargs->ls105); /* End of for each */
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 908);
									am_localargs->ls106 = 0;
									ListCopy(SchedJobList, am_localargs->ls106, VehGetJobList(ValidPtr(am2_vvSelect, 81, vehicle*)));
									for (am_localargs->lv106 = (am_localargs->ls106) ? (am_localargs->ls106)->first : NULL; am_localargs->lv106; am_localargs->lv106 = am_localargs->lv106->next) {
										am2_vJob = am_localargs->lv106->item;
										{
											{
												AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 910);
												if (StringCompare(JobGetType(ValidPtr(am2_vJob, 58, SchedJob*)), "move") == 0) {
													AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 911);
													veh_cancel(am2_vJob);
												}
											}
										}
									}
									ListRemoveAllAndFree(SchedJobList, am_localargs->ls106); /* End of for each */
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 914);
									ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_atAssign = ASIclock;
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 915);
									ValidPtr(am2_vlSelect, 32, load*)->attribute->am2_atAssignInit = ASIclock;
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 917);
									ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_aAssign = 1;
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 918);
									VsegSetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(ValidPtr(am2_vvSelect, 81, vehicle*))), 84, VehSeg*), 34);
									EntityChanged(0x01000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 919);
									ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_aRetDistance = VehGetTotDistA(ValidPtr(am2_vvSelect, 81, vehicle*));
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 920);
									ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_atBattery_Ret = ToModelTime(ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_atBattery, UNITSECONDS);
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 921);
									tabulate(am2_tBatteryChange_Idle, ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_atBattery - FromModelTime(ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_atBattery_Idle, UNITSECONDS));	// Tabulate the value
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 923);
									{
										if (isFileValid(am2_vfpOutResult[8], 0)) {
											double pArg1 = FromModelTime(ASIclock, UNITSECONDS);
											char* pArg2 = " ";
											char* pArg3 = "\t";
											char* pArg4 = " ";
											char* pArg5 = "JobAssigned";
											char* pArg6 = " ";
											char* pArg7 = "\t";
											char* pArg8 = " ";
											char* pArg9 = rel_actorname(am2_vvSelect, am_model.$sys);
											char* pArg10 = " ";
											char* pArg11 = "\t";
											char* pArg12 = " ";
											double pArg13 = ValidPtr(am2_vvSelect, 81, vehicle*)->load.attribute->am2_atBattery;

											fprintf((am2_vfpOutResult[8])->fp, "%lf%s%s%s%s%s%s%s%s%s%s%s%lf\n", pArg1, pArg2, pArg3, pArg4, pArg5, pArg6, pArg7, pArg8, pArg9, pArg10, pArg11, pArg12, pArg13);
											fflush((am2_vfpOutResult[8])->fp);
										}
									}
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 925);
									ListRemoveFirstMatch(VehicleList, am2_vlistROHT, am2_vvSelect);	// remove first match from list
								}
								{
									AMDebugger("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor, 926);
									ListRemoveFirstMatch(LoadList, am2_vlistLoad[2], am2_vlSelect);	// remove first match from list
								}
							}
						}
					}
				}
			}
		}
	}
LabelRet: ;
	ListRemoveAllAndFree(VehicleList, am_localargs->ls103);
	ListRemoveAllAndFree(LoadList, am_localargs->ls104);
	ListRemoveAllAndFree(SchedJobList, am_localargs->ls105);
	ListRemoveAllAndFree(SchedJobList, am_localargs->ls106);
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("vehicle.m", "Arriving procedure", "model.pDispatchR", pDispatchR_arriving, localactor);
	return retval;
} /* end of pDispatchR_arriving */



/* init function for vehicle.m */
void
model_vehicle_init(struct model_struct* data)
{
	((MovementSystem*)data->am_pm.$sys)->srcblock.initprc = pm_vehinit;
	((MovementSystem*)data->am_pm.$sys)->srcblock.taskprc = pm_task;
	data->am_F_Dijkstra = F_Dijkstra;
	data->am_F_Choose = F_Choose;
	((MovementSystem*)data->am_pm.$sys)->srcblock.destdecelprc = pm_destdecel;
	((MovementSystem*)data->am_pm.$sys)->srcblock.passprc = pm_pass;
	((MovementSystem*)data->am_pm.$sys)->srcblock.pickupprc = pm_pickup;
	((MovementSystem*)data->am_pm.$sys)->srcblock.setdownprc = pm_setdown;
	((MovementSystem*)data->am_pm.$sys)->srcblock.jobselectprc = pm_jobselect;
	data->am_pm.am_ROHT->srcblock.jobfinishprc = pm_ROHT_jobfinish;
	data->am_pIdleCheck->aprc = pIdleCheck_arriving;
	data->am_F_QuickSort = F_QuickSort;
	data->am_pDispatch->aprc = pDispatch_arriving;
	data->am_F_Sqrt = F_Sqrt;
	data->am_pReAssign->aprc = pReAssign_arriving;
	((MovementSystem*)data->am_pm.$sys)->srcblock.workprc = pm_work;
	((MovementSystem*)data->am_pm.$sys)->srcblock.resumemoveprc = pm_resumemove;
	data->am_pDispatchR->aprc = pDispatchR_arriving;
	data->am_F_Dijkstra$func->dispatch = dispatch_F_Dijkstra;
	data->am_F_Dijkstra$func->func = F_Dijkstra;
	data->am_F_Choose$func->dispatch = dispatch_F_Choose;
	data->am_F_Choose$func->func = F_Choose;
	data->am_F_QuickSort$func->dispatch = dispatch_F_QuickSort;
	data->am_F_QuickSort$func->func = F_QuickSort;
	data->am_F_Sqrt$func->dispatch = dispatch_F_Sqrt;
	data->am_F_Sqrt$func->func = F_Sqrt;
}

