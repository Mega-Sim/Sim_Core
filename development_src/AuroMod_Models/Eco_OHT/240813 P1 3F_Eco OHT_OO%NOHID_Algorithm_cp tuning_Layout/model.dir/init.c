// init.c
// AutoMod 12.6.1 Generated File
// Build: 12.6.1.12
// Model name:	model
// Model path:	D:\Project\5. ECO OHT\models\240807~\240813 P1 3F_Eco OHT_OO%NOHID_Algorithm_cp tuning_Layout\model.dir\
// Generated:	Tue Aug 13 10:47:44 2024
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

#undef fDistanceMatrix
static int32 fDistanceMatrix(void);
#undef fsetValuable_FilePtr
static int32 fsetValuable_FilePtr(void);
#undef freadFromto
static int32 freadFromto(void);
#undef freadFromto2
static int32 freadFromto2(void);
#undef freadOHTSpec
static int32 freadOHTSpec(void);
#undef freadControl
static int32 freadControl(void);
#undef freadBatcharge
static int32 freadBatcharge(void);

static int32
model_initialize()
{
	AMLocationListItem* am_lv81; // 'for each' loop variable
	AMLocationList* am_ls81 = NULL; // 'for each' list

	{
		{
			am2_vnRoute = 40723;
			EntityChanged(0x01000000);
		}
		{
			am2_vrCapa = 1.6399999999999999;
			EntityChanged(0x01000000);
		}
		{
			am2_vnOHT = 0;
			EntityChanged(0x01000000);
		}
		{
			am2_vnROHT = 0;
			EntityChanged(0x01000000);
		}
		{
			am2_vrOHTspec = 0.59999999999999998;
			EntityChanged(0x01000000);
		}
		{
			am2_vrEfficiency = 0.59999999999999998;
			EntityChanged(0x01000000);
		}
		{
			ListCopy(LocationList, am2_vllpm, SysGetLocations(am_model.am_pm.$sys));
			EntityChanged(0x01000000);
		}
		{
			am_ls81 = 0;
			ListCopy(LocationList, am_ls81, am2_vllpm);
			for (am_lv81 = (am_ls81) ? (am_ls81)->first : NULL; am_lv81; am_lv81 = am_lv81->next) {
				am2_vlocTemp[1] = am_lv81->item;
				{
					{
						if (LocGetColor(ValidPtr(am2_vlocTemp[1], 40, simloc*)) == 4) {
							ListAppendItem(LocationList, am2_vllpurple, am2_vlocTemp[1]);	// append item to end of list
						}
						else {
							if (LocGetColor(ValidPtr(am2_vlocTemp[1], 40, simloc*)) == -1) {
								ListAppendItem(LocationList, am2_vllInherit, am2_vlocTemp[1]);	// append item to end of list
							}
							else {
								if (LocGetColor(ValidPtr(am2_vlocTemp[1], 40, simloc*)) == 2) {
									ListAppendItem(LocationList, am2_vllChargeRoute, am2_vlocTemp[1]);	// append item to end of list
								}
							}
						}
					}
					{
						if (LocGetColor(ValidPtr(am2_vlocTemp[1], 40, simloc*)) != 9) {
							{
								if (LocGetCapacity(ValidPtr(am2_vlocTemp[1], 40, simloc*)) == 10000) {
									ListAppendItem(LocationList, am2_vllLower, am2_vlocTemp[1]);	// append item to end of list
								}
								else {
									ListAppendItem(LocationList, am2_vllUpper, am2_vlocTemp[1]);	// append item to end of list
								}
							}
						}
					}
				}
			}
			ListRemoveAllAndFree(LocationList, am_ls81); /* End of for each */
		}
		{
			am2_vfpDistance = OpenFilePtr(am_model.$sys, "arc/result/distance.txt", "w");
		}
		{
			am2_vnCapa = am2_vrCapa * 100;
			EntityChanged(0x01000000);
		}
		{
			am2_vrBatteryCapa = 3960;
			EntityChanged(0x01000000);
		}
		{
			am2_vtBatteryMax = ToModelTime(am2_vrBatteryCapa * 0.80000000000000004, UNITSECONDS);
			EntityChanged(0x01000000);
		}
		{
			am2_vtBatteryMin = ToModelTime(am2_vrBatteryCapa * 0.20000000000000001, UNITSECONDS);
			EntityChanged(0x01000000);
		}
		{
			am2_vrRecharge = 0.20000000000000001;
			EntityChanged(0x01000000);
		}
		{
			fsetValuable_FilePtr();
		}
		{
			freadFromto();
		}
		{
			freadOHTSpec();
		}
		{
			freadControl();
		}
		{
			freadBatcharge();
		}
		{
			fDistanceMatrix();
		}
		{
	ListRemoveAllAndFree(LocationList, am_ls81);
			return 1;
		}
	}
LabelRet: ;
} /* end of model_initialize */

static int32
fDistanceMatrix()
{
	AMLocationListItem* am_lv82; // 'for each' loop variable
	AMLocationList* am_ls82 = NULL; // 'for each' list
	AMLocationListItem* am_lv83; // 'for each' loop variable
	AMLocationList* am_ls83 = NULL; // 'for each' list
	AMLocationListItem* am_lv84; // 'for each' loop variable
	AMLocationList* am_ls84 = NULL; // 'for each' list

	load* localactor = NULL;
	AMDebuggerBeginRoutine("init.m", "Function", "model.fDistanceMatrix", localactor);
	{
		char*	names[1];
		void*	ptrs[1];
		char*	(*valstrfuncs[1])(void*);
		
		AMDebuggerParams("model.fDistanceMatrix", fDistanceMatrix, localactor, 0, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 48);
			am2_vrBigValue = 999999999;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 49);
			am2_i = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 50);
			am2_j = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 52);
			am2_viSize = Size(List, LocationList, am2_vllDM);
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 54);
			am_ls82 = 0;
			ListCopy(LocationList, am_ls82, am2_vllDM);
			for (am_lv82 = (am_ls82) ? (am_ls82)->first : NULL; am_lv82; am_lv82 = am_lv82->next) {
				am2_vlocTemp[1] = am_lv82->item;
				{
					{
						AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 56);
						am2_i += 1;
						EntityChanged(0x01000000);
					}
					{
						AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 57);
						am_ls83 = 0;
						ListCopy(LocationList, am_ls83, am2_vllDM);
						for (am_lv83 = (am_ls83) ? (am_ls83)->first : NULL; am_lv83; am_lv83 = am_lv83->next) {
							am2_vlocTemp[2] = am_lv83->item;
							{
								{
									AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 59);
									am2_j += 1;
									EntityChanged(0x01000000);
								}
								{
									AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 60);
									if (LocCompare(am2_vlocTemp[1], am2_vlocTemp[2]) != 0) {
										{
											AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 62);
											ListCopy(LocationList, am2_vllTemp, LocGetRouteListTo(ValidPtr(am2_vlocTemp[1], 40, simloc*), ValidPtr(am2_vlocTemp[2], 40, simloc*)));
											EntityChanged(0x01000000);
										}
										{
											AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 64);
											am_ls84 = 0;
											ListCopy(LocationList, am_ls84, am2_vllTemp);
											for (am_lv84 = (am_ls84) ? (am_ls84)->first : NULL; am_lv84; am_lv84 = am_lv84->next) {
												am2_vlocTemp[3] = am_lv84->item;
												{
													{
														AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 66);
														if (LocGetColor(ValidPtr(am2_vlocTemp[3], 40, simloc*)) != 9) {
															AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 67);
															ListRemoveFirstMatch(LocationList, am2_vllTemp, am2_vlocTemp[3]);	// remove first match from list
														}
													}
												}
											}
											ListRemoveAllAndFree(LocationList, am_ls84); /* End of for each */
										}
										{
											AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 70);
											if (Size(List, LocationList, am2_vllTemp) != 0) {
												{
													AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 72);
													am2_vrDM[ValidIndex("am_model.am_vrDM", am2_i, 2200)][ValidIndex("am_model.am_vrDM", am2_j, 2200)] = am2_vrBigValue;
													EntityChanged(0x01000000);
												}
											}
											else {
												{
													AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 76);
													if ((PthGetColor(ValidPtr(LocGetCurPath(ValidPtr(ListIndexItem(LocationList, am2_vllDM, am2_i), 40, simloc*)), 43, Path*)) == 0 && PthGetColor(ValidPtr(LocGetCurPath(ValidPtr(ListIndexItem(LocationList, am2_vllDM, am2_j), 40, simloc*)), 43, Path*)) == 0)) {
														AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 77);
														am2_vrDM[ValidIndex("am_model.am_vrDM", am2_i, 2200)][ValidIndex("am_model.am_vrDM", am2_j, 2200)] = FromModelDistance((LocGetDistToLoc(ValidPtr(am2_vlocTemp[1], 40, simloc*), ValidPtr(am2_vlocTemp[2], 40, simloc*))) / 1000, UNITMILLIMETERS);
														EntityChanged(0x01000000);
													}
													else {
														AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 78);
														if ((PthGetColor(ValidPtr(LocGetCurPath(ValidPtr(ListIndexItem(LocationList, am2_vllDM, am2_i), 40, simloc*)), 43, Path*)) == 0 && PthGetColor(ValidPtr(LocGetCurPath(ValidPtr(ListIndexItem(LocationList, am2_vllDM, am2_j), 40, simloc*)), 43, Path*)) == 1)) {
															AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 79);
															am2_vrDM[ValidIndex("am_model.am_vrDM", am2_i, 2200)][ValidIndex("am_model.am_vrDM", am2_j, 2200)] = FromModelDistance(LocGetDistToLoc(ValidPtr(am2_vlocTemp[1], 40, simloc*), ValidPtr(am2_vlocTemp[2], 40, simloc*)), UNITMILLIMETERS);
															EntityChanged(0x01000000);
														}
														else {
															AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 80);
															if ((PthGetColor(ValidPtr(LocGetCurPath(ValidPtr(ListIndexItem(LocationList, am2_vllDM, am2_i), 40, simloc*)), 43, Path*)) == 1 && PthGetColor(ValidPtr(LocGetCurPath(ValidPtr(ListIndexItem(LocationList, am2_vllDM, am2_j), 40, simloc*)), 43, Path*)) == 0)) {
																AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 81);
																am2_vrDM[ValidIndex("am_model.am_vrDM", am2_i, 2200)][ValidIndex("am_model.am_vrDM", am2_j, 2200)] = FromModelDistance((LocGetDistToLoc(ValidPtr(am2_vlocTemp[1], 40, simloc*), ValidPtr(am2_vlocTemp[2], 40, simloc*))) / 1000, UNITMILLIMETERS);
																EntityChanged(0x01000000);
															}
															else {
																AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 82);
																if ((PthGetColor(ValidPtr(LocGetCurPath(ValidPtr(ListIndexItem(LocationList, am2_vllDM, am2_i), 40, simloc*)), 43, Path*)) == 1 && PthGetColor(ValidPtr(LocGetCurPath(ValidPtr(ListIndexItem(LocationList, am2_vllDM, am2_j), 40, simloc*)), 43, Path*)) == 1)) {
																	AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 83);
																	am2_vrDM[ValidIndex("am_model.am_vrDM", am2_i, 2200)][ValidIndex("am_model.am_vrDM", am2_j, 2200)] = FromModelDistance(LocGetDistToLoc(ValidPtr(am2_vlocTemp[1], 40, simloc*), ValidPtr(am2_vlocTemp[2], 40, simloc*)), UNITMILLIMETERS);
																	EntityChanged(0x01000000);
																}
															}
														}
													}
												}
												{
													AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 85);
													if (LocGetCapacity(ValidPtr(ListIndexItem(LocationList, am2_vllDM, am2_i), 40, simloc*)) == 1500 || LocGetCapacity(ValidPtr(ListIndexItem(LocationList, am2_vllDM, am2_j), 40, simloc*)) == 1500) {
														AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 86);
														am2_vrDM[ValidIndex("am_model.am_vrDM", am2_i, 2200)][ValidIndex("am_model.am_vrDM", am2_j, 2200)] = am2_vrDM[ValidIndex("am_model.am_vrDM", am2_i, 2200)][ValidIndex("am_model.am_vrDM", am2_j, 2200)] * 1.5000000000000000;
														EntityChanged(0x01000000);
													}
												}
											}
										}
									}
								}
							}
						}
						ListRemoveAllAndFree(LocationList, am_ls83); /* End of for each */
					}
					{
						AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 90);
						am2_j = 0;
						EntityChanged(0x01000000);
					}
				}
			}
			ListRemoveAllAndFree(LocationList, am_ls82); /* End of for each */
		}
		{
			AMDebugger("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor, 93);
	ListRemoveAllAndFree(LocationList, am_ls82);
	ListRemoveAllAndFree(LocationList, am_ls83);
	ListRemoveAllAndFree(LocationList, am_ls84);
			AMDebuggerEndRoutine("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("init.m", "Function", "model.fDistanceMatrix", fDistanceMatrix, localactor);
} /* end of fDistanceMatrix */

static int
dispatch_fDistanceMatrix(int nParams, int* argTypes, void** argVals, void** retVal)
{
	static char buf[512];
	int retType;
	static int32 ret;

	if (nParams != 0) {
		message("The function fDistanceMatrix was called from the ActiveX interface with %d parameters, while 0 are required.", nParams);
		return 0;
	}
	ret = fDistanceMatrix();
	*retVal = &ret;
	return 1;
}

static int32
fsetValuable_FilePtr()
{
	load* localactor = NULL;
	AMDebuggerBeginRoutine("init.m", "Function", "model.fsetValuable_FilePtr", localactor);
	{
		char*	names[1];
		void*	ptrs[1];
		char*	(*valstrfuncs[1])(void*);
		
		AMDebuggerParams("model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 0, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 98);
			am2_vfpInFromto = OpenFilePtr(am_model.$sys, "arc/data/fromto_renew.txt", "r");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 101);
			am2_vfpBatcharge = OpenFilePtr(am_model.$sys, "arc/data/BatteryCharge.txt", "r");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 102);
			am2_vfpAvoidingBayEnd = OpenFilePtr(am_model.$sys, "arc/data/AvoidingBayEnd.txt", "r");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 103);
			am2_vfpAvoidingBayEnd_R = OpenFilePtr(am_model.$sys, "arc/data/AvoidingBayEnd_R.txt", "r");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 104);
			am2_vfpReRoute = OpenFilePtr(am_model.$sys, "arc/data/Reroute.txt", "r");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 105);
			am2_vfpClosetNode[1] = OpenFilePtr(am_model.$sys, "arc/data/closest_nodes.txt", "r");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 106);
			am2_vfpVLLDM = OpenFilePtr(am_model.$sys, "arc/data/vllDM.txt", "r");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 109);
			am2_vfpCongLog = OpenFilePtr(am_model.$sys, "arc/result/CongLog.txt", "w");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 110);
			am2_vfpOutResult[1] = OpenFilePtr(am_model.$sys, "arc/result/output.txt", "w");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 111);
			am2_vfpOutResult[2] = OpenFilePtr(am_model.$sys, "arc/result/Battery.txt", "w");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 112);
			am2_vfpOutResult[3] = OpenFilePtr(am_model.$sys, "arc/result/Battery_Change.txt", "w");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 113);
			am2_vfpOutResult[4] = OpenFilePtr(am_model.$sys, "arc/result/Block_Count.txt", "w");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 114);
			am2_vfpOutResult[5] = OpenFilePtr(am_model.$sys, "arc/result/Path_Count.txt", "w");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 115);
			am2_vfpOutResult[6] = OpenFilePtr(am_model.$sys, "arc/result/InRed.txt", "w");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 116);
			am2_vfpOutResult[7] = OpenFilePtr(am_model.$sys, "arc/result/Battery_R.txt", "w");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 117);
			am2_vfpOutResult[8] = OpenFilePtr(am_model.$sys, "arc/result/ROHT_Trace.txt", "w");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 118);
			am2_vfpOutResult[9] = OpenFilePtr(am_model.$sys, "arc/result/Time_in_NoHID.txt", "w");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 119);
			am2_vfpOutResult[11] = OpenFilePtr(am_model.$sys, "arc/result/Battery_Cycles.txt", "w");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 120);
			am2_vfpTimeInRed = OpenFilePtr(am_model.$sys, "arc/result/TimeInRed.txt", "w");
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 123);
			{
				if (isFileValid(am2_vfpOutResult[1], 0)) {
					char* pArg1 = "tLMD";
					char* pArg2 = " ";
					char* pArg3 = "\t";
					char* pArg4 = " ";
					char* pArg5 = "tRetDistance";
					char* pArg6 = " ";
					char* pArg7 = "\t";
					char* pArg8 = " ";
					char* pArg9 = "tTotDistance";
					char* pArg10 = " ";
					char* pArg11 = "\t";
					char* pArg12 = " ";
					char* pArg13 = "tIAssign";
					char* pArg14 = " ";
					char* pArg15 = "\t";
					char* pArg16 = " ";
					char* pArg17 = "tAssign";
					char* pArg18 = " ";
					char* pArg19 = "\t";
					char* pArg20 = " ";
					char* pArg21 = "tUnloadMove";
					char* pArg22 = " ";
					char* pArg23 = "\t";
					char* pArg24 = " ";
					char* pArg25 = "tLoadMove";
					char* pArg26 = " ";
					char* pArg27 = "\t";
					char* pArg28 = " ";
					char* pArg29 = "vnRequest";
					char* pArg30 = " ";
					char* pArg31 = "\t";
					char* pArg32 = " ";
					char* pArg33 = "vnComplete";
					char* pArg34 = " ";
					char* pArg35 = "\t";
					char* pArg36 = " ";
					char* pArg37 = "vnDelay";

					fprintf((am2_vfpOutResult[1])->fp, "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s\n", pArg1, pArg2, pArg3, pArg4, pArg5, pArg6, pArg7, pArg8, pArg9, pArg10, pArg11, pArg12, pArg13, pArg14, pArg15, pArg16, pArg17, pArg18, pArg19, pArg20, pArg21, pArg22, pArg23, pArg24, pArg25, pArg26, pArg27, pArg28, pArg29, pArg30, pArg31, pArg32, pArg33, pArg34, pArg35, pArg36, pArg37);
					fflush((am2_vfpOutResult[1])->fp);
				}
			}
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 127);
			{
				if (isFileValid(am2_vfpCongLog, 0)) {
					char* pArg1 = "theVehicle";
					char* pArg2 = "\t";
					char* pArg3 = " ";
					char* pArg4 = "Delayed Node";
					char* pArg5 = "\t";
					char* pArg6 = "theVehicle A_cgStopOccur";
					char* pArg7 = "\t";
					char* pArg8 = "Stop Duration";

					fprintf((am2_vfpCongLog)->fp, "%15s%s%s%15s%s%10s%s%15s\n", pArg1, pArg2, pArg3, pArg4, pArg5, pArg6, pArg7, pArg8);
					fflush((am2_vfpCongLog)->fp);
				}
			}
		}
		{
			AMDebugger("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor, 130);
			AMDebuggerEndRoutine("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("init.m", "Function", "model.fsetValuable_FilePtr", fsetValuable_FilePtr, localactor);
} /* end of fsetValuable_FilePtr */

static int
dispatch_fsetValuable_FilePtr(int nParams, int* argTypes, void** argVals, void** retVal)
{
	static char buf[512];
	int retType;
	static int32 ret;

	if (nParams != 0) {
		message("The function fsetValuable_FilePtr was called from the ActiveX interface with %d parameters, while 0 are required.", nParams);
		return 0;
	}
	ret = fsetValuable_FilePtr();
	*retVal = &ret;
	return 1;
}

static int32
freadFromto()
{
	load* localactor = NULL;
	AMDebuggerBeginRoutine("init.m", "Function", "model.freadFromto", localactor);
	{
		char*	names[1];
		void*	ptrs[1];
		char*	(*valstrfuncs[1])(void*);
		
		AMDebuggerParams("model.freadFromto", freadFromto, localactor, 0, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("init.m", "Function", "model.freadFromto", freadFromto, localactor, 135);
			am2_i = 1;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadFromto", freadFromto, localactor, 136);
			while (FileGetEof(ValidPtr(am2_vfpInFromto, 24, iofile*)) == 0) {
								{
					if (isFileValid(am2_vfpInFromto, 1)) {
						int rflag;
						static ReadRef st1;

						setupReadRef(&st1, 0, am_model.am_vsStream$var, &am2_vsStream[1], NULL, -1, FALSE);
						AMDebugger("init.m", "Function", "model.freadFromto", freadFromto, localactor, 138);
						rflag = readFile(am2_vfpInFromto->fp, "\n", &st1, NULL);
						SetFileAtEof(am2_vfpInFromto, EOF, rflag);
					}
				}
								{
					int rflag;
					static ReadRef st1;
					static ReadRef st2;
					static ReadRef st3;

					setupReadRef(&st1, 0, am_model.am_vraStream$var, &am2_vraStream[1], NULL, -1, FALSE);
					setupReadRef(&st2, 0, am_model.am_vsaStream$var, &am2_vsaStream[1], NULL, -1, FALSE);
					setupReadRef(&st3, 0, am_model.am_vsaStream$var, &am2_vsaStream[2], NULL, -1, FALSE);
					AMDebugger("init.m", "Function", "model.freadFromto", freadFromto, localactor, 139);
					rflag = readString(am2_vsStream[1], "\t", &st1, &st2, &st3, NULL);
				}
				{
					AMDebugger("init.m", "Function", "model.freadFromto", freadFromto, localactor, 141);
					am2_vroute_Interval[1][ValidIndex("am_model.am_vroute_Interval", am2_i, 99999)] = am2_vraStream[1] / am2_vrCapa;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("init.m", "Function", "model.freadFromto", freadFromto, localactor, 142);
					SetString(&am2_vroute_FromLoc[1][ValidIndex("am_model.am_vroute_FromLoc", am2_i, 99999)], am2_vsaStream[1]);
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("init.m", "Function", "model.freadFromto", freadFromto, localactor, 143);
					SetString(&am2_vroute_ToLoc[1][ValidIndex("am_model.am_vroute_ToLoc", am2_i, 99999)], am2_vsaStream[2]);
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("init.m", "Function", "model.freadFromto", freadFromto, localactor, 146);
					am2_i += 1;
					EntityChanged(0x01000000);
				}
			}
		}
		{
			AMDebugger("init.m", "Function", "model.freadFromto", freadFromto, localactor, 148);
			AMDebuggerEndRoutine("init.m", "Function", "model.freadFromto", freadFromto, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("init.m", "Function", "model.freadFromto", freadFromto, localactor);
} /* end of freadFromto */

static int
dispatch_freadFromto(int nParams, int* argTypes, void** argVals, void** retVal)
{
	static char buf[512];
	int retType;
	static int32 ret;

	if (nParams != 0) {
		message("The function freadFromto was called from the ActiveX interface with %d parameters, while 0 are required.", nParams);
		return 0;
	}
	ret = freadFromto();
	*retVal = &ret;
	return 1;
}

static int32
freadFromto2()
{
	load* localactor = NULL;
	AMDebuggerBeginRoutine("init.m", "Function", "model.freadFromto2", localactor);
	{
		char*	names[1];
		void*	ptrs[1];
		char*	(*valstrfuncs[1])(void*);
		
		AMDebuggerParams("model.freadFromto2", freadFromto2, localactor, 0, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("init.m", "Function", "model.freadFromto2", freadFromto2, localactor, 153);
			am2_i = 1;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadFromto2", freadFromto2, localactor, 154);
			while (FileGetEof(ValidPtr(am2_vfpInFromto2, 24, iofile*)) == 0) {
								{
					if (isFileValid(am2_vfpInFromto2, 1)) {
						int rflag;
						static ReadRef st1;

						setupReadRef(&st1, 0, am_model.am_vsStream$var, &am2_vsStream[2], NULL, -1, FALSE);
						AMDebugger("init.m", "Function", "model.freadFromto2", freadFromto2, localactor, 157);
						rflag = readFile(am2_vfpInFromto2->fp, "\n", &st1, NULL);
						SetFileAtEof(am2_vfpInFromto2, EOF, rflag);
					}
				}
								{
					int rflag;
					static ReadRef st1;
					static ReadRef st2;
					static ReadRef st3;

					setupReadRef(&st1, 0, am_model.am_vraStream$var, &am2_vraStream[1], NULL, -1, FALSE);
					setupReadRef(&st2, 0, am_model.am_vsaStream$var, &am2_vsaStream[1], NULL, -1, FALSE);
					setupReadRef(&st3, 0, am_model.am_vsaStream$var, &am2_vsaStream[2], NULL, -1, FALSE);
					AMDebugger("init.m", "Function", "model.freadFromto2", freadFromto2, localactor, 158);
					rflag = readString(am2_vsStream[2], "\t", &st1, &st2, &st3, NULL);
				}
				{
					AMDebugger("init.m", "Function", "model.freadFromto2", freadFromto2, localactor, 160);
					am2_vroute_Interval[2][ValidIndex("am_model.am_vroute_Interval", am2_i, 99999)] = am2_vraStream[1] / am2_vrCapa;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("init.m", "Function", "model.freadFromto2", freadFromto2, localactor, 161);
					SetString(&am2_vroute_FromLoc[2][ValidIndex("am_model.am_vroute_FromLoc", am2_i, 99999)], am2_vsaStream[1]);
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("init.m", "Function", "model.freadFromto2", freadFromto2, localactor, 162);
					SetString(&am2_vroute_ToLoc[2][ValidIndex("am_model.am_vroute_ToLoc", am2_i, 99999)], am2_vsaStream[2]);
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("init.m", "Function", "model.freadFromto2", freadFromto2, localactor, 163);
					am2_i += 1;
					EntityChanged(0x01000000);
				}
			}
		}
		{
			AMDebugger("init.m", "Function", "model.freadFromto2", freadFromto2, localactor, 165);
			AMDebuggerEndRoutine("init.m", "Function", "model.freadFromto2", freadFromto2, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("init.m", "Function", "model.freadFromto2", freadFromto2, localactor);
} /* end of freadFromto2 */

static int
dispatch_freadFromto2(int nParams, int* argTypes, void** argVals, void** retVal)
{
	static char buf[512];
	int retType;
	static int32 ret;

	if (nParams != 0) {
		message("The function freadFromto2 was called from the ActiveX interface with %d parameters, while 0 are required.", nParams);
		return 0;
	}
	ret = freadFromto2();
	*retVal = &ret;
	return 1;
}

static int32
freadOHTSpec()
{
	load* localactor = NULL;
	AMDebuggerBeginRoutine("init.m", "Function", "model.freadOHTSpec", localactor);
	{
		char*	names[1];
		void*	ptrs[1];
		char*	(*valstrfuncs[1])(void*);
		
		AMDebuggerParams("model.freadOHTSpec", freadOHTSpec, localactor, 0, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("init.m", "Function", "model.freadOHTSpec", freadOHTSpec, localactor, 170);
			am2_vrNormalVelocity = 3.2999999999999998;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadOHTSpec", freadOHTSpec, localactor, 171);
			am2_vrCurveVelocity = 1.0000000000000000 * am2_vrOHTspec;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadOHTSpec", freadOHTSpec, localactor, 172);
			am2_vrAcceleration = 2 * am2_vrOHTspec;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadOHTSpec", freadOHTSpec, localactor, 173);
			am2_vrDeceleration = 3 * am2_vrOHTspec;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadOHTSpec", freadOHTSpec, localactor, 174);
			am2_vrBrakeDistance = 4.5000000000000000;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadOHTSpec", freadOHTSpec, localactor, 175);
			am2_vrStopDistance = 0.38000000000000000;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadOHTSpec", freadOHTSpec, localactor, 176);
			am2_vtResume = ToModelTime(0.50000000000000000, UNITSECONDS);
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadOHTSpec", freadOHTSpec, localactor, 177);
			am2_vtLoading[1] = ToModelTime(9, UNITSECONDS);
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadOHTSpec", freadOHTSpec, localactor, 179);
			{
				char* pArg1 = "Number of OHT: ";
				int32 pArg2 = am2_vnOHT;

				updatelabel(am2_lblOHT, "%s%d", pArg1, pArg2);
			}
		}
		{
			AMDebugger("init.m", "Function", "model.freadOHTSpec", freadOHTSpec, localactor, 180);
			{
				char* pArg1 = "Capa : ";
				int32 pArg2 = am2_vnCapa;

				updatelabel(am2_lblCapa, "%s%d", pArg1, pArg2);
			}
		}
		{
			AMDebugger("init.m", "Function", "model.freadOHTSpec", freadOHTSpec, localactor, 182);
			AMDebuggerEndRoutine("init.m", "Function", "model.freadOHTSpec", freadOHTSpec, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("init.m", "Function", "model.freadOHTSpec", freadOHTSpec, localactor);
} /* end of freadOHTSpec */

static int
dispatch_freadOHTSpec(int nParams, int* argTypes, void** argVals, void** retVal)
{
	static char buf[512];
	int retType;
	static int32 ret;

	if (nParams != 0) {
		message("The function freadOHTSpec was called from the ActiveX interface with %d parameters, while 0 are required.", nParams);
		return 0;
	}
	ret = freadOHTSpec();
	*retVal = &ret;
	return 1;
}

static int32
freadControl()
{
	load* localactor = NULL;
	AMDebuggerBeginRoutine("init.m", "Function", "model.freadControl", localactor);
	{
		char*	names[1];
		void*	ptrs[1];
		char*	(*valstrfuncs[1])(void*);
		
		AMDebuggerParams("model.freadControl", freadControl, localactor, 0, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 186);
			am2_vtRun = ToModelTime(1, UNITSECONDS);
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 187);
			am2_vtSchedule = ToModelTime(5, UNITSECONDS);
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 188);
			am2_vtPriorityCost = ToModelTime(100, UNITSECONDS);
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 189);
			am2_vnTimeWeight = 1.0000000000000000;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 190);
			am2_vtTimeLimit = ToModelTime(300, UNITSECONDS);
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 191);
			am2_vnPark = 195;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 193);
			while (FileGetEof(ValidPtr(am2_vfpAvoidingBayEnd, 24, iofile*)) == 0) {
								{
					if (isFileValid(am2_vfpAvoidingBayEnd, 1)) {
						int rflag;
						static ReadRef st1;

						setupReadRef(&st1, 0, am_model.am_vsStream$var, &am2_vsStream[1], NULL, -1, FALSE);
						AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 195);
						rflag = readFile(am2_vfpAvoidingBayEnd->fp, "\n", &st1, NULL);
						SetFileAtEof(am2_vfpAvoidingBayEnd, EOF, rflag);
					}
				}
				{
					AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 196);
					am2_vlocTemp[1] = str2Location(am2_vsStream[1]);
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 197);
					if (LocCompare(am2_vlocTemp[1], NULL) != 0) {
						AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 198);
						ListAppendItem(LocationList, am2_vll_ABE, am2_vlocTemp[1]);	// append item to end of list
					}
				}
			}
		}
		{
			AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 201);
			while (FileGetEof(ValidPtr(am2_vfpAvoidingBayEnd_R, 24, iofile*)) == 0) {
								{
					if (isFileValid(am2_vfpAvoidingBayEnd_R, 1)) {
						int rflag;
						static ReadRef st1;

						setupReadRef(&st1, 0, am_model.am_vsStream$var, &am2_vsStream[1], NULL, -1, FALSE);
						AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 203);
						rflag = readFile(am2_vfpAvoidingBayEnd_R->fp, "\n", &st1, NULL);
						SetFileAtEof(am2_vfpAvoidingBayEnd_R, EOF, rflag);
					}
				}
				{
					AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 204);
					am2_vlocTemp[1] = str2Location(am2_vsStream[1]);
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 205);
					if (LocCompare(am2_vlocTemp[1], NULL) != 0) {
						AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 206);
						ListAppendItem(LocationList, am2_vll_ABE_R, am2_vlocTemp[1]);	// append item to end of list
					}
				}
			}
		}
		{
			AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 209);
			am2_i = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 210);
			while (FileGetEof(ValidPtr(am2_vfpClosetNode[1], 24, iofile*)) == 0) {
				{
					AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 212);
					am2_i += 1;
					EntityChanged(0x01000000);
				}
								{
					if (isFileValid(am2_vfpClosetNode[1], 1)) {
						int rflag;
						static ReadRef st1;

						setupReadRef(&st1, 0, am_model.am_vsStream$var, &am2_vsStream[1], NULL, -1, FALSE);
						AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 213);
						rflag = readFile(am2_vfpClosetNode[1]->fp, "\n", &st1, NULL);
						SetFileAtEof(am2_vfpClosetNode[1], EOF, rflag);
					}
				}
								{
					int rflag;
					static ReadRef st1;
					static ReadRef st2;
					static ReadRef st3;
					static ReadRef st4;

					setupReadRef(&st1, 0, am_model.am_vsaStream$var, &am2_vsaStream[1], NULL, -1, FALSE);
					setupReadRef(&st2, 0, am_model.am_vsaStream$var, &am2_vsaStream[2], NULL, -1, FALSE);
					setupReadRef(&st3, 0, am_model.am_viaStream$var, &am2_viaStream[1], NULL, -1, FALSE);
					setupReadRef(&st4, 0, am_model.am_viaStream$var, &am2_viaStream[2], NULL, -1, FALSE);
					AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 214);
					rflag = readString(am2_vsStream[1], "\t", &st1, &st2, &st3, &st4, NULL);
				}
				{
					AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 215);
					am2_vlocClosestFr[1][ValidIndex("am_model.am_vlocClosestFr", am2_i, 3500)] = str2Location(am2_vsaStream[1]);
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 216);
					am2_vlocClosestTo[1][ValidIndex("am_model.am_vlocClosestTo", am2_i, 3500)] = str2Location(am2_vsaStream[2]);
					EntityChanged(0x01000000);
				}
			}
		}
		{
			AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 221);
			am2_i = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 222);
			while (FileGetEof(ValidPtr(am2_vfpVLLDM, 24, iofile*)) == 0) {
				{
					AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 224);
					am2_i += 1;
					EntityChanged(0x01000000);
				}
								{
					if (isFileValid(am2_vfpVLLDM, 1)) {
						int rflag;
						static ReadRef st1;

						setupReadRef(&st1, 0, am_model.am_vsStream$var, &am2_vsStream[1], NULL, -1, FALSE);
						AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 225);
						rflag = readFile(am2_vfpVLLDM->fp, "\n", &st1, NULL);
						SetFileAtEof(am2_vfpVLLDM, EOF, rflag);
					}
				}
				{
					AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 226);
					am2_vlocTemp[1] = str2Location(am2_vsStream[1]);
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 227);
					if (LocCompare(am2_vlocTemp[1], NULL) != 0) {
						AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 228);
						ListAppendItem(LocationList, am2_vllDM, am2_vlocTemp[1]);	// append item to end of list
					}
				}
			}
		}
		{
			AMDebugger("init.m", "Function", "model.freadControl", freadControl, localactor, 233);
			AMDebuggerEndRoutine("init.m", "Function", "model.freadControl", freadControl, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("init.m", "Function", "model.freadControl", freadControl, localactor);
} /* end of freadControl */

static int
dispatch_freadControl(int nParams, int* argTypes, void** argVals, void** retVal)
{
	static char buf[512];
	int retType;
	static int32 ret;

	if (nParams != 0) {
		message("The function freadControl was called from the ActiveX interface with %d parameters, while 0 are required.", nParams);
		return 0;
	}
	ret = freadControl();
	*retVal = &ret;
	return 1;
}

static int32
freadBatcharge()
{
	load* localactor = NULL;
	AMDebuggerBeginRoutine("init.m", "Function", "model.freadBatcharge", localactor);
	{
		char*	names[1];
		void*	ptrs[1];
		char*	(*valstrfuncs[1])(void*);
		
		AMDebuggerParams("model.freadBatcharge", freadBatcharge, localactor, 0, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 237);
			am2_i = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 238);
			while (FileGetEof(ValidPtr(am2_vfpBatcharge, 24, iofile*)) == 0) {
								{
					if (isFileValid(am2_vfpBatcharge, 1)) {
						int rflag;
						static ReadRef st1;

						setupReadRef(&st1, 0, am_model.am_vsStream$var, &am2_vsStream[1], NULL, -1, FALSE);
						AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 240);
						rflag = readFile(am2_vfpBatcharge->fp, "\n", &st1, NULL);
						SetFileAtEof(am2_vfpBatcharge, EOF, rflag);
					}
				}
				{
					AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 242);
					if (am2_i == 0) {
						AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 243);
						am2_viTempBat = str2Integer(am2_vsStream[1]);
						EntityChanged(0x01000000);
					}
					else {
						AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 245);
						if (am2_i < am2_viTempBat + 1) {
														{
								int rflag;
								static ReadRef st1;
								static ReadRef st2;
								static ReadRef st3;
								static ReadRef st4;
								static ReadRef st5;
								static ReadRef st6;
								static ReadRef st7;

								setupReadRef(&st1, 0, am_model.am_vraStream$var, &am2_vraStream[1], NULL, -1, FALSE);
								setupReadRef(&st2, 0, am_model.am_vraStream$var, &am2_vraStream[2], NULL, -1, FALSE);
								setupReadRef(&st3, 0, am_model.am_vraStream$var, &am2_vraStream[3], NULL, -1, FALSE);
								setupReadRef(&st4, 0, am_model.am_vraStream$var, &am2_vraStream[4], NULL, -1, FALSE);
								setupReadRef(&st5, 0, am_model.am_vraStream$var, &am2_vraStream[5], NULL, -1, FALSE);
								setupReadRef(&st6, 0, am_model.am_vraStream$var, &am2_vraStream[6], NULL, -1, FALSE);
								setupReadRef(&st7, 0, am_model.am_vraStream$var, &am2_vraStream[7], NULL, -1, FALSE);
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 247);
								rflag = readString(am2_vsStream[1], "\t", &st1, &st2, &st3, &st4, &st5, &st6, &st7, NULL);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 249);
								am2_vrBattery_Idle[1][ValidIndex("am_model.am_vrBattery_Idle", am2_i, 100)] = am2_vraStream[1] * am2_vrEfficiency;
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 250);
								am2_vrBattery_Move1[1][ValidIndex("am_model.am_vrBattery_Move1", am2_i, 100)] = am2_vraStream[2] * am2_vrEfficiency;
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 251);
								am2_vrBattery_Move2[1][ValidIndex("am_model.am_vrBattery_Move2", am2_i, 100)] = am2_vraStream[3] * am2_vrEfficiency;
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 252);
								am2_vrBattery_Move3[1][ValidIndex("am_model.am_vrBattery_Move3", am2_i, 100)] = am2_vraStream[4];
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 253);
								am2_vrBattery_Move4[1][ValidIndex("am_model.am_vrBattery_Move4", am2_i, 100)] = am2_vraStream[5] * am2_vrEfficiency;
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 254);
								am2_vrBattery_Dec[1][ValidIndex("am_model.am_vrBattery_Dec", am2_i, 100)] = am2_vraStream[6] * am2_vrEfficiency;
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 255);
								am2_vrBattery_Pick[1][ValidIndex("am_model.am_vrBattery_Pick", am2_i, 100)] = am2_vraStream[7] * am2_vrEfficiency;
								EntityChanged(0x01000000);
							}
						}
						else {
														{
								int rflag;
								static ReadRef st1;
								static ReadRef st2;
								static ReadRef st3;
								static ReadRef st4;
								static ReadRef st5;
								static ReadRef st6;
								static ReadRef st7;

								setupReadRef(&st1, 0, am_model.am_vraStream$var, &am2_vraStream[1], NULL, -1, FALSE);
								setupReadRef(&st2, 0, am_model.am_vraStream$var, &am2_vraStream[2], NULL, -1, FALSE);
								setupReadRef(&st3, 0, am_model.am_vraStream$var, &am2_vraStream[3], NULL, -1, FALSE);
								setupReadRef(&st4, 0, am_model.am_vraStream$var, &am2_vraStream[4], NULL, -1, FALSE);
								setupReadRef(&st5, 0, am_model.am_vraStream$var, &am2_vraStream[5], NULL, -1, FALSE);
								setupReadRef(&st6, 0, am_model.am_vraStream$var, &am2_vraStream[6], NULL, -1, FALSE);
								setupReadRef(&st7, 0, am_model.am_vraStream$var, &am2_vraStream[7], NULL, -1, FALSE);
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 259);
								rflag = readString(am2_vsStream[1], "\t", &st1, &st2, &st3, &st4, &st5, &st6, &st7, NULL);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 261);
								am2_vrBattery_Idle[2][ValidIndex("am_model.am_vrBattery_Idle", am2_i - am2_viTempBat, 100)] = am2_vraStream[1];
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 262);
								am2_vrBattery_Move1[2][ValidIndex("am_model.am_vrBattery_Move1", am2_i - am2_viTempBat, 100)] = am2_vraStream[2];
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 263);
								am2_vrBattery_Move2[2][ValidIndex("am_model.am_vrBattery_Move2", am2_i - am2_viTempBat, 100)] = am2_vraStream[3];
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 264);
								am2_vrBattery_Move3[2][ValidIndex("am_model.am_vrBattery_Move3", am2_i - am2_viTempBat, 100)] = am2_vraStream[4];
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 265);
								am2_vrBattery_Move4[2][ValidIndex("am_model.am_vrBattery_Move4", am2_i - am2_viTempBat, 100)] = am2_vraStream[5];
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 266);
								am2_vrBattery_Dec[2][ValidIndex("am_model.am_vrBattery_Dec", am2_i - am2_viTempBat, 100)] = am2_vraStream[6] * am2_vrEfficiency;
								EntityChanged(0x01000000);
							}
							{
								AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 267);
								am2_vrBattery_Pick[2][ValidIndex("am_model.am_vrBattery_Pick", am2_i - am2_viTempBat, 100)] = am2_vraStream[7];
								EntityChanged(0x01000000);
							}
						}
					}
				}
				{
					AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 269);
					am2_i += 1;
					EntityChanged(0x01000000);
				}
			}
		}
		{
			AMDebugger("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor, 272);
			AMDebuggerEndRoutine("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("init.m", "Function", "model.freadBatcharge", freadBatcharge, localactor);
} /* end of freadBatcharge */

static int
dispatch_freadBatcharge(int nParams, int* argTypes, void** argVals, void** retVal)
{
	static char buf[512];
	int retType;
	static int32 ret;

	if (nParams != 0) {
		message("The function freadBatcharge was called from the ActiveX interface with %d parameters, while 0 are required.", nParams);
		return 0;
	}
	ret = freadBatcharge();
	*retVal = &ret;
	return 1;
}

static int32
model_snap()
{
	load* localactor = NULL;
	AMDebuggerBeginRoutine("init.m", "Model snap function", "model", localactor);
	{
		char*	names[1];
		void*	ptrs[1];
		char*	(*valstrfuncs[1])(void*);
		
		AMDebuggerParams("model", model_snap, localactor, 0, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 277);
			{
				char* pArg1 = "ROHT Jobs\t";
				char* pArg2 = " ";
				int32 pArg3 = Size(List, VehicleList, am2_vlistROHT);

				message("%s%s%d", pArg1, pArg2, pArg3);
			}
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 279);
			{
				int32 pArg1 = CntGetCurConts(ValidPtr(&(am2_cLoadMakeID[1]), 10, counter*));
				char* pArg2 = " ";
				char* pArg3 = "\t";
				char* pArg4 = " ";
				int32 pArg5 = CntGetCurConts(ValidPtr(&(am2_cLoadMakeID[2]), 10, counter*));
				char* pArg6 = " ";
				char* pArg7 = "\t";
				char* pArg8 = " ";
				int32 pArg9 = CntGetCurConts(ValidPtr(&(am2_cLoadMakeID[3]), 10, counter*));

				message("%d%s%s%s%d%s%s%s%d", pArg1, pArg2, pArg3, pArg4, pArg5, pArg6, pArg7, pArg8, pArg9);
			}
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 281);
			{
				if (isFileValid(am2_vfpOutResult[1], 0)) {
					double pArg1 = TblGetAvContsR(am2_tDelDistance);
					char* pArg2 = " ";
					char* pArg3 = "\t";
					char* pArg4 = " ";
					double pArg5 = TblGetAvContsR(am2_tRetDistance);
					char* pArg6 = " ";
					char* pArg7 = "\t";
					char* pArg8 = " ";
					double pArg9 = TblGetAvContsR(am2_tTotDistance);
					char* pArg10 = " ";
					char* pArg11 = "\t";
					char* pArg12 = " ";
					double pArg13 = TblGetAvContsR(am2_tAssignInit);
					char* pArg14 = " ";
					char* pArg15 = "\t";
					double pArg16 = TblGetAvContsR(am2_tAssign);
					char* pArg17 = " ";
					char* pArg18 = "\t";
					char* pArg19 = " ";
					double pArg20 = TblGetAvContsR(am2_tUnloadMove);
					char* pArg21 = " ";
					char* pArg22 = "\t";
					char* pArg23 = " ";
					double pArg24 = TblGetAvContsR(am2_tLoadMove);
					char* pArg25 = " ";
					char* pArg26 = "\t";
					char* pArg27 = " ";
					double pArg28 = ToModelTime(am2_vnRequest / am2_vtRun, UNITSECONDS);
					char* pArg29 = " ";
					char* pArg30 = "\t";
					char* pArg31 = " ";
					double pArg32 = ToModelTime(am2_vnComplete / am2_vtRun, UNITSECONDS);
					char* pArg33 = " ";
					char* pArg34 = "\t";
					char* pArg35 = " ";
					double pArg36 = ToModelTime(am2_vnDelay / am2_vtRun, UNITSECONDS);

					fprintf((am2_vfpOutResult[1])->fp, "%lf%s%s%s%lf%s%s%s%lf%s%s%s%lf%s%s%lf%s%s%s%lf%s%s%s%lf%s%s%s%lf%s%s%s%lf%s%s%s%lf\n", pArg1, pArg2, pArg3, pArg4, pArg5, pArg6, pArg7, pArg8, pArg9, pArg10, pArg11, pArg12, pArg13, pArg14, pArg15, pArg16, pArg17, pArg18, pArg19, pArg20, pArg21, pArg22, pArg23, pArg24, pArg25, pArg26, pArg27, pArg28, pArg29, pArg30, pArg31, pArg32, pArg33, pArg34, pArg35, pArg36);
					fflush((am2_vfpOutResult[1])->fp);
				}
			}
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 286);
			{
				if (isFileValid(am2_vfpOutResult[3], 0)) {
					double pArg1 = TblGetAvContsR(am2_tBatteryChange_Idle);
					char* pArg2 = " ";
					char* pArg3 = "\t";
					char* pArg4 = " ";
					double pArg5 = TblGetAvContsR(am2_tBatteryChange_Ret);
					char* pArg6 = " ";
					char* pArg7 = "\t";
					char* pArg8 = " ";
					double pArg9 = TblGetAvContsR(am2_tBatteryChange_Del);
					char* pArg10 = " ";
					char* pArg11 = "\t";
					char* pArg12 = " ";
					double pArg13 = TblGetAvContsR(am2_tBatteryChange_Ret) + TblGetAvContsR(am2_tBatteryChange_Del);

					fprintf((am2_vfpOutResult[3])->fp, "%lf%s%s%s%lf%s%s%s%lf%s%s%s%lf\n", pArg1, pArg2, pArg3, pArg4, pArg5, pArg6, pArg7, pArg8, pArg9, pArg10, pArg11, pArg12, pArg13);
					fflush((am2_vfpOutResult[3])->fp);
				}
			}
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 289);
			{
				char* pArg1 = "\n";
				char* pArg2 = " ";
				char* pArg3 = "IAT: ";
				char* pArg4 = " ";
				double pArg5 = TblGetAvContsR(am2_tAssignInit);
				char* pArg6 = " ";
				char* pArg7 = "\t";
				char* pArg8 = " ";
				char* pArg9 = "FAT: ";
				char* pArg10 = " ";
				double pArg11 = TblGetAvContsR(am2_tAssign);
				char* pArg12 = " ";
				char* pArg13 = "\n";
				char* pArg14 = " ";
				char* pArg15 = "\t";
				char* pArg16 = " ";
				char* pArg17 = "UMT: ";
				char* pArg18 = " ";
				double pArg19 = (TblGetAvContsR(am2_tUnloadMove) + TblGetAvContsR(am2_tAssign) - TblGetAvContsR(am2_tAssignInit));
				char* pArg20 = " ";
				char* pArg21 = "\t";
				char* pArg22 = " ";
				char* pArg23 = "LMT: ";
				char* pArg24 = " ";
				double pArg25 = TblGetAvContsR(am2_tLoadMove);
				char* pArg26 = " ";
				char* pArg27 = "\n";
				char* pArg28 = " ";
				char* pArg29 = "\t";
				char* pArg30 = "TT: ";
				char* pArg31 = " ";
				double pArg32 = (TblGetAvContsR(am2_tUnloadMove) + TblGetAvContsR(am2_tAssign) - TblGetAvContsR(am2_tAssignInit) + TblGetAvContsR(am2_tLoadMove));
				char* pArg33 = " ";
				char* pArg34 = "\t";
				char* pArg35 = " ";
				char* pArg36 = "DT: ";
				char* pArg37 = " ";
				double pArg38 = (TblGetAvContsR(am2_tUnloadMove) + TblGetAvContsR(am2_tAssign) + TblGetAvContsR(am2_tLoadMove));
				char* pArg39 = " ";
				char* pArg40 = "\n";
				char* pArg41 = " ";
				char* pArg42 = "\t";
				char* pArg43 = "Request: ";
				char* pArg44 = " ";
				double pArg45 = ToModelTime(am2_vnRequest / am2_vtRun, UNITSECONDS);
				char* pArg46 = " ";
				char* pArg47 = "\t";
				char* pArg48 = " ";
				char* pArg49 = "Complete: ";
				char* pArg50 = " ";
				double pArg51 = ToModelTime(am2_vnComplete / am2_vtRun, UNITSECONDS);

				message("%s%s%s%s%lf%s%s%s%s%s%lf%s%s%s%s%s%s%s%lf%s%s%s%s%s%lf%s%s%s%s%s%s%lf%s%s%s%s%s%lf%s%s%s%s%s%s%lf%s%s%s%s%s%lf", pArg1, pArg2, pArg3, pArg4, pArg5, pArg6, pArg7, pArg8, pArg9, pArg10, pArg11, pArg12, pArg13, pArg14, pArg15, pArg16, pArg17, pArg18, pArg19, pArg20, pArg21, pArg22, pArg23, pArg24, pArg25, pArg26, pArg27, pArg28, pArg29, pArg30, pArg31, pArg32, pArg33, pArg34, pArg35, pArg36, pArg37, pArg38, pArg39, pArg40, pArg41, pArg42, pArg43, pArg44, pArg45, pArg46, pArg47, pArg48, pArg49, pArg50, pArg51);
			}
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 296);
			{
				if (isFileValid(am2_vfpOutResult[4], 0)) {
					int32 pArg1 = am2_viBC_move;
					char* pArg2 = " ";
					char* pArg3 = "\t";
					char* pArg4 = " ";
					int32 pArg5 = am2_viBC_retrieve;
					char* pArg6 = " ";
					char* pArg7 = "\t";
					char* pArg8 = " ";
					int32 pArg9 = am2_viBC_deliver;
					char* pArg10 = " ";
					char* pArg11 = "\t";
					char* pArg12 = " ";
					int32 pArg13 = am2_viBR_move;
					char* pArg14 = " ";
					char* pArg15 = "\t";
					char* pArg16 = " ";
					int32 pArg17 = am2_viBR_retrieve;
					char* pArg18 = " ";
					char* pArg19 = "\t";
					char* pArg20 = " ";
					int32 pArg21 = am2_viBR_deliver;

					fprintf((am2_vfpOutResult[4])->fp, "%d%s%s%s%d%s%s%s%d%s%s%s%d%s%s%s%d%s%s%s%d\n", pArg1, pArg2, pArg3, pArg4, pArg5, pArg6, pArg7, pArg8, pArg9, pArg10, pArg11, pArg12, pArg13, pArg14, pArg15, pArg16, pArg17, pArg18, pArg19, pArg20, pArg21);
					fflush((am2_vfpOutResult[4])->fp);
				}
			}
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 297);
			{
				int32 pArg1 = am2_viBC_move;
				char* pArg2 = " ";
				char* pArg3 = "\t";
				char* pArg4 = " ";
				int32 pArg5 = am2_viBC_retrieve;
				char* pArg6 = " ";
				char* pArg7 = "\t";
				char* pArg8 = " ";
				int32 pArg9 = am2_viBC_deliver;
				char* pArg10 = " ";
				char* pArg11 = "\t";
				char* pArg12 = " ";
				int32 pArg13 = am2_viBR_move;
				char* pArg14 = " ";
				char* pArg15 = "\t";
				char* pArg16 = " ";
				int32 pArg17 = am2_viBR_retrieve;
				char* pArg18 = " ";
				char* pArg19 = "\t";
				char* pArg20 = " ";
				int32 pArg21 = am2_viBR_deliver;

				message("%d%s%s%s%d%s%s%s%d%s%s%s%d%s%s%s%d%s%s%s%d", pArg1, pArg2, pArg3, pArg4, pArg5, pArg6, pArg7, pArg8, pArg9, pArg10, pArg11, pArg12, pArg13, pArg14, pArg15, pArg16, pArg17, pArg18, pArg19, pArg20, pArg21);
			}
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 298);
			am2_viBC_move = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 299);
			am2_viBC_retrieve = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 300);
			am2_viBC_deliver = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 301);
			am2_viBR_move = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 302);
			am2_viBR_retrieve = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 303);
			am2_viBR_deliver = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 305);
			{
				if (isFileValid(am2_vfpOutResult[6], 0)) {
					int32 pArg1 = CntGetCurConts(am2_cChargingOHT);

					fprintf((am2_vfpOutResult[6])->fp, "%d\n", pArg1);
					fflush((am2_vfpOutResult[6])->fp);
				}
			}
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 307);
			am2_vnRequest = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 308);
			am2_vnComplete = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 309);
			am2_vnDelay = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Model snap function", "model", model_snap, localactor, 311);
			AMDebuggerEndRoutine("init.m", "Model snap function", "model", model_snap, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("init.m", "Model snap function", "model", model_snap, localactor);
} /* end of model_snap */

static int32
model_finished()
{
	load* localactor = NULL;
	AMDebuggerBeginRoutine("init.m", "Model finished function", "model", localactor);
	{
		char*	names[1];
		void*	ptrs[1];
		char*	(*valstrfuncs[1])(void*);
		
		AMDebuggerParams("model", model_finished, localactor, 0, names, ptrs, valstrfuncs);
	}
	{
		{
			AMDebugger("init.m", "Model finished function", "model", model_finished, localactor, 317);
			am2_i = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("init.m", "Model finished function", "model", model_finished, localactor, 318);
			while (am2_i < am2_vnOHT) {
				{
					AMDebugger("init.m", "Model finished function", "model", model_finished, localactor, 320);
					am2_i += 1;
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("init.m", "Model finished function", "model", model_finished, localactor, 321);
					{
						if (isFileValid(am2_vfpOutResult[11], 0)) {
							int32 pArg1 = am2_i;
							char* pArg2 = " ";
							char* pArg3 = "\t";
							char* pArg4 = " ";
							int32 pArg5 = CntGetCurConts(ValidPtr(&(am2_cBatteryCycle[ValidIndex("am_model.am_cBatteryCycle", am2_i, 1000)]), 10, counter*));

							fprintf((am2_vfpOutResult[11])->fp, "%d%s%s%s%d\n", pArg1, pArg2, pArg3, pArg4, pArg5);
							fflush((am2_vfpOutResult[11])->fp);
						}
					}
				}
			}
		}
		{
			AMDebugger("init.m", "Model finished function", "model", model_finished, localactor, 324);
			AMDebuggerEndRoutine("init.m", "Model finished function", "model", model_finished, localactor);
			return 1;
		}
	}
LabelRet: ;
	AMDebuggerEndRoutine("init.m", "Model finished function", "model", model_finished, localactor);
} /* end of model_finished */



/* init function for init.m */
void
model_init_init(struct model_struct* data)
{
	((ProcSystem*)data->$sys)->modelInitPtr = model_initialize;
	data->am_fDistanceMatrix = fDistanceMatrix;
	data->am_fsetValuable_FilePtr = fsetValuable_FilePtr;
	data->am_freadFromto = freadFromto;
	data->am_freadFromto2 = freadFromto2;
	data->am_freadOHTSpec = freadOHTSpec;
	data->am_freadControl = freadControl;
	data->am_freadBatcharge = freadBatcharge;
	((ProcSystem*)data->$sys)->snapFunctionPtr = model_snap;
	((ProcSystem*)data->$sys)->modelFinishedPtr = model_finished;
	data->am_fDistanceMatrix$func->dispatch = dispatch_fDistanceMatrix;
	data->am_fDistanceMatrix$func->func = fDistanceMatrix;
	data->am_fsetValuable_FilePtr$func->dispatch = dispatch_fsetValuable_FilePtr;
	data->am_fsetValuable_FilePtr$func->func = fsetValuable_FilePtr;
	data->am_freadFromto$func->dispatch = dispatch_freadFromto;
	data->am_freadFromto$func->func = freadFromto;
	data->am_freadFromto2$func->dispatch = dispatch_freadFromto2;
	data->am_freadFromto2$func->func = freadFromto2;
	data->am_freadOHTSpec$func->dispatch = dispatch_freadOHTSpec;
	data->am_freadOHTSpec$func->func = freadOHTSpec;
	data->am_freadControl$func->dispatch = dispatch_freadControl;
	data->am_freadControl$func->func = freadControl;
	data->am_freadBatcharge$func->dispatch = dispatch_freadBatcharge;
	data->am_freadBatcharge$func->func = freadBatcharge;
}

