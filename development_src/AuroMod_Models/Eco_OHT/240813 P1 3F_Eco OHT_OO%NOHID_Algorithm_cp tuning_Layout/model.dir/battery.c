// battery.c
// AutoMod 12.6.1 Generated File
// Build: 12.6.1.12
// Model name:	model
// Model path:	D:\Project\5. ECO OHT\models\240807~\240813 P1 3F_Eco OHT_OO%NOHID_Algorithm_cp tuning_Layout\model.dir\
// Generated:	Tue Aug 13 10:42:23 2024
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


static int32
pBatteryCheck_arriving(load* this, int32 step, void* args)
{
	struct _localargs {
		AMVehicleListItem* lv26; // 'for each' loop variable
		AMVehicleList* ls26; // 'for each' list
		AMVehicleListItem* lv27; // 'for each' loop variable
		AMVehicleList* ls27; // 'for each' list
		AMVehicleListItem* lv28; // 'for each' loop variable
		AMVehicleList* ls28; // 'for each' list
	} *am_localargs = (struct _localargs*)args;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("battery.m", "Arriving procedure", "model.pBatteryCheck", localactor);
	AMDebuggerParams("model.pBatteryCheck", pBatteryCheck_arriving, localactor, 0, NULL, NULL, NULL);
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
			AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 2);
			while (1 == 1) {
				{
					AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 4);
					if (waitfor(ToModelTime(10, UNITSECONDS), this, pBatteryCheck_arriving, Step 2, am_localargs) == Delayed)
						return Delayed;
Label2: ; // Step 2
				}
				{
					AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 6);
					if (ASIclock > ToModelTime(3600, UNITSECONDS)) {
						{
							AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 8);
							am2_i = 0;
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 9);
							am_localargs->ls26 = 0;
							ListCopy(VehicleList, am_localargs->ls26, am2_vlistOHTall);
							for (am_localargs->lv26 = (am_localargs->ls26) ? (am_localargs->ls26)->first : NULL; am_localargs->lv26; am_localargs->lv26 = am_localargs->lv26->next) {
								am2_vohtTemp = am_localargs->lv26->item;
								{
									{
										AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 11);
										am2_i += 1;
										EntityChanged(0x01000000);
									}
									{
										AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 12);
										if (ValidPtr(am2_vohtTemp, 81, vehicle*)->load.attribute->am2_atBattery < 3960 * 0.50000000000000000) {
											AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 13);
											ValidPtr(am2_vohtTemp, 81, vehicle*)->load.attribute->am2_aiUnder50 = 1;
											EntityChanged(0x00000040);
										}
										else {
											AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 14);
											if (ValidPtr(am2_vohtTemp, 81, vehicle*)->load.attribute->am2_atBattery == 3960 * 0.80000000000000004 && ValidPtr(am2_vohtTemp, 81, vehicle*)->load.attribute->am2_aiUnder50 == 1) {
												{
													AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 16);
													ValidPtr(am2_vohtTemp, 81, vehicle*)->load.attribute->am2_aiUnder50 = 0;
													EntityChanged(0x00000040);
												}
												{
													AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 17);
													{
														int result = inccount(&(am2_cBatteryCycle[ValidIndex("am_model.am_cBatteryCycle", am2_i, 1000)]), 1, this, pBatteryCheck_arriving, Step 3, am_localargs);
														if (result != Continue) return result;
Label3: ;	// Step 3
													}
												}
											}
										}
									}
								}
							}
							ListRemoveAllAndFree(VehicleList, am_localargs->ls26); /* End of for each */
						}
						{
							AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 21);
							am_localargs->ls27 = 0;
							ListCopy(VehicleList, am_localargs->ls27, am2_vlistOHT_Bat);
							for (am_localargs->lv27 = (am_localargs->ls27) ? (am_localargs->ls27)->first : NULL; am_localargs->lv27; am_localargs->lv27 = am_localargs->lv27->next) {
								am2_vohtTemp_Bat = am_localargs->lv27->item;
								{
									{
										AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 23);
										{
											if (isFileValid(am2_vfpOutResult[2], 0)) {
												double pArg1 = FromModelTime(ASIclock, UNITSECONDS);
												char* pArg2 = " ";
												char* pArg3 = "\t";
												char* pArg4 = " ";
												int32 pArg5 = ValidPtr(am2_vohtTemp_Bat, 81, vehicle*)->load.attribute->am2_aID;
												char* pArg6 = " ";
												char* pArg7 = "\t";
												char* pArg8 = " ";
												double pArg9 = ValidPtr(am2_vohtTemp_Bat, 81, vehicle*)->load.attribute->am2_atBattery;

												fprintf((am2_vfpOutResult[2])->fp, "%lf%s%s%s%d%s%s%s%lf\n", pArg1, pArg2, pArg3, pArg4, pArg5, pArg6, pArg7, pArg8, pArg9);
												fflush((am2_vfpOutResult[2])->fp);
											}
										}
									}
								}
							}
							ListRemoveAllAndFree(VehicleList, am_localargs->ls27); /* End of for each */
						}
						{
							AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 26);
							am_localargs->ls28 = 0;
							ListCopy(VehicleList, am_localargs->ls28, am2_vlistROHT_Bat);
							for (am_localargs->lv28 = (am_localargs->ls28) ? (am_localargs->ls28)->first : NULL; am_localargs->lv28; am_localargs->lv28 = am_localargs->lv28->next) {
								am2_vohtTemp_Bat = am_localargs->lv28->item;
								{
									{
										AMDebugger("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor, 28);
										{
											if (isFileValid(am2_vfpOutResult[7], 0)) {
												double pArg1 = FromModelTime(ASIclock, UNITSECONDS);
												char* pArg2 = " ";
												char* pArg3 = "\t";
												char* pArg4 = " ";
												int32 pArg5 = ValidPtr(am2_vohtTemp_Bat, 81, vehicle*)->load.attribute->am2_aID;
												char* pArg6 = " ";
												char* pArg7 = "\t";
												char* pArg8 = " ";
												double pArg9 = ValidPtr(am2_vohtTemp_Bat, 81, vehicle*)->load.attribute->am2_atBattery;

												fprintf((am2_vfpOutResult[7])->fp, "%lf%s%s%s%d%s%s%s%lf\n", pArg1, pArg2, pArg3, pArg4, pArg5, pArg6, pArg7, pArg8, pArg9);
												fflush((am2_vfpOutResult[7])->fp);
											}
										}
									}
								}
							}
							ListRemoveAllAndFree(VehicleList, am_localargs->ls28); /* End of for each */
						}
					}
				}
			}
		}
	}
LabelRet: ;
	ListRemoveAllAndFree(VehicleList, am_localargs->ls26);
	ListRemoveAllAndFree(VehicleList, am_localargs->ls27);
	ListRemoveAllAndFree(VehicleList, am_localargs->ls28);
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("battery.m", "Arriving procedure", "model.pBatteryCheck", pBatteryCheck_arriving, localactor);
	return retval;
} /* end of pBatteryCheck_arriving */

static int32
pm_speedchange(vehicle* am_theVehicle, Velocity am_newVelocity, Acceleration am_newAcceleration)
{
	load* localactor = (load*)am_theVehicle;
	AMDebuggerBeginRoutine("battery.m", "Vehicle speed change function", "model.pm", localactor);
	{
		char*	names[3];
		void*	ptrs[3];
		char*	(*valstrfuncs[3])(void*);
		
		names[0] = "theVehicle";
		ptrs[0] = &am_theVehicle;
		valstrfuncs[0] = VehiclePtr_valstrfunc;
		names[1] = "newVelocity";
		ptrs[1] = &am_newVelocity;
		valstrfuncs[1] = Velocity_valstrfunc;
		names[2] = "newAcceleration";
		ptrs[2] = &am_newAcceleration;
		valstrfuncs[2] = Acceleration_valstrfunc;
		AMDebuggerParams("model.pm", pm_speedchange, localactor, 3, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 37);
			if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime == ToModelTime(0, UNITSECONDS))) {
				{
					AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 39);
					ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime = ASIclock;
					EntityChanged(0x00000040);
				}
				{
					AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 40);
					ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldaccel = ToModelTime(ToModelTime(FromModelDistance(VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS), UNITSECONDS);
					EntityChanged(0x00000040);
				}
				{
					AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 41);
					ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldvelocity = ToModelTime(FromModelDistance(VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS);
					EntityChanged(0x00000040);
				}
				{
					AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 42);
					AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
					return 1;
				}
			}
		}
		{
			AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 47);
			if (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery < am2_vrBatteryCapa * 0.45000000000000001) {
				{
					AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 49);
					ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex = 1;
					EntityChanged(0x00000040);
				}
			}
			else {
				AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 51);
				if (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery < am2_vrBatteryCapa * 0.50000000000000000) {
					{
						AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 53);
						ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex = 2;
						EntityChanged(0x00000040);
					}
				}
				else {
					AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 55);
					if (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery < am2_vrBatteryCapa * 0.55000000000000004) {
						{
							AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 57);
							ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex = 3;
							EntityChanged(0x00000040);
						}
					}
					else {
						AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 59);
						if (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery < am2_vrBatteryCapa * 0.59999999999999998) {
							{
								AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 61);
								ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex = 4;
								EntityChanged(0x00000040);
							}
							{
								AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 62);
								if (StringCompare(VehGetType(ValidPtr(am_theVehicle, 81, vehicle*)), "DefVehicle") == 0 && ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiRecharge == 1) {
									{
										AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 64);
										VsegSetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(ValidPtr(am_theVehicle, 81, vehicle*))), 84, VehSeg*), 21);
										EntityChanged(0x01000040);
									}
									{
										AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 65);
										ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiRecharge = 0;
										EntityChanged(0x00000040);
									}
									{
										AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 66);
										ListAppendItem(VehicleList, am2_vlistOHT, am_theVehicle);	// append item to end of list
									}
									{
										AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 67);
										if (CntGetCurConts(am2_cChargingOHT) > 0) {
											AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 68);
											CntDecContents(am2_cChargingOHT, 1, NULL);
											EntityChanged(0x00000010);
										}
										else {
											AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 70);
											{
												char* pArg1 = "Charging OHT Count Error";

												message("%s", pArg1);
											}
										}
									}
									{
										AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 71);
										{
											char* pArg1 = rel_actorname(am_theVehicle, am_model.$sys);
											char* pArg2 = " ";
											char* pArg3 = "\t";
											char* pArg4 = " ";
											char* pArg5 = "return to work";

											message("%s%s%s%s%s", pArg1, pArg2, pArg3, pArg4, pArg5);
										}
									}
								}
							}
						}
						else {
							AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 74);
							if (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery < am2_vrBatteryCapa * 0.65000000000000002) {
								{
									AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 76);
									ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex = 5;
									EntityChanged(0x00000040);
								}
							}
							else {
								AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 78);
								if (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery < am2_vrBatteryCapa * 0.69999999999999996) {
									{
										AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 80);
										ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex = 6;
										EntityChanged(0x00000040);
									}
									{
										AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 81);
										if (StringCompare(VehGetType(ValidPtr(am_theVehicle, 81, vehicle*)), "ROHT") == 0 && ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiRecharge == 1) {
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 83);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiRecharge = 0;
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 84);
												VsegSetColor(ValidPtr(ListFirstItem(VehSegList, VehGetVsegList(ValidPtr(am_theVehicle, 81, vehicle*))), 84, VehSeg*), 21);
												EntityChanged(0x01000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 85);
												ListAppendItem(VehicleList, am2_vlistOHT, am_theVehicle);	// append item to end of list
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 86);
												{
													char* pArg1 = rel_actorname(am_theVehicle, am_model.$sys);
													char* pArg2 = " ";
													char* pArg3 = "\t";
													char* pArg4 = " ";
													char* pArg5 = "return to work";

													message("%s%s%s%s%s", pArg1, pArg2, pArg3, pArg4, pArg5);
												}
											}
										}
									}
								}
								else {
									AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 89);
									if (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery < am2_vrBatteryCapa * 0.75000000000000000) {
										{
											AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 91);
											ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex = 7;
											EntityChanged(0x00000040);
										}
									}
									else {
										AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 93);
										if (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery < am2_vrBatteryCapa * 0.80000000000000004) {
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 95);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex = 8;
												EntityChanged(0x00000040);
											}
										}
										else {
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 99);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex = 8;
												EntityChanged(0x00000040);
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
		{
			AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 103);
			if ((PthGetColor(ValidPtr(VehGetCurPath(ValidPtr(am_theVehicle, 81, vehicle*)), 43, Path*)) == 0 || PthGetColor(ValidPtr(VehGetCurPath(ValidPtr(am_theVehicle, 81, vehicle*)), 43, Path*)) == 7)) {
				AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 104);
				ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex = 1;
				EntityChanged(0x00000040);
			}
			else {
				AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 105);
				if ((PthGetColor(ValidPtr(VehGetCurPath(ValidPtr(am_theVehicle, 81, vehicle*)), 43, Path*)) == 4)) {
					AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 106);
					ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex = 1;
					EntityChanged(0x00000040);
				}
				else {
					AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 107);
					if ((PthGetColor(ValidPtr(VehGetCurPath(ValidPtr(am_theVehicle, 81, vehicle*)), 43, Path*)) == 1)) {
						AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 108);
						ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex = 2;
						EntityChanged(0x00000040);
					}
					else {
						AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 110);
						ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex = 2;
						EntityChanged(0x00000040);
					}
				}
			}
		}
		{
			AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 112);
			if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_acOldpathcolor == 1)) {
				AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 113);
				ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex = 2;
				EntityChanged(0x00000040);
			}
		}
		{
			AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 115);
			ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = 0;
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 118);
			if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldvelocity == 0)) {
				{
					AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 120);
					if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldaccel == 0)) {
						{
							AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 122);
							if ((VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)) == FromModelTime(ToModelDistance(0, UNITMILLIMETERS), UNITSECONDS))) {
								{
									AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 124);
									if ((VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)) > FromModelTime(FromModelTime(ToModelDistance(0, UNITMILLIMETERS), UNITSECONDS), UNITSECONDS))) {
										{
											AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 126);
											if ((StringCompare(ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_asOldstatus, "Retrieve Pickup") == 0 || StringCompare(ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_asOldstatus, "Deliver Setdown") == 0)) {
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 127);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = FromModelTime((am2_vrBattery_Pick[ValidIndex("am_model.am_vrBattery_Pick", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Pick", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)] * (ASIclock - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime)), UNITSECONDS);
												EntityChanged(0x00000040);
											}
											else {
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 129);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = FromModelTime((am2_vrBattery_Idle[ValidIndex("am_model.am_vrBattery_Idle", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Idle", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)] * (ASIclock - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime)), UNITSECONDS);
												EntityChanged(0x00000040);
											}
										}
										{
											AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 131);
											ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery;
											EntityChanged(0x00000040);
										}
										{
											AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 133);
											if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery > 0)) {
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 134);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime + (ASIclock - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime);
												EntityChanged(0x00000040);
											}
										}
										{
											AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 136);
											ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime = ASIclock;
											EntityChanged(0x00000040);
										}
										{
											AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 137);
											ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldaccel = ToModelTime(ToModelTime(FromModelDistance(VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS), UNITSECONDS);
											EntityChanged(0x00000040);
										}
										{
											AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 138);
											ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldvelocity = ToModelTime(FromModelDistance(VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS);
											EntityChanged(0x00000040);
										}
										{
											AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 139);
											ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_acOldpathcolor = PthGetColor(ValidPtr(VehGetCurPath(ValidPtr(am_theVehicle, 81, vehicle*)), 43, Path*));
											EntityChanged(0x00000040);
										}
									}
									else {
										AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 142);
										AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
										return 1;
									}
								}
							}
							else {
								AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 146);
								AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
								return 1;
							}
						}
					}
					else {
						AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 148);
						if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldaccel > 0)) {
							{
								AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 150);
								if ((VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)) > FromModelTime(ToModelDistance(0, UNITMILLIMETERS), UNITSECONDS))) {
									{
										AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 152);
										if ((VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)) <= FromModelTime(FromModelTime(ToModelDistance(0, UNITMILLIMETERS), UNITSECONDS), UNITSECONDS) || (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_acOldpathcolor != PthGetColor(ValidPtr(VehGetCurPath(ValidPtr(am_theVehicle, 81, vehicle*)), 43, Path*))))) {
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 154);
												if ((VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)) <= ToModelRate(ToModelDistance(1.2000000000000000, UNITMETERS), UNITSECONDS))) {
													{
														AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 156);
														ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = am2_vrBattery_Move1[ValidIndex("am_model.am_vrBattery_Move1", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move1", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)];
														EntityChanged(0x00000040);
													}
												}
												else {
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 160);
													if ((VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)) <= ToModelRate(ToModelDistance(3.2999999999999998, UNITMETERS), UNITSECONDS))) {
														{
															AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 162);
															ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = (am2_vrBattery_Move1[ValidIndex("am_model.am_vrBattery_Move1", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move1", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)] + am2_vrBattery_Move2[ValidIndex("am_model.am_vrBattery_Move2", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move2", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)]);
															EntityChanged(0x00000040);
														}
													}
													else {
														{
															AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 167);
															ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = (am2_vrBattery_Move1[ValidIndex("am_model.am_vrBattery_Move1", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move1", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)] + am2_vrBattery_Move2[ValidIndex("am_model.am_vrBattery_Move2", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move2", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)] + am2_vrBattery_Move3[ValidIndex("am_model.am_vrBattery_Move3", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move3", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)]);
															EntityChanged(0x00000040);
														}
													}
												}
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 172);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery;
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 174);
												if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery > 0)) {
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 175);
													ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime + (ASIclock - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime);
													EntityChanged(0x00000040);
												}
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 177);
												if ((VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)) < FromModelTime(FromModelTime(ToModelDistance(0, UNITMILLIMETERS), UNITSECONDS), UNITSECONDS) && VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)) == ToModelRate(ToModelDistance(3.2999999999999998, UNITMETERS), UNITSECONDS))) {
													{
														AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 179);
														ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = am2_vrBattery_Dec[ValidIndex("am_model.am_vrBattery_Dec", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Dec", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)];
														EntityChanged(0x00000040);
													}
													{
														AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 180);
														ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery;
														EntityChanged(0x00000040);
													}
													{
														AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 182);
														if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery > 0)) {
															AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 183);
															ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime + (ASIclock - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime);
															EntityChanged(0x00000040);
														}
													}
												}
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 186);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime = ASIclock;
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 187);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldaccel = ToModelTime(ToModelTime(FromModelDistance(VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS), UNITSECONDS);
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 188);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldvelocity = ToModelTime(FromModelDistance(VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS);
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 189);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_acOldpathcolor = PthGetColor(ValidPtr(VehGetCurPath(ValidPtr(am_theVehicle, 81, vehicle*)), 43, Path*));
												EntityChanged(0x00000040);
											}
										}
										else {
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 193);
												AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
												return 1;
											}
										}
									}
								}
								else {
									AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 197);
									AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
									return 1;
								}
							}
						}
						else {
							AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 200);
							AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
							return 1;
						}
					}
				}
			}
			else {
				AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 202);
				if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldvelocity > 0)) {
					{
						AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 204);
						if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldaccel == 0)) {
							{
								AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 206);
								if ((VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)) > FromModelTime(ToModelDistance(0, UNITMILLIMETERS), UNITSECONDS))) {
									{
										AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 208);
										if ((VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)) > FromModelTime(FromModelTime(ToModelDistance(0, UNITMILLIMETERS), UNITSECONDS), UNITSECONDS))) {
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 210);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = FromModelTime(((am2_vrBattery_Move4[ValidIndex("am_model.am_vrBattery_Move4", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move4", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)] * (ASIclock - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime))), UNITSECONDS);
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 211);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery;
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 213);
												if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery > 0)) {
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 214);
													ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime + (ASIclock - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime);
													EntityChanged(0x00000040);
												}
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 216);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime = ASIclock;
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 217);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldaccel = ToModelTime(ToModelTime(FromModelDistance(VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS), UNITSECONDS);
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 218);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldvelocity = ToModelTime(FromModelDistance(VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS);
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 219);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_acOldpathcolor = PthGetColor(ValidPtr(VehGetCurPath(ValidPtr(am_theVehicle, 81, vehicle*)), 43, Path*));
												EntityChanged(0x00000040);
											}
										}
										else {
											AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 221);
											if ((VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)) < FromModelTime(FromModelTime(ToModelDistance(0, UNITMILLIMETERS), UNITSECONDS), UNITSECONDS))) {
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 223);
													ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = FromModelTime(((am2_vrBattery_Move4[ValidIndex("am_model.am_vrBattery_Move4", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move4", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)] * (ASIclock - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime))), UNITSECONDS);
													EntityChanged(0x00000040);
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 224);
													ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery;
													EntityChanged(0x00000040);
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 226);
													if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery > 0)) {
														AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 227);
														ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime + (ASIclock - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime);
														EntityChanged(0x00000040);
													}
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 229);
													if ((VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)) == ToModelRate(ToModelDistance(3.2999999999999998, UNITMETERS), UNITSECONDS))) {
														{
															AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 231);
															ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = am2_vrBattery_Dec[ValidIndex("am_model.am_vrBattery_Dec", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Dec", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)];
															EntityChanged(0x00000040);
														}
														{
															AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 232);
															ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery;
															EntityChanged(0x00000040);
														}
														{
															AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 234);
															if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery > 0)) {
																AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 235);
																ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime + (ASIclock - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime);
																EntityChanged(0x00000040);
															}
														}
													}
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 238);
													ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime = ASIclock;
													EntityChanged(0x00000040);
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 239);
													ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldaccel = ToModelTime(ToModelTime(FromModelDistance(VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS), UNITSECONDS);
													EntityChanged(0x00000040);
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 240);
													ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldvelocity = ToModelTime(FromModelDistance(VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS);
													EntityChanged(0x00000040);
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 241);
													ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_acOldpathcolor = PthGetColor(ValidPtr(VehGetCurPath(ValidPtr(am_theVehicle, 81, vehicle*)), 43, Path*));
													EntityChanged(0x00000040);
												}
											}
											else {
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 245);
												AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
												return 1;
											}
										}
									}
								}
								else {
									AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 248);
									AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
									return 1;
								}
							}
						}
						else {
							AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 250);
							if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldaccel > 0)) {
								{
									AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 252);
									if ((VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)) > FromModelTime(ToModelDistance(0, UNITMILLIMETERS), UNITSECONDS))) {
										{
											AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 254);
											if ((VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)) <= FromModelTime(FromModelTime(ToModelDistance(0, UNITMILLIMETERS), UNITSECONDS), UNITSECONDS) || (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_acOldpathcolor != PthGetColor(ValidPtr(VehGetCurPath(ValidPtr(am_theVehicle, 81, vehicle*)), 43, Path*))))) {
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 256);
													if ((VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)) <= ToModelRate(ToModelDistance(1.2000000000000000, UNITMETERS), UNITSECONDS))) {
														{
															AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 258);
															ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = am2_vrBattery_Move1[ValidIndex("am_model.am_vrBattery_Move1", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move1", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)];
															EntityChanged(0x00000040);
														}
													}
													else {
														AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 261);
														if ((VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)) <= ToModelRate(ToModelDistance(3.2999999999999998, UNITMETERS), UNITSECONDS))) {
															{
																AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 263);
																if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldvelocity < ToModelTime(FromModelDistance(ToModelRate(ToModelDistance(1.2000000000000000, UNITMETERS), UNITSECONDS), UNITMILLIMETERS), UNITSECONDS))) {
																	{
																		AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 265);
																		ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = (am2_vrBattery_Move1[ValidIndex("am_model.am_vrBattery_Move1", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move1", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)] + am2_vrBattery_Move2[ValidIndex("am_model.am_vrBattery_Move2", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move2", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)]);
																		EntityChanged(0x00000040);
																	}
																}
																else {
																	{
																		AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 270);
																		ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = am2_vrBattery_Move2[ValidIndex("am_model.am_vrBattery_Move2", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move2", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)];
																		EntityChanged(0x00000040);
																	}
																}
															}
														}
														else {
															{
																AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 276);
																if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldvelocity < ToModelTime(FromModelDistance(ToModelRate(ToModelDistance(1.2000000000000000, UNITMETERS), UNITSECONDS), UNITMILLIMETERS), UNITSECONDS))) {
																	{
																		AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 278);
																		ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = (am2_vrBattery_Move1[ValidIndex("am_model.am_vrBattery_Move1", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move1", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)] + am2_vrBattery_Move2[ValidIndex("am_model.am_vrBattery_Move2", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move2", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)] + am2_vrBattery_Move3[ValidIndex("am_model.am_vrBattery_Move3", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move3", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)]);
																		EntityChanged(0x00000040);
																	}
																}
																else {
																	AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 282);
																	if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldvelocity < ToModelTime(FromModelDistance(ToModelRate(ToModelDistance(3.2999999999999998, UNITMETERS), UNITSECONDS), UNITMILLIMETERS), UNITSECONDS))) {
																		{
																			AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 284);
																			ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = (am2_vrBattery_Move2[ValidIndex("am_model.am_vrBattery_Move2", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move2", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)] + am2_vrBattery_Move3[ValidIndex("am_model.am_vrBattery_Move3", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move3", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)]);
																			EntityChanged(0x00000040);
																		}
																	}
																	else {
																		{
																			AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 289);
																			ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = am2_vrBattery_Move3[ValidIndex("am_model.am_vrBattery_Move3", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Move3", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)];
																			EntityChanged(0x00000040);
																		}
																	}
																}
															}
														}
													}
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 294);
													ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery;
													EntityChanged(0x00000040);
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 296);
													if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery > 0)) {
														AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 297);
														ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime + (ASIclock - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime);
														EntityChanged(0x00000040);
													}
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 299);
													if ((VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)) < FromModelTime(FromModelTime(ToModelDistance(0, UNITMILLIMETERS), UNITSECONDS), UNITSECONDS) && VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)) == ToModelRate(ToModelDistance(3.2999999999999998, UNITMETERS), UNITSECONDS))) {
														{
															AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 301);
															ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery = am2_vrBattery_Dec[ValidIndex("am_model.am_vrBattery_Dec", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiChargeIndex, 2)][ValidIndex("am_model.am_vrBattery_Dec", ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_aiIndex, 100)];
															EntityChanged(0x00000040);
														}
														{
															AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 302);
															ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery;
															EntityChanged(0x00000040);
														}
														{
															AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 304);
															if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arAddBattery > 0)) {
																AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 305);
																ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime = ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atChargetime + (ASIclock - ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime);
																EntityChanged(0x00000040);
															}
														}
													}
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 308);
													ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime = ASIclock;
													EntityChanged(0x00000040);
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 309);
													ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldaccel = ToModelTime(ToModelTime(FromModelDistance(VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS), UNITSECONDS);
													EntityChanged(0x00000040);
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 310);
													ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldvelocity = ToModelTime(FromModelDistance(VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS);
													EntityChanged(0x00000040);
												}
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 311);
													ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_acOldpathcolor = PthGetColor(ValidPtr(VehGetCurPath(ValidPtr(am_theVehicle, 81, vehicle*)), 43, Path*));
													EntityChanged(0x00000040);
												}
											}
											else {
												{
													AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 315);
													AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
													return 1;
												}
											}
										}
									}
									else {
										AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 319);
										AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
										return 1;
									}
								}
							}
							else {
								AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 321);
								if ((ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldaccel < 0)) {
									{
										AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 323);
										if ((VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)) >= FromModelTime(FromModelTime(ToModelDistance(0, UNITMILLIMETERS), UNITSECONDS), UNITSECONDS))) {
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 325);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atOldtime = ASIclock;
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 326);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldaccel = ToModelTime(ToModelTime(FromModelDistance(VehGetCurAccel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS), UNITSECONDS);
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 327);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_arOldvelocity = ToModelTime(FromModelDistance(VehGetCurVel(ValidPtr(am_theVehicle, 81, vehicle*)), UNITMILLIMETERS), UNITSECONDS);
												EntityChanged(0x00000040);
											}
											{
												AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 328);
												ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_acOldpathcolor = PthGetColor(ValidPtr(VehGetCurPath(ValidPtr(am_theVehicle, 81, vehicle*)), 43, Path*));
												EntityChanged(0x00000040);
											}
										}
										else {
											AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 331);
											AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
											return 1;
										}
									}
								}
								else {
									AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 334);
									AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
									return 1;
								}
							}
						}
					}
				}
			}
		}
		{
			AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 337);
			if (ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery > FromModelTime(am2_vtBatteryMax, UNITSECONDS)) {
				AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 338);
				ValidPtr(am_theVehicle, 81, vehicle*)->load.attribute->am2_atBattery = FromModelTime(am2_vtBatteryMax, UNITSECONDS);
				EntityChanged(0x00000040);
			}
		}
		{
			AMDebugger("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor, 340);
			AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("battery.m", "Vehicle speed change function", "model.pm", pm_speedchange, localactor);
} /* end of pm_speedchange */



/* init function for battery.m */
void
model_battery_init(struct model_struct* data)
{
	data->am_pBatteryCheck->aprc = pBatteryCheck_arriving;
	((MovementSystem*)data->am_pm.$sys)->srcblock.speedchangeprc = pm_speedchange;
}

