// logic.c
// AutoMod 12.6.1 Generated File
// Build: 12.6.1.12
// Model name:	model
// Model path:	D:\Project\5. ECO OHT\models\240807~\240813 P1 3F_Eco OHT_OO%NOHID_Algorithm_cp tuning_Layout\model.dir\
// Generated:	Tue Aug 13 10:53:46 2024
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
pCreate_arriving(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("logic.m", "Arriving procedure", "model.pCreate", localactor);
	AMDebuggerParams("model.pCreate", pCreate_arriving, localactor, 0, NULL, NULL, NULL);
	{
		{
			AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 3);
			am2_i = 1;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 4);
			this->attribute->am2_aiLoadMakeID = 1;
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 6);
			am2_i = 1;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 7);
			while (am2_i <= 1) {
				{
					AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 9);
					this->attribute->am2_anRoute = 0;
					EntityChanged(0x00000040);
				}
				{
					AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 10);
					while (this->attribute->am2_anRoute < am2_vnRoute) {
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 13);
							this->attribute->am2_anRoute += 1;
							EntityChanged(0x00000040);
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 14);
							am2_vNum += 1;
							EntityChanged(0x01000000);
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 16);
							if (am2_vNum <= am2_vnRoute) {
								{
									AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 18);
									this->attribute->am2_anFromtoType = 1;
									EntityChanged(0x00000040);
								}
								{
									AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 19);
									clone(this, 1, am2_pMakeRoute, am2_lFOUP);
								}
							}
							else {
								AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 22);
								if (am2_vNum <= (am2_vnRoute * 2 - 1)) {
									{
										AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 24);
										this->attribute->am2_anFromtoType = 2;
										EntityChanged(0x00000040);
									}
									{
										AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 25);
										clone(this, 1, am2_pMakeRoute, am2_lFOUP);
									}
								}
								else {
									AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 27);
									if (am2_vNum <= (am2_vnRoute * 3 - 1)) {
										{
											AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 29);
											this->attribute->am2_anFromtoType = 3;
											EntityChanged(0x00000040);
										}
										{
											AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 30);
											clone(this, 1, am2_pMakeRoute, am2_lFOUP);
										}
									}
								}
							}
						}
					}
				}
				{
					AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 34);
					am2_i += 1;
					EntityChanged(0x01000000);
				}
			}
		}
		{
			AMDebugger("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor, 36);
			{
				int32 pArg1 = am2_i;

				message("%d", pArg1);
			}
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("logic.m", "Arriving procedure", "model.pCreate", pCreate_arriving, localactor);
	return retval;
} /* end of pCreate_arriving */

static int32
pMakeRoute_arriving(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("logic.m", "Arriving procedure", "model.pMakeRoute", localactor);
	AMDebuggerParams("model.pMakeRoute", pMakeRoute_arriving, localactor, 0, NULL, NULL, NULL);
	switch (step) { /* Make the step switcher */
	case Step 1: goto Label1;
	case Step 2: goto Label2;
	case Step 3: goto Label3;
	case Step 4: goto Label4;
	case Step 5: goto Label5;
	case Step 6: goto Label6;
	default: message("Bad step number %ld.", step);
	}
	retval = Error;
	goto LabelRet;
Label1: ;  /* Step1 */
	{
		{
			AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 40);
			this->attribute->am2_alocFrom = str2Location(am2_vroute_FromLoc[ValidIndex("am_model.am_vroute_FromLoc", this->attribute->am2_anFromtoType, 3)][ValidIndex("am_model.am_vroute_FromLoc", this->attribute->am2_anRoute, 99999)]);
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 41);
			this->attribute->am2_alocTo = str2Location(am2_vroute_ToLoc[ValidIndex("am_model.am_vroute_ToLoc", this->attribute->am2_anFromtoType, 3)][ValidIndex("am_model.am_vroute_ToLoc", this->attribute->am2_anRoute, 99999)]);
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 43);
			if (waitfor(ToModelTime(uniform1(am2_stream0, am2_vroute_Interval[ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anFromtoType, 3)][ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anRoute, 99999)] / 2, am2_vroute_Interval[ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anFromtoType, 3)][ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anRoute, 99999)] / 2), UNITSECONDS), this, pMakeRoute_arriving, Step 2, am_localargs) == Delayed)
				return Delayed;
Label2: ; // Step 2
		}
		{
			AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 44);
			am2_o = 0;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 45);
			while (1 == 1) {
				{
					AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 47);
					if (am2_o == 0) {
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 49);
							this->attribute->am2_arTimeGap = FromModelTime(this->attribute->am2_atInitialCreated, UNITSECONDS);
							EntityChanged(0x00000040);
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 50);
							clone(this, 1, am2_pMove, NULL);
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 51);
							if (waitfor(ToModelTime(am2_vroute_Interval[ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anFromtoType, 3)][ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anRoute, 99999)] - this->attribute->am2_arTimeGap, UNITSECONDS), this, pMakeRoute_arriving, Step 3, am_localargs) == Delayed)
								return Delayed;
Label3: ; // Step 3
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 52);
							this->attribute->am2_atAfterTimeGap = ASIclock;
							EntityChanged(0x00000040);
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 53);
							if (waitfor(ToModelTime(uniform1(am2_stream0, am2_vroute_Interval[ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anFromtoType, 3)][ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anRoute, 99999)] / 2, am2_vroute_Interval[ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anFromtoType, 3)][ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anRoute, 99999)] / 2), UNITSECONDS), this, pMakeRoute_arriving, Step 4, am_localargs) == Delayed)
								return Delayed;
Label4: ; // Step 4
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 54);
							am2_o += 1;
							EntityChanged(0x01000000);
						}
					}
				}
				{
					AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 57);
					if (am2_o != 0) {
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 59);
							this->attribute->am2_atCreate = ASIclock;
							EntityChanged(0x00000040);
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 60);
							this->attribute->am2_arTimeGap = FromModelTime(this->attribute->am2_atCreate - this->attribute->am2_atAfterTimeGap, UNITSECONDS);
							EntityChanged(0x00000040);
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 61);
							clone(this, 1, am2_pMove, NULL);
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 62);
							if (waitfor(ToModelTime(am2_vroute_Interval[ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anFromtoType, 3)][ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anRoute, 99999)] - this->attribute->am2_arTimeGap, UNITSECONDS), this, pMakeRoute_arriving, Step 5, am_localargs) == Delayed)
								return Delayed;
Label5: ; // Step 5
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 63);
							this->attribute->am2_atAfterTimeGap = ASIclock;
							EntityChanged(0x00000040);
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 64);
							if (waitfor(ToModelTime(uniform1(am2_stream0, am2_vroute_Interval[ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anFromtoType, 3)][ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anRoute, 99999)] / 2, am2_vroute_Interval[ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anFromtoType, 3)][ValidIndex("am_model.am_vroute_Interval", this->attribute->am2_anRoute, 99999)] / 2), UNITSECONDS), this, pMakeRoute_arriving, Step 6, am_localargs) == Delayed)
								return Delayed;
Label6: ; // Step 6
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor, 65);
							am2_o += 1;
							EntityChanged(0x01000000);
						}
					}
				}
			}
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("logic.m", "Arriving procedure", "model.pMakeRoute", pMakeRoute_arriving, localactor);
	return retval;
} /* end of pMakeRoute_arriving */


typedef struct {
	double freq;
	int32 value;
} Oneof0;

static Oneof0 List0[] = {
	{ 1, 1},
	{ 2, 2}
};

static int32
oneofFunc0(load* this)
{
	int ind = 0;
	Oneof0* list = List0;
	double sample = getdrand(am2_stream0) * 2;

	tprintf(tfp, "In oneof\n");
	while (list->freq < sample) {
		ind++;
		list++;
	}
	return List0[ind].value;
}

static int32
pCreate2_arriving(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("logic.m", "Arriving procedure", "model.pCreate2", localactor);
	AMDebuggerParams("model.pCreate2", pCreate2_arriving, localactor, 0, NULL, NULL, NULL);
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
			AMDebugger("logic.m", "Arriving procedure", "model.pCreate2", pCreate2_arriving, localactor, 71);
			while (1 == 1) {
				{
					AMDebugger("logic.m", "Arriving procedure", "model.pCreate2", pCreate2_arriving, localactor, 74);
					if (waitfor(ToModelTime(3.6000000000000001 / am2_vrCapa, UNITSECONDS), this, pCreate2_arriving, Step 2, am_localargs) == Delayed)
						return Delayed;
Label2: ; // Step 2
				}
				{
					AMDebugger("logic.m", "Arriving procedure", "model.pCreate2", pCreate2_arriving, localactor, 75);
					am2_i = oneofFunc0(this);
					EntityChanged(0x01000000);
				}
				{
					AMDebugger("logic.m", "Arriving procedure", "model.pCreate2", pCreate2_arriving, localactor, 76);
					if (am2_i == 1) {
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pCreate2", pCreate2_arriving, localactor, 78);
							this->attribute->am2_alocFrom = ListIndexItem(LocationList, am2_vllpurple, 1 + Size(List, LocationList, am2_vllpurple) * uniform1(am2_stream0, 0.50000000000000000, 0.50000000000000000));
							EntityChanged(0x00000040);
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pCreate2", pCreate2_arriving, localactor, 79);
							this->attribute->am2_alocTo = ListIndexItem(LocationList, am2_vllInherit, 1 + Size(List, LocationList, am2_vllInherit) * uniform1(am2_stream0, 0.50000000000000000, 0.50000000000000000));
							EntityChanged(0x00000040);
						}
					}
					else {
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pCreate2", pCreate2_arriving, localactor, 83);
							this->attribute->am2_alocFrom = ListIndexItem(LocationList, am2_vllInherit, 1 + Size(List, LocationList, am2_vllInherit) * uniform1(am2_stream0, 0.50000000000000000, 0.50000000000000000));
							EntityChanged(0x00000040);
						}
						{
							AMDebugger("logic.m", "Arriving procedure", "model.pCreate2", pCreate2_arriving, localactor, 84);
							this->attribute->am2_alocTo = ListIndexItem(LocationList, am2_vllpurple, 1 + Size(List, LocationList, am2_vllpurple) * uniform1(am2_stream0, 0.50000000000000000, 0.50000000000000000));
							EntityChanged(0x00000040);
						}
					}
				}
				{
					AMDebugger("logic.m", "Arriving procedure", "model.pCreate2", pCreate2_arriving, localactor, 86);
					clone(this, 1, am2_pMove, NULL);
				}
				{
					AMDebugger("logic.m", "Arriving procedure", "model.pCreate2", pCreate2_arriving, localactor, 87);
					am2_vnRequest2 += 1;
					EntityChanged(0x01000000);
				}
			}
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("logic.m", "Arriving procedure", "model.pCreate2", pCreate2_arriving, localactor);
	return retval;
} /* end of pCreate2_arriving */

static int32
pMove_arriving(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("logic.m", "Arriving procedure", "model.pMove", localactor);
	AMDebuggerParams("model.pMove", pMove_arriving, localactor, 0, NULL, NULL, NULL);
	{
		{
			AMDebugger("logic.m", "Arriving procedure", "model.pMove", pMove_arriving, localactor, 102);
			am2_vnRequest += 1;
			EntityChanged(0x01000000);
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("logic.m", "Arriving procedure", "model.pMove", pMove_arriving, localactor);
	return retval;
} /* end of pMove_arriving */

static int32
pExit_arriving(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("logic.m", "Arriving procedure", "model.pExit", localactor);
	AMDebuggerParams("model.pExit", pExit_arriving, localactor, 0, NULL, NULL, NULL);
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
			AMDebugger("logic.m", "Arriving procedure", "model.pExit", pExit_arriving, localactor, 130);
			pushppa(this, pExit_arriving, Step 2, am_localargs);
			pushppa(this, inqueue, Step 1, am2_qSpace);
			return Continue; // go move into territory
Label2: ; // Step 2
		}
		{
			AMDebugger("logic.m", "Arriving procedure", "model.pExit", pExit_arriving, localactor, 131);
			this->nextproc = am2_die; /* send to ... */
			EntityChanged(W_LOAD);
			retval = Continue;
			goto LabelRet;
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("logic.m", "Arriving procedure", "model.pExit", pExit_arriving, localactor);
	return retval;
} /* end of pExit_arriving */

static int32
am_sSetFromLocation(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("logic.m", "Subroutine", "model.sSetFromLocation", localactor);
	AMDebuggerParams("model.sSetFromLocation", am_sSetFromLocation, localactor, 0, NULL, NULL, NULL);
	{
		{
			AMDebugger("logic.m", "Subroutine", "model.sSetFromLocation", am_sSetFromLocation, localactor, 136);
			{
				char* pArg1 = "pm:cp_";
				char* pArg2 = am2_vroute_FromLoc[ValidIndex("am_model.am_vroute_FromLoc", this->attribute->am2_anFromtoType, 3)][ValidIndex("am_model.am_vroute_FromLoc", this->attribute->am2_anRoute, 99999)];

				char* am_tmp;
				am_tmp = bufsprintf("%s%s", pArg1, pArg2);
				SetString(&am2_vstrTemp, am_tmp);
				EntityChanged(0x01000000);
			}
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sSetFromLocation", am_sSetFromLocation, localactor, 137);
			{
				int32 pArg1 = am2_vroute_FromBay[ValidIndex("am_model.am_vroute_FromBay", this->attribute->am2_anFromtoType, 2)][ValidIndex("am_model.am_vroute_FromBay", this->attribute->am2_anRoute, 99999)];

				char* am_tmp;
				am_tmp = bufsprintf("%d", pArg1);
				SetString(&am2_vstrTemp2, am_tmp);
				EntityChanged(0x01000000);
			}
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sSetFromLocation", am_sSetFromLocation, localactor, 138);
			this->attribute->am2_alocFrom = str2Location(am2_vstrTemp);
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sSetFromLocation", am_sSetFromLocation, localactor, 139);
			this->attribute->am2_alocFromBay = str2Integer(am2_vstrTemp2);
			EntityChanged(0x00000040);
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("logic.m", "Subroutine", "model.sSetFromLocation", am_sSetFromLocation, localactor);
	return retval;
} /* end of am_sSetFromLocation */

static int32
am_sSetToLocation(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("logic.m", "Subroutine", "model.sSetToLocation", localactor);
	AMDebuggerParams("model.sSetToLocation", am_sSetToLocation, localactor, 0, NULL, NULL, NULL);
	{
		{
			AMDebugger("logic.m", "Subroutine", "model.sSetToLocation", am_sSetToLocation, localactor, 143);
			{
				char* pArg1 = "pm:cp_";
				char* pArg2 = am2_vroute_ToLoc[ValidIndex("am_model.am_vroute_ToLoc", this->attribute->am2_anFromtoType, 3)][ValidIndex("am_model.am_vroute_ToLoc", this->attribute->am2_anRoute, 99999)];

				char* am_tmp;
				am_tmp = bufsprintf("%s%s", pArg1, pArg2);
				SetString(&am2_vstrTemp, am_tmp);
				EntityChanged(0x01000000);
			}
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sSetToLocation", am_sSetToLocation, localactor, 144);
			{
				int32 pArg1 = am2_vroute_ToBay[ValidIndex("am_model.am_vroute_ToBay", this->attribute->am2_anFromtoType, 2)][ValidIndex("am_model.am_vroute_ToBay", this->attribute->am2_anRoute, 99999)];

				char* am_tmp;
				am_tmp = bufsprintf("%d", pArg1);
				SetString(&am2_vstrTemp2, am_tmp);
				EntityChanged(0x01000000);
			}
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sSetToLocation", am_sSetToLocation, localactor, 145);
			this->attribute->am2_alocTo = str2Location(am2_vstrTemp);
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sSetToLocation", am_sSetToLocation, localactor, 146);
			this->attribute->am2_alocToBay = str2Integer(am2_vstrTemp2);
			EntityChanged(0x00000040);
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("logic.m", "Subroutine", "model.sSetToLocation", am_sSetToLocation, localactor);
	return retval;
} /* end of am_sSetToLocation */

static int32
am_sSetUnloadLoad(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("logic.m", "Subroutine", "model.sSetUnloadLoad", localactor);
	AMDebuggerParams("model.sSetUnloadLoad", am_sSetUnloadLoad, localactor, 0, NULL, NULL, NULL);
	{
		{
			AMDebugger("logic.m", "Subroutine", "model.sSetUnloadLoad", am_sSetUnloadLoad, localactor, 150);
			this->attribute->am2_aPickup = am2_vroute_Pickup[ValidIndex("am_model.am_vroute_Pickup", this->attribute->am2_anFromtoType, 2)][ValidIndex("am_model.am_vroute_Pickup", this->attribute->am2_anRoute, 99999)];
			EntityChanged(0x00000040);
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sSetUnloadLoad", am_sSetUnloadLoad, localactor, 151);
			this->attribute->am2_aSetdown = am2_vroute_Setdown[ValidIndex("am_model.am_vroute_Setdown", this->attribute->am2_anFromtoType, 2)][ValidIndex("am_model.am_vroute_Setdown", this->attribute->am2_anRoute, 99999)];
			EntityChanged(0x00000040);
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("logic.m", "Subroutine", "model.sSetUnloadLoad", am_sSetUnloadLoad, localactor);
	return retval;
} /* end of am_sSetUnloadLoad */

static int32
am_sReport(load* this, int32 step, void* args)
{
	void* am_localargs = NULL;
	load* localactor = this;
	int32 retval = Continue;
	AMDebuggerBeginRoutine("logic.m", "Subroutine", "model.sReport", localactor);
	AMDebuggerParams("model.sReport", am_sReport, localactor, 0, NULL, NULL, NULL);
	{
		{
			AMDebugger("logic.m", "Subroutine", "model.sReport", am_sReport, localactor, 156);
			tabulate(am2_tDelDistance, FromModelDistance(this->attribute->am2_aDelDistance, UNITMILLIMETERS));	// Tabulate the value
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sReport", am_sReport, localactor, 157);
			tabulate(am2_tRetDistance, FromModelDistance(this->attribute->am2_aRetDistance, UNITMILLIMETERS));	// Tabulate the value
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sReport", am_sReport, localactor, 158);
			tabulate(am2_tTotDistance, FromModelDistance(this->attribute->am2_aTotDistance, UNITMILLIMETERS));	// Tabulate the value
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sReport", am_sReport, localactor, 161);
			tabulate(am2_tAssignInit, FromModelTime(this->attribute->am2_atAssignInit - this->attribute->am2_atTR, UNITSECONDS));	// Tabulate the value
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sReport", am_sReport, localactor, 162);
			tabulate(am2_tAssign, FromModelTime(this->attribute->am2_atAssign - this->attribute->am2_atTR, UNITSECONDS));	// Tabulate the value
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sReport", am_sReport, localactor, 163);
			tabulate(am2_tUnloadMove, FromModelTime(this->attribute->am2_atUnload - this->attribute->am2_atAssign, UNITSECONDS));	// Tabulate the value
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sReport", am_sReport, localactor, 164);
			tabulate(am2_tLoadMove, FromModelTime(this->attribute->am2_atLoad - this->attribute->am2_atUnload, UNITSECONDS));	// Tabulate the value
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sReport", am_sReport, localactor, 166);
			am2_vnComplete += 1;
			EntityChanged(0x01000000);
		}
		{
			AMDebugger("logic.m", "Subroutine", "model.sReport", am_sReport, localactor, 167);
			if (this->attribute->am2_atLoad - this->attribute->am2_atTR > ToModelTime(5, UNITMINUTES)) {
				AMDebugger("logic.m", "Subroutine", "model.sReport", am_sReport, localactor, 168);
				am2_vnDelay += 1;
				EntityChanged(0x01000000);
			}
		}
	}
LabelRet: ;
	if (am_localargs)
		xfree(am_localargs);
	AMDebuggerEndRoutine("logic.m", "Subroutine", "model.sReport", am_sReport, localactor);
	return retval;
} /* end of am_sReport */



/* init function for logic.m */
void
model_logic_init(struct model_struct* data)
{
	data->am_pCreate->aprc = pCreate_arriving;
	data->am_pMakeRoute->aprc = pMakeRoute_arriving;
	data->am_pCreate2->aprc = pCreate2_arriving;
	data->am_pMove->aprc = pMove_arriving;
	data->am_pExit->aprc = pExit_arriving;
	data->am_sSetFromLocation = am_sSetFromLocation;
	data->am_sSetToLocation = am_sSetToLocation;
	data->am_sSetUnloadLoad = am_sSetUnloadLoad;
	data->am_sReport = am_sReport;
}

