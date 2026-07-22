// model~model.c
// AutoMod 12.6.1 Generated File
// Build: 12.6.1.12
// Model name:	model
// Model path:	D:\Project\5. ECO OHT\models\240807~\240813 P1 3F_Eco OHT_OO%NOHID_Algorithm_cp tuning_Layout\model.dir\
// Generated:	Tue Aug 13 10:54:13 2024
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


#include "decls.h"

struct model_struct am_model;

char CommandName[] = "C:/AutoModx64/12_6/bin/amod64.exe";
extern ASIWindow WORKMENU;

FILE** imp_stdin;
FILE** imp_stdout;
FILE** imp_stderr;
struct process_system** imp_headpt;
struct AMLoadList* imp_activeloads;
struct model_header** imp_model;
FILE** imp_tfp;
FILE** imp_rfp;
FILE** imp_pfp;
int32* imp_trace;
int32* imp_animate;
int32* imp_Animating;
unsigned long* imp_changeflag;
int32* imp_EnableBeaming;
Time* imp_ASIclock;
Time* imp_beginper;
Boolean* imp_SIMULATOR;
struct AMEventNoticeList** imp_cel;
struct eventlist* imp_fel;
struct dlogItem** imp_grf_sl;
struct s_menu** imp_popmenu;
ASIWindow* imp_WORKMENU;
ASIWindow* imp_SimLotStatusWin;
ASIWindow* imp_SimStnStatusWin;
ASIWindow* imp_SimOperStatusWin;
ASIWindow* imp_SimInvStatusWin;
ASIWindow* imp_SimKanbanStatusWin;

#ifdef __GNUC__
int __attribute__((stdcall)) 
DllEntryPoint(void* hinstDLL, int fdwReason, void* lpvReserved) 
{
	return 1;
}
#endif //__GNUC__


MODELDLLEXPORT
init_globs()
{
	imp_headpt = Getimpheadpt();
	imp_activeloads = Getimpactiveloads();
	imp_model = Getimpmodel();
	imp_tfp = Getimptfp();
	imp_rfp = Getimprfp();
	imp_pfp = Getimppfp();
	imp_trace = Getimptrace();
	imp_animate = Getimpanimate();
	imp_Animating = GetimpAnimating();
	imp_changeflag = Getimpchangeflag();
	imp_EnableBeaming = GetimpEnableBeaming();
	imp_ASIclock = GetimpASIclock();
	imp_beginper = Getimpbeginper();
	imp_SIMULATOR = GetimpSIMULATOR();
	imp_cel = Getimpcel();
	imp_fel = Getimpfel();
	imp_grf_sl = Getimpgrf_sl();
	imp_popmenu = Getimppopmenu();
	imp_WORKMENU = GetimpWORKMENU();
	imp_SimLotStatusWin = GetimpSimLotStatusWin();
	imp_SimStnStatusWin = GetimpSimStnStatusWin();
	imp_SimOperStatusWin = GetimpSimOperStatusWin();
	imp_SimInvStatusWin = GetimpSimInvStatusWin();
	imp_SimKanbanStatusWin = GetimpSimKanbanStatusWin();
	imp_stdin = Getimpstdin();
	imp_stdout = Getimpstdout();
	imp_stderr = Getimpstderr();

	initglobs0();
}

MODELDLLEXPORT load*
newattrib(load* this, load* that)
{
	int i0;

	if (!this->attribute)
		this->attribute = (loadatt*)xmalloc(sizeof(loadatt));
	else {
		ListRemoveAllAndFree(LocationList, this->attribute->am_model.am_aRoute_ToLoc);
		ListRemoveAllAndFree(LocationList, this->attribute->am_model.am_aRoute_FromLoc);
		if (this->attribute->am_model.am_asOldstatus)
			xfree(this->attribute->am_model.am_asOldstatus);
	}
	if (that != NULL) {
		*(this->attribute) = *(that->attribute);
		this->attribute->am_model.am_aRoute_ToLoc = NULL;
		ListCopy(LocationList, this->attribute->am_model.am_aRoute_ToLoc, that->attribute->am_model.am_aRoute_ToLoc);
		this->attribute->am_model.am_aRoute_FromLoc = NULL;
		ListCopy(LocationList, this->attribute->am_model.am_aRoute_FromLoc, that->attribute->am_model.am_aRoute_FromLoc);
		if (this->attribute->am_model.am_asOldstatus) {
			this->attribute->am_model.am_asOldstatus = strdup(that->attribute->am_model.am_asOldstatus);
		}
	} else
		memset(this->attribute, 0, sizeof(loadatt));
	return this;
}

MODELDLLEXPORT void*
get_ldatt_address(load* this, int32 index, int32* d)
{
	void* data = NULL;

	switch(index) {
	case 0:
		data = (void*)&this->attribute->am_model.am_anRoute;
		break;
	case 1:
		data = (void*)&this->attribute->am_model.am_atInitialCreated;
		break;
	case 2:
		data = (void*)&this->attribute->am_model.am_arTimeGap;
		break;
	case 3:
		data = (void*)&this->attribute->am_model.am_atAfterTimeGap;
		break;
	case 4:
		data = (void*)&this->attribute->am_model.am_atCreate;
		break;
	case 5:
		data = (void*)&this->attribute->am_model.am_anTransfer;
		break;
	case 6:
		data = (void*)&this->attribute->am_model.am_atTR;
		break;
	case 7:
		data = (void*)&this->attribute->am_model.am_alocFrom;
		break;
	case 8:
		data = (void*)&this->attribute->am_model.am_aDistance;
		break;
	case 9:
		data = (void*)&this->attribute->am_model.am_aRetDistance;
		break;
	case 10:
		data = (void*)&this->attribute->am_model.am_alocStorage;
		break;
	case 11:
		data = (void*)&this->attribute->am_model.am_atLoad;
		break;
	case 12:
		data = (void*)&this->attribute->am_model.am_aDelDistance;
		break;
	case 13:
		data = (void*)&this->attribute->am_model.am_aTotDistance;
		break;
	case 14:
		data = (void*)&this->attribute->am_model.am_alocTo;
		break;
	case 15:
		data = (void*)&this->attribute->am_model.am_alocFromBay;
		break;
	case 16:
		data = (void*)&this->attribute->am_model.am_alocToBay;
		break;
	case 17:
		data = (void*)&this->attribute->am_model.am_atAssign;
		break;
	case 18:
		data = (void*)&this->attribute->am_model.am_atUnload;
		break;
	case 19:
		data = (void*)&this->attribute->am_model.am_aID;
		break;
	case 20:
		data = (void*)&this->attribute->am_model.am_aAssign;
		break;
	case 21:
		data = (void*)&this->attribute->am_model.am_aParkBay;
		break;
	case 22:
		data = (void*)&this->attribute->am_model.am_avDispatch;
		break;
	case 23:
		data = (void*)&this->attribute->am_model.am_aRoute_ToLoc;
		break;
	case 24:
		data = (void*)&this->attribute->am_model.am_aRoute_FromLoc;
		break;
	case 25:
		data = (void*)&this->attribute->am_model.am_anFromtoType;
		break;
	case 26:
		data = (void*)&this->attribute->am_model.am_alocPark;
		break;
	case 27:
		data = (void*)&this->attribute->am_model.am_atAssignInit;
		break;
	case 28:
		data = (void*)&this->attribute->am_model.am_aiSTKTL[d[0]];
		break;
	case 29:
		data = (void*)&this->attribute->am_model.am_aPickup;
		break;
	case 30:
		data = (void*)&this->attribute->am_model.am_aSetdown;
		break;
	case 31:
		data = (void*)&this->attribute->am_model.am_atcheck;
		break;
	case 32:
		data = (void*)&this->attribute->am_model.am_atLoad2;
		break;
	case 33:
		data = (void*)&this->attribute->am_model.am_A_cgStopDelay;
		break;
	case 34:
		data = (void*)&this->attribute->am_model.am_A_cgStopOccur;
		break;
	case 35:
		data = (void*)&this->attribute->am_model.am_A_cgStopTotalDelay;
		break;
	case 36:
		data = (void*)&this->attribute->am_model.am_A_cgStopVeh;
		break;
	case 37:
		data = (void*)&this->attribute->am_model.am_atBattery;
		break;
	case 38:
		data = (void*)&this->attribute->am_model.am_atOldtime;
		break;
	case 39:
		data = (void*)&this->attribute->am_model.am_arOldaccel;
		break;
	case 40:
		data = (void*)&this->attribute->am_model.am_arOldvelocity;
		break;
	case 41:
		data = (void*)&this->attribute->am_model.am_aiIndex;
		break;
	case 42:
		data = (void*)&this->attribute->am_model.am_aiRecharge;
		break;
	case 43:
		data = (void*)&this->attribute->am_model.am_aiChargeIndex;
		break;
	case 44:
		data = (void*)&this->attribute->am_model.am_acOldpathcolor;
		break;
	case 45:
		data = (void*)&this->attribute->am_model.am_arAddBattery;
		break;
	case 46:
		data = (void*)&this->attribute->am_model.am_asOldstatus;
		break;
	case 47:
		data = (void*)&this->attribute->am_model.am_atChargetime;
		break;
	case 48:
		data = (void*)&this->attribute->am_model.am_aiRouteChange;
		break;
	case 49:
		data = (void*)&this->attribute->am_model.am_atRedIn;
		break;
	case 50:
		data = (void*)&this->attribute->am_model.am_atBatteryRedIn;
		break;
	case 51:
		data = (void*)&this->attribute->am_model.am_atBalckIn;
		break;
	case 52:
		data = (void*)&this->attribute->am_model.am_atBatteryBlackIn;
		break;
	case 53:
		data = (void*)&this->attribute->am_model.am_atBlackIn;
		break;
	case 54:
		data = (void*)&this->attribute->am_model.am_atBatteryRedkIn;
		break;
	case 55:
		data = (void*)&this->attribute->am_model.am_atBattery_Del;
		break;
	case 56:
		data = (void*)&this->attribute->am_model.am_atBattery_Ret;
		break;
	case 57:
		data = (void*)&this->attribute->am_model.am_atBattery_Idle;
		break;
	case 58:
		data = (void*)&this->attribute->am_model.am_aiLoadMakeID;
		break;
	case 59:
		data = (void*)&this->attribute->am_model.am_atNoHID_Start;
		break;
	case 60:
		data = (void*)&this->attribute->am_model.am_aiPathSearched;
		break;
	case 61:
		data = (void*)&this->attribute->am_model.am_aiCheck;
		break;
	case 62:
		data = (void*)&this->attribute->am_model.am_aiUnder50;
		break;
	case 63:
		data = (void*)&this->attribute->am_model.am_atRedStart;
		break;
	}
	return data;
}

MODELDLLEXPORT void
set_attdata(load* this)
{
	attribute* att;

	am_model.am_anRoute$att->data = (void*)&this->attribute->am_model.am_anRoute;
	am_model.am_atInitialCreated$att->data = (void*)&this->attribute->am_model.am_atInitialCreated;
	am_model.am_arTimeGap$att->data = (void*)&this->attribute->am_model.am_arTimeGap;
	am_model.am_atAfterTimeGap$att->data = (void*)&this->attribute->am_model.am_atAfterTimeGap;
	am_model.am_atCreate$att->data = (void*)&this->attribute->am_model.am_atCreate;
	am_model.am_anTransfer$att->data = (void*)&this->attribute->am_model.am_anTransfer;
	am_model.am_atTR$att->data = (void*)&this->attribute->am_model.am_atTR;
	am_model.am_alocFrom$att->data = (void*)&this->attribute->am_model.am_alocFrom;
	am_model.am_aDistance$att->data = (void*)&this->attribute->am_model.am_aDistance;
	am_model.am_aRetDistance$att->data = (void*)&this->attribute->am_model.am_aRetDistance;
	am_model.am_alocStorage$att->data = (void*)&this->attribute->am_model.am_alocStorage;
	am_model.am_atLoad$att->data = (void*)&this->attribute->am_model.am_atLoad;
	am_model.am_aDelDistance$att->data = (void*)&this->attribute->am_model.am_aDelDistance;
	am_model.am_aTotDistance$att->data = (void*)&this->attribute->am_model.am_aTotDistance;
	am_model.am_alocTo$att->data = (void*)&this->attribute->am_model.am_alocTo;
	am_model.am_alocFromBay$att->data = (void*)&this->attribute->am_model.am_alocFromBay;
	am_model.am_alocToBay$att->data = (void*)&this->attribute->am_model.am_alocToBay;
	am_model.am_atAssign$att->data = (void*)&this->attribute->am_model.am_atAssign;
	am_model.am_atUnload$att->data = (void*)&this->attribute->am_model.am_atUnload;
	am_model.am_aID$att->data = (void*)&this->attribute->am_model.am_aID;
	am_model.am_aAssign$att->data = (void*)&this->attribute->am_model.am_aAssign;
	am_model.am_aParkBay$att->data = (void*)&this->attribute->am_model.am_aParkBay;
	am_model.am_avDispatch$att->data = (void*)&this->attribute->am_model.am_avDispatch;
	am_model.am_aRoute_ToLoc$att->data = (void*)&this->attribute->am_model.am_aRoute_ToLoc;
	am_model.am_aRoute_FromLoc$att->data = (void*)&this->attribute->am_model.am_aRoute_FromLoc;
	am_model.am_anFromtoType$att->data = (void*)&this->attribute->am_model.am_anFromtoType;
	am_model.am_alocPark$att->data = (void*)&this->attribute->am_model.am_alocPark;
	am_model.am_atAssignInit$att->data = (void*)&this->attribute->am_model.am_atAssignInit;
	am_model.am_aiSTKTL$att->data = (void*)this->attribute->am_model.am_aiSTKTL;
	am_model.am_aPickup$att->data = (void*)&this->attribute->am_model.am_aPickup;
	am_model.am_aSetdown$att->data = (void*)&this->attribute->am_model.am_aSetdown;
	am_model.am_atcheck$att->data = (void*)&this->attribute->am_model.am_atcheck;
	am_model.am_atLoad2$att->data = (void*)&this->attribute->am_model.am_atLoad2;
	am_model.am_A_cgStopDelay$att->data = (void*)&this->attribute->am_model.am_A_cgStopDelay;
	am_model.am_A_cgStopOccur$att->data = (void*)&this->attribute->am_model.am_A_cgStopOccur;
	am_model.am_A_cgStopTotalDelay$att->data = (void*)&this->attribute->am_model.am_A_cgStopTotalDelay;
	am_model.am_A_cgStopVeh$att->data = (void*)&this->attribute->am_model.am_A_cgStopVeh;
	am_model.am_atBattery$att->data = (void*)&this->attribute->am_model.am_atBattery;
	am_model.am_atOldtime$att->data = (void*)&this->attribute->am_model.am_atOldtime;
	am_model.am_arOldaccel$att->data = (void*)&this->attribute->am_model.am_arOldaccel;
	am_model.am_arOldvelocity$att->data = (void*)&this->attribute->am_model.am_arOldvelocity;
	am_model.am_aiIndex$att->data = (void*)&this->attribute->am_model.am_aiIndex;
	am_model.am_aiRecharge$att->data = (void*)&this->attribute->am_model.am_aiRecharge;
	am_model.am_aiChargeIndex$att->data = (void*)&this->attribute->am_model.am_aiChargeIndex;
	am_model.am_acOldpathcolor$att->data = (void*)&this->attribute->am_model.am_acOldpathcolor;
	am_model.am_arAddBattery$att->data = (void*)&this->attribute->am_model.am_arAddBattery;
	am_model.am_asOldstatus$att->data = (void*)&this->attribute->am_model.am_asOldstatus;
	am_model.am_atChargetime$att->data = (void*)&this->attribute->am_model.am_atChargetime;
	am_model.am_aiRouteChange$att->data = (void*)&this->attribute->am_model.am_aiRouteChange;
	am_model.am_atRedIn$att->data = (void*)&this->attribute->am_model.am_atRedIn;
	am_model.am_atBatteryRedIn$att->data = (void*)&this->attribute->am_model.am_atBatteryRedIn;
	am_model.am_atBalckIn$att->data = (void*)&this->attribute->am_model.am_atBalckIn;
	am_model.am_atBatteryBlackIn$att->data = (void*)&this->attribute->am_model.am_atBatteryBlackIn;
	am_model.am_atBlackIn$att->data = (void*)&this->attribute->am_model.am_atBlackIn;
	am_model.am_atBatteryRedkIn$att->data = (void*)&this->attribute->am_model.am_atBatteryRedkIn;
	am_model.am_atBattery_Del$att->data = (void*)&this->attribute->am_model.am_atBattery_Del;
	am_model.am_atBattery_Ret$att->data = (void*)&this->attribute->am_model.am_atBattery_Ret;
	am_model.am_atBattery_Idle$att->data = (void*)&this->attribute->am_model.am_atBattery_Idle;
	am_model.am_aiLoadMakeID$att->data = (void*)&this->attribute->am_model.am_aiLoadMakeID;
	am_model.am_atNoHID_Start$att->data = (void*)&this->attribute->am_model.am_atNoHID_Start;
	am_model.am_aiPathSearched$att->data = (void*)&this->attribute->am_model.am_aiPathSearched;
	am_model.am_aiCheck$att->data = (void*)&this->attribute->am_model.am_aiCheck;
	am_model.am_aiUnder50$att->data = (void*)&this->attribute->am_model.am_aiUnder50;
	am_model.am_atRedStart$att->data = (void*)&this->attribute->am_model.am_atRedStart;
}

char*
Acceleration_valstrfunc(void* data)
{
	Acceleration* valptr = (Acceleration*)data;

	return acceleration2str(*valptr);
}

Acceleration
Acceleration_strvalfunc(char* data)
{
	return str2Acceleration(data);
}

char*
BlockPtr_valstrfunc(void* data)
{
	block** valptr = (block**)data;

	return actorname(*valptr);
}

block*
BlockPtr_strvalfunc(char* data)
{
	return str2BlockPtr(data);
}

char*
BlockList_valstrfunc(void* data)
{
	AMBlockList** valptr = (AMBlockList**)data;

	return AMBlockListToStr(*valptr);
}

char*
Color_valstrfunc(void* data)
{
	ASI_Color* valptr = (ASI_Color*)data;

	return color2str(*valptr);
}

ASI_Color
Color_strvalfunc(char* data)
{
	return str2Color(data);
}

char*
ContainerPtr_valstrfunc(void* data)
{
	Container** valptr = (Container**)data;

	return actorname(*valptr);
}

Container*
ContainerPtr_strvalfunc(char* data)
{
	return str2ContainerPtr(data);
}

char*
ContainerList_valstrfunc(void* data)
{
	AMContainerList** valptr = (AMContainerList**)data;

	return AMContainerListToStr(*valptr);
}

char*
CounterPtr_valstrfunc(void* data)
{
	counter** valptr = (counter**)data;

	return actorname(*valptr);
}

counter*
CounterPtr_strvalfunc(char* data)
{
	return str2CounterPtr(data);
}

char*
Distance_valstrfunc(void* data)
{
	Distance* valptr = (Distance*)data;

	return distance2str(*valptr);
}

Distance
Distance_strvalfunc(char* data)
{
	return str2Distance(data);
}

char*
FilePtr_valstrfunc(void* data)
{
	iofile** valptr = (iofile**)data;

	return iofile2str(*valptr);
}

iofile*
FilePtr_strvalfunc(char* data)
{
	return str2FilePtr(data);
}

char*
GraphPtr_valstrfunc(void* data)
{
	bgraph** valptr = (bgraph**)data;

	return actorname(*valptr);
}

bgraph*
GraphPtr_strvalfunc(char* data)
{
	return str2GraphPtr(data);
}

char*
Integer_valstrfunc(void* data)
{
	int32* valptr = (int32*)data;

	return int2str(*valptr);
}

int32
Integer_strvalfunc(char* data)
{
	return str2Integer(data);
}

char*
LabelPtr_valstrfunc(void* data)
{
	label** valptr = (label**)data;

	return actorname(*valptr);
}

label*
LabelPtr_strvalfunc(char* data)
{
	return str2LabelPtr(data);
}

char*
LoadPtr_valstrfunc(void* data)
{
	load** valptr = (load**)data;

	return actorname(*valptr);
}

load*
LoadPtr_strvalfunc(char* data)
{
	return str2LoadPtr(data);
}

char*
LoadList_valstrfunc(void* data)
{
	AMLoadList** valptr = (AMLoadList**)data;

	return AMLoadListToStr(*valptr);
}

char*
LoadTypePtr_valstrfunc(void* data)
{
	loadtype** valptr = (loadtype**)data;

	return actorname(*valptr);
}

loadtype*
LoadTypePtr_strvalfunc(char* data)
{
	return str2LoadTypePtr(data);
}

char*
Location_valstrfunc(void* data)
{
	simloc** valptr = (simloc**)data;

	return simlocname(*valptr);
}

simloc*
Location_strvalfunc(char* data)
{
	return str2Location(data);
}

char*
LocationList_valstrfunc(void* data)
{
	AMLocationList** valptr = (AMLocationList**)data;

	return AMLocationListToStr(*valptr);
}

char*
LocationTypePtr_valstrfunc(void* data)
{
	LocationType** valptr = (LocationType**)data;

	return actorname(*valptr);
}

LocationType*
LocationTypePtr_strvalfunc(char* data)
{
	return str2LocationTypePtr(data);
}

char*
LocationTypeList_valstrfunc(void* data)
{
	AMLocationTypeList** valptr = (AMLocationTypeList**)data;

	return AMLocationTypeListToStr(*valptr);
}

char*
MonitorPtr_valstrfunc(void* data)
{
	State_machine** valptr = (State_machine**)data;

	return actorname(*valptr);
}

State_machine*
MonitorPtr_strvalfunc(char* data)
{
	return str2MonitorPtr(data);
}

char*
MotorPtr_valstrfunc(void* data)
{
	ConvMotor** valptr = (ConvMotor**)data;

	return actorname(*valptr);
}

ConvMotor*
MotorPtr_strvalfunc(char* data)
{
	return str2MotorPtr(data);
}

char*
MotorList_valstrfunc(void* data)
{
	AMConvMotorList** valptr = (AMConvMotorList**)data;

	return AMConvMotorListToStr(*valptr);
}

char*
MotorTypePtr_valstrfunc(void* data)
{
	MotorType** valptr = (MotorType**)data;

	return actorname(*valptr);
}

MotorType*
MotorTypePtr_strvalfunc(char* data)
{
	return str2MotorTypePtr(data);
}

char*
MotorTypeList_valstrfunc(void* data)
{
	AMMotorTypeList** valptr = (AMMotorTypeList**)data;

	return AMMotorTypeListToStr(*valptr);
}

char*
OrderListPtr_valstrfunc(void* data)
{
	ordlist** valptr = (ordlist**)data;

	return actorname(*valptr);
}

ordlist*
OrderListPtr_strvalfunc(char* data)
{
	return str2OrderListPtr(data);
}

char*
PathPtr_valstrfunc(void* data)
{
	Path** valptr = (Path**)data;

	return actorname(*valptr);
}

Path*
PathPtr_strvalfunc(char* data)
{
	return str2PathPtr(data);
}

char*
PathList_valstrfunc(void* data)
{
	AMPathList** valptr = (AMPathList**)data;

	return AMPathListToStr(*valptr);
}

char*
PathTypePtr_valstrfunc(void* data)
{
	AgvPathType** valptr = (AgvPathType**)data;

	return actorname(*valptr);
}

AgvPathType*
PathTypePtr_strvalfunc(char* data)
{
	return str2PathTypePtr(data);
}

char*
PathTypeList_valstrfunc(void* data)
{
	AMAgvPathTypeList** valptr = (AMAgvPathTypeList**)data;

	return AMAgvPathTypeListToStr(*valptr);
}

char*
PhotoeyePtr_valstrfunc(void* data)
{
	Photoeye** valptr = (Photoeye**)data;

	return actorname(*valptr);
}

Photoeye*
PhotoeyePtr_strvalfunc(char* data)
{
	return str2PhotoeyePtr(data);
}

char*
PhotoeyeList_valstrfunc(void* data)
{
	AMPhotoList** valptr = (AMPhotoList**)data;

	return AMPhotoListToStr(*valptr);
}

char*
PhotoeyeTypePtr_valstrfunc(void* data)
{
	PhotoeyeType** valptr = (PhotoeyeType**)data;

	return actorname(*valptr);
}

PhotoeyeType*
PhotoeyeTypePtr_strvalfunc(char* data)
{
	return str2PhotoeyeTypePtr(data);
}

char*
PhotoeyeTypeList_valstrfunc(void* data)
{
	AMPhotoeyeTypeList** valptr = (AMPhotoeyeTypeList**)data;

	return AMPhotoeyeTypeListToStr(*valptr);
}

char*
ProcessPtr_valstrfunc(void* data)
{
	process** valptr = (process**)data;

	return actorname(*valptr);
}

process*
ProcessPtr_strvalfunc(char* data)
{
	return str2ProcessPtr(data);
}

char*
QueuePtr_valstrfunc(void* data)
{
	queue** valptr = (queue**)data;

	return actorname(*valptr);
}

queue*
QueuePtr_strvalfunc(char* data)
{
	return str2QueuePtr(data);
}

char*
QueueList_valstrfunc(void* data)
{
	AMQueueList** valptr = (AMQueueList**)data;

	return AMQueueListToStr(*valptr);
}

char*
Rate_valstrfunc(void* data)
{
	Rate* valptr = (Rate*)data;

	return rate2str(*valptr);
}

Rate
Rate_strvalfunc(char* data)
{
	return str2Rate(data);
}

char*
Real_valstrfunc(void* data)
{
	double* valptr = (double*)data;

	return double2str(*valptr);
}

double
Real_strvalfunc(char* data)
{
	return str2Real(data);
}

char*
ResourcePtr_valstrfunc(void* data)
{
	resource** valptr = (resource**)data;

	return actorname(*valptr);
}

resource*
ResourcePtr_strvalfunc(char* data)
{
	return str2ResourcePtr(data);
}

char*
ResourceList_valstrfunc(void* data)
{
	AMResourceList** valptr = (AMResourceList**)data;

	return AMResourceListToStr(*valptr);
}

char*
SchedJobPtr_valstrfunc(void* data)
{
	SchedJob** valptr = (SchedJob**)data;

	return actorname(*valptr);
}

SchedJob*
SchedJobPtr_strvalfunc(char* data)
{
	return str2SchedJobPtr(data);
}

char*
SchedJobList_valstrfunc(void* data)
{
	AMSchedJobList** valptr = (AMSchedJobList**)data;

	return AMSchedJobListToStr(*valptr);
}

char*
SectionPtr_valstrfunc(void* data)
{
	ConvSection** valptr = (ConvSection**)data;

	return actorname(*valptr);
}

ConvSection*
SectionPtr_strvalfunc(char* data)
{
	return str2SectionPtr(data);
}

char*
SectionList_valstrfunc(void* data)
{
	AMConvSectionList** valptr = (AMConvSectionList**)data;

	return AMConvSectionListToStr(*valptr);
}

char*
SectionTypePtr_valstrfunc(void* data)
{
	ConvSectionType** valptr = (ConvSectionType**)data;

	return actorname(*valptr);
}

ConvSectionType*
SectionTypePtr_strvalfunc(char* data)
{
	return str2SectionTypePtr(data);
}

char*
SectionTypeList_valstrfunc(void* data)
{
	AMConvSectionTypeList** valptr = (AMConvSectionTypeList**)data;

	return AMConvSectionTypeListToStr(*valptr);
}

char*
SocketPtr_valstrfunc(void* data)
{
	amSocket** valptr = (amSocket**)data;

	return amsocketname(*valptr);
}

amSocket*
SocketPtr_strvalfunc(char* data)
{
	return str2SocketPtr(data);
}

char*
StatePtr_valstrfunc(void* data)
{
	States** valptr = (States**)data;

	return actorname(*valptr);
}

States*
StatePtr_strvalfunc(char* data)
{
	return str2StatePtr(data);
}

char*
StreamPtr_valstrfunc(void* data)
{
	rnstream** valptr = (rnstream**)data;

	return actorname(*valptr);
}

rnstream*
StreamPtr_strvalfunc(char* data)
{
	return str2StreamPtr(data);
}

char*
String_valstrfunc(void* data)
{
	char** valptr = (char**)data;

	return VALIDSTRING(*valptr);
}

char*
String_strvalfunc(char* data)
{
	return str2String(data);
}

char*
StringList_valstrfunc(void* data)
{
	AMStringList** valptr = (AMStringList**)data;

	return AMStringListToStr(*valptr);
}

char*
SystemPtr_valstrfunc(void* data)
{
	System** valptr = (System**)data;

	return systemname(*valptr);
}

System*
SystemPtr_strvalfunc(char* data)
{
	return str2SystemPtr(data);
}

char*
TablePtr_valstrfunc(void* data)
{
	table** valptr = (table**)data;

	return actorname(*valptr);
}

table*
TablePtr_strvalfunc(char* data)
{
	return str2TablePtr(data);
}

char*
Time_valstrfunc(void* data)
{
	ASITime* valptr = (ASITime*)data;

	return time2str(*valptr);
}

ASITime
Time_strvalfunc(char* data)
{
	return str2Time(data);
}

char*
TransferPtr_valstrfunc(void* data)
{
	ConvTransfer** valptr = (ConvTransfer**)data;

	return actorname(*valptr);
}

ConvTransfer*
TransferPtr_strvalfunc(char* data)
{
	return str2TransferPtr(data);
}

char*
TransferTypePtr_valstrfunc(void* data)
{
	TransferType** valptr = (TransferType**)data;

	return actorname(*valptr);
}

TransferType*
TransferTypePtr_strvalfunc(char* data)
{
	return str2TransferTypePtr(data);
}

char*
VehiclePtr_valstrfunc(void* data)
{
	vehicle** valptr = (vehicle**)data;

	return actorname(*valptr);
}

vehicle*
VehiclePtr_strvalfunc(char* data)
{
	return str2VehiclePtr(data);
}

char*
VehicleList_valstrfunc(void* data)
{
	AMVehicleList** valptr = (AMVehicleList**)data;

	return AMVehicleListToStr(*valptr);
}

char*
VehSegPtr_valstrfunc(void* data)
{
	VehSeg** valptr = (VehSeg**)data;

	return actorname(*valptr);
}

VehSeg*
VehSegPtr_strvalfunc(char* data)
{
	return str2VehSegPtr(data);
}

char*
VehSegList_valstrfunc(void* data)
{
	AMVehSegList** valptr = (AMVehSegList**)data;

	return AMVehSegListToStr(*valptr);
}

char*
Velocity_valstrfunc(void* data)
{
	Velocity* valptr = (Velocity*)data;

	return velocity2str(*valptr);
}

Velocity
Velocity_strvalfunc(char* data)
{
	return str2Velocity(data);
}

ImplementList(_IntegerList, int32, 0);

char*
IntegerList_valstrfunc(void* data)
{
	AM_IntegerList** valptr = (AM_IntegerList**)data;

	return AM_IntegerListToStr(*valptr);
}

ImplementList(_RealList, double, 0.0);

char*
RealList_valstrfunc(void* data)
{
	AM_RealList** valptr = (AM_RealList**)data;

	return AM_RealListToStr(*valptr);
}

ImplementList(_CounterList, counter*, NULL);

char*
CounterList_valstrfunc(void* data)
{
	AM_CounterList** valptr = (AM_CounterList**)data;

	return AM_CounterListToStr(*valptr);
}
