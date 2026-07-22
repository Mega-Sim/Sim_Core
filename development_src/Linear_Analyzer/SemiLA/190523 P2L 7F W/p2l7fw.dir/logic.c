// logic.c
// AutoMod 12.6.1 Generated File
// Build: 12.6.1.12
// Model name:	P2L7FW
// Model path:	C:\Users\Administrator\Desktop\SemiLA_1204_EXE\190523 P2L 7F W\P2L7FW.dir\
// Generated:	Thu May 23 10:45:31 2019
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
pStart_arriving(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	int32 retval = Continue;
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
			clone(this, 1, am2_pTimeDel, NULL);
		}
		{
			am2_vfpRead = OpenFilePtr(am_model.$sys, "arc/eqToeq.dat", "r");
		}
		{
			am2_vi = 1;
			EntityChanged(0x01000000);
		}
		{
			while (FileGetEof(ValidPtr(am2_vfpRead, 24, iofile*)) == 0) {
								{
					if (isFileValid(am2_vfpRead, 1)) {
						int rflag;
						static ReadRef st1;

						setupReadRef(&st1, 0, am_model.am_vStrTmp$var, &am2_vStrTmp, NULL, -1, FALSE);
						rflag = readFile(am2_vfpRead->fp, "\n", &st1, NULL);
						SetFileAtEof(am2_vfpRead, EOF, rflag);
					}
				}
								{
					int rflag;
					static ReadRef st1;
					static ReadRef st2;
					static ReadRef st3;

					setupReadRef(&st1, 0, am_model.am_vFromEqsName$var, &am2_vFromEqsName, NULL, -1, FALSE);
					setupReadRef(&st2, 0, am_model.am_vToEqsName$var, &am2_vToEqsName, NULL, -1, FALSE);
					setupReadRef(&st3, 0, am_model.am_vLotPerHour$var, &am2_vLotPerHour, NULL, -1, FALSE);
					rflag = readString(am2_vStrTmp, "\t", &st1, &st2, &st3, NULL);
				}
				{
					if (StrGetIndex(am2_vFromEqsName, "-") <= StrGetLength(am2_vFromEqsName)) {
						SetString(&am2_vFromEqsName, StrSetSubStr(ValidPtr(am2_vFromEqsName, 0, char*), StrGetIndex(am2_vFromEqsName, "-"), 1, "_"));
						EntityChanged(0x01000000);
					}
				}
				{
					if (StrGetIndex(am2_vToEqsName, "-") <= StrGetLength(am2_vToEqsName)) {
						SetString(&am2_vToEqsName, StrSetSubStr(ValidPtr(am2_vToEqsName, 0, char*), StrGetIndex(am2_vToEqsName, "-"), 1, "_"));
						EntityChanged(0x01000000);
					}
				}
				{
					if (StringCompare(StrGetSubStr(am2_vFromEqsName, 1, 1), "*") != 0) {
						{
							{
								char* pArg1 = "pm:cp_";
								char* pArg2 = am2_vFromEqsName;

								char* am_tmp;
								am_tmp = bufsprintf("%s%s", pArg1, pArg2);
								SetString(&am2_vStrTmp, am_tmp);
								EntityChanged(0x01000000);
							}
						}
						{
							this->attribute->am2_lapFromEq = str2Location(am2_vStrTmp);
							EntityChanged(0x00000040);
						}
						{
							{
								char* pArg1 = "pm:cp_";
								char* pArg2 = am2_vToEqsName;

								char* am_tmp;
								am_tmp = bufsprintf("%s%s", pArg1, pArg2);
								SetString(&am2_vStrTmp, am_tmp);
								EntityChanged(0x01000000);
							}
						}
						{
							this->attribute->am2_lapToEq = str2Location(am2_vStrTmp);
							EntityChanged(0x00000040);
						}
						{
							this->attribute->am2_larLotPerHour = am2_vLotPerHour;
							EntityChanged(0x00000040);
						}
						{
							clone(this, 1, am2_pPreFromTo, NULL);
						}
						{
							if (waitfor(ToModelTime(0.10000000000000001, UNITSECONDS), this, pStart_arriving, Step 2, am_localargs) == Delayed)
								return Delayed;
Label2: ; // Step 2
						}
						{
							am2_vi += 1;
							EntityChanged(0x01000000);
						}
					}
					else {
						{
							if (StringCompare(StrGetSubStr(am2_vFromEqsName, 1, 6), "* From") == 0) {
								{
									am2_vFromToCnt = am2_vLotPerHour;
									EntityChanged(0x01000000);
								}
							}
						}
					}
				}
			}
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	return retval;
} /* end of pStart_arriving */

static int32
pPreFromTo_arriving(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	int32 retval = Continue;
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
			if (waitfor(ToModelTime((1 + 86400 * 15.000000000000000 * uniform1(am2_stream0, 0.50000000000000000, 0.50000000000000000)), UNITSECONDS), this, pPreFromTo_arriving, Step 2, am_localargs) == Delayed)
				return Delayed;
Label2: ; // Step 2
		}
		{
			clone(this, 1, am2_pFromTo, NULL);
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	return retval;
} /* end of pPreFromTo_arriving */

static int32
pFromTo_arriving(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	int32 retval = Continue;
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
			while (1 == 1) {
				{
					clone(this, 1, am2_pMove, NULL);
				}
				{
					if (waitfor(ToModelTime(normal1(am2_stream0, 60 * 60 / this->attribute->am2_larLotPerHour, 60 * 60 / (this->attribute->am2_larLotPerHour * 10)), UNITSECONDS), this, pFromTo_arriving, Step 2, am_localargs) == Delayed)
						return Delayed;
Label2: ; // Step 2
				}
			}
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	return retval;
} /* end of pFromTo_arriving */

static int32
pMove_arriving(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	int32 retval = Continue;
	switch (step) { /* Make the step switcher */
	case Step 1: goto Label1;
	case Step 2: goto Label2;
	case Step 3: goto Label3;
	case Step 4: goto Label4;
	case Step 5: goto Label5;
	case Step 6: goto Label6;
	case Step 7: goto Label7;
	default: message("Bad step number %ld.", step);
	}
	retval = Error;
	goto LabelRet;
Label1: ;  /* Step1 */
	{
		{
			if (LocCompare(this->attribute->am2_lapFromEq, NULL) != 0 && LocCompare(this->attribute->am2_lapToEq, NULL) != 0) {
				{
					{
						int result = inccount(am2_cWIP, 1, this, pMove_arriving, Step 2, am_localargs);
						if (result != Continue) return result;
Label2: ;	// Step 2
					}
				}
				{
					if (am2_vVehicleOrTime == 1) {
						{
							pushppa(this, pMove_arriving, Step 3, am_localargs);
							load_SetDestLoc(this, this->attribute->am2_lapFromEq);
							pushppa(this, move_in_loc, Step 1, NULL);
							return Continue; // go move into territory
Label3: ; // Step 3
						}
						{
							pushppa(this, pMove_arriving, Step 4, am_localargs);
							load_SetDestLoc(this, this->attribute->am2_lapToEq);
							pushppa(this, travel_to_loc, Step 1, NULL);
							return Continue; // go move to location
Label4: ; // Step 4
						}
					}
					else {
						{
							return usefor(am2_rOHT, 1, this, pMove_arriving, Step 5, am_localargs, ToModelTime(am2_vOHTDel_Time, UNITSECONDS));
Label5: ; // Step 5
						}
					}
				}
				{
					{
						int result = deccount(am2_cWIP, 1, this, pMove_arriving, Step 6, am_localargs);
						if (result != Continue) return result;
Label6: ;	// Step 6
					}
				}
				{
					pushppa(this, pMove_arriving, Step 7, am_localargs);
					pushppa(this, inqueue, Step 1, am2_qOut);
					return Continue; // go move into territory
Label7: ; // Step 7
				}
			}
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	return retval;
} /* end of pMove_arriving */

static int32
pTimeDel_arriving(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	int32 retval = Continue;
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
			if (waitfor(ToModelTime(am2_vInitDel_Time, UNITSECONDS), this, pTimeDel_arriving, Step 2, am_localargs) == Delayed)
				return Delayed;
Label2: ; // Step 2
		}
		{
			am2_vVehicleOrTime = 1;
			EntityChanged(0x01000000);
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	return retval;
} /* end of pTimeDel_arriving */



/* init function for logic.m */
void
model_logic_init(struct model_struct* data)
{
	data->am_pStart->aprc = pStart_arriving;
	data->am_pPreFromTo->aprc = pPreFromTo_arriving;
	data->am_pFromTo->aprc = pFromTo_arriving;
	data->am_pMove->aprc = pMove_arriving;
	data->am_pTimeDel->aprc = pTimeDel_arriving;
}

