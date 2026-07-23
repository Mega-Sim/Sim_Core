// user.h
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


#ifndef __USER_H__
#define __USER_H__

#include "amc2.h"

FILE** Getimpstdin();
extern FILE** imp_stdin;
#undef stdin
#define stdin (*imp_stdin)
FILE** Getimpstdout();
extern FILE** imp_stdout;
#undef stdout
#define stdout (*imp_stdout)
FILE** Getimpstderr();
extern FILE** imp_stderr;
#undef stderr
#define stderr (*imp_stderr)
struct process_system** Getimpheadpt();
extern struct process_system** imp_headpt;
#undef headpt
#define headpt (*imp_headpt)
struct AMLoadList* Getimpactiveloads();
extern struct AMLoadList* imp_activeloads;
#undef activeloads
#define activeloads (*imp_activeloads)
struct model_header** Getimpmodel();
extern struct model_header** imp_model;
#undef model
#define model (*imp_model)
FILE** Getimptfp();
extern FILE** imp_tfp;
#undef tfp
#define tfp (*imp_tfp)
FILE** Getimprfp();
extern FILE** imp_rfp;
#undef rfp
#define rfp (*imp_rfp)
FILE** Getimppfp();
extern FILE** imp_pfp;
#undef pfp
#define pfp (*imp_pfp)
int32* Getimptrace();
extern int32* imp_trace;
#undef trace
#define trace (*imp_trace)
int32* Getimpanimate();
extern int32* imp_animate;
#undef animate
#define animate (*imp_animate)
int32* GetimpAnimating();
extern int32* imp_Animating;
#undef Animating
#define Animating (*imp_Animating)
unsigned long* Getimpchangeflag();
extern unsigned long* imp_changeflag;
#undef changeflag
#define changeflag (*imp_changeflag)
int32* GetimpEnableBeaming();
extern int32* imp_EnableBeaming;
#undef EnableBeaming
#define EnableBeaming (*imp_EnableBeaming)
Time* GetimpASIclock();
extern Time* imp_ASIclock;
#undef ASIclock
#define ASIclock (*imp_ASIclock)
Time* Getimpbeginper();
extern Time* imp_beginper;
#undef beginper
#define beginper (*imp_beginper)
Boolean* GetimpSIMULATOR();
extern Boolean* imp_SIMULATOR;
#undef SIMULATOR
#define SIMULATOR (*imp_SIMULATOR)
struct AMEventNoticeList** Getimpcel();
extern struct AMEventNoticeList** imp_cel;
#undef cel
#define cel (*imp_cel)
struct eventlist* Getimpfel();
extern struct eventlist* imp_fel;
#undef fel
#define fel (*imp_fel)
struct dlogItem** Getimpgrf_sl();
extern struct dlogItem** imp_grf_sl;
#undef grf_sl
#define grf_sl (*imp_grf_sl)
struct s_menu** Getimppopmenu();
extern struct s_menu** imp_popmenu;
#undef popmenu
#define popmenu (*imp_popmenu)
ASIWindow* GetimpWORKMENU();
extern ASIWindow* imp_WORKMENU;
#undef WORKMENU
#define WORKMENU (*imp_WORKMENU)
ASIWindow* GetimpSimLotStatusWin();
extern ASIWindow* imp_SimLotStatusWin;
#undef SimLotStatusWin
#define SimLotStatusWin (*imp_SimLotStatusWin)
ASIWindow* GetimpSimStnStatusWin();
extern ASIWindow* imp_SimStnStatusWin;
#undef SimStnStatusWin
#define SimStnStatusWin (*imp_SimStnStatusWin)
ASIWindow* GetimpSimOperStatusWin();
extern ASIWindow* imp_SimOperStatusWin;
#undef SimOperStatusWin
#define SimOperStatusWin (*imp_SimOperStatusWin)
ASIWindow* GetimpSimInvStatusWin();
extern ASIWindow* imp_SimInvStatusWin;
#undef SimInvStatusWin
#define SimInvStatusWin (*imp_SimInvStatusWin)
ASIWindow* GetimpSimKanbanStatusWin();
extern ASIWindow* imp_SimKanbanStatusWin;
#undef SimKanbanStatusWin
#define SimKanbanStatusWin (*imp_SimKanbanStatusWin)
#ifdef VISUALC
#define MODELDLLEXPORT __declspec(dllexport)
#else
#define MODELDLLEXPORT
#endif // VISUALC
DeclareList(_IntegerList, int32,);
#define AM_IntegerListItemCopy(item1, item2) item1 = item2
#define AM_IntegerListItemEqual(item1, item2) (item1 == item2)
#define AM_IntegerListItemRemove(item) /* empty */
#define AM_IntegerListItemToStr(item) int2str(item)
DeclareList(_RealList, double,);
#define AM_RealListItemCopy(item1, item2) item1 = item2
#define AM_RealListItemEqual(item1, item2) (item1 == item2)
#define AM_RealListItemRemove(item) /* empty */
#define AM_RealListItemToStr(item) double2str(item)
DeclareList(_CounterList, counter*,);
#define AM_CounterListItemCopy(item1, item2) item1 = item2
#define AM_CounterListItemEqual(item1, item2) (item1 == item2)
#define AM_CounterListItemRemove(item) /* empty */
#define AM_CounterListItemToStr(item) actorname(item)

typedef struct loadatt {
	struct {
		int32 am_anRoute;	/* anRoute */
		ASITime am_atInitialCreated;	/* atInitialCreated */
		double am_arTimeGap;	/* arTimeGap */
		ASITime am_atAfterTimeGap;	/* atAfterTimeGap */
		ASITime am_atCreate;	/* atCreate */
		int32 am_anTransfer;	/* anTransfer */
		ASITime am_atTR;	/* atTR */
		simloc* am_alocFrom;	/* alocFrom */
		Distance am_aDistance;	/* aDistance */
		Distance am_aRetDistance;	/* aRetDistance */
		simloc* am_alocStorage;	/* alocStorage */
		ASITime am_atLoad;	/* atLoad */
		Distance am_aDelDistance;	/* aDelDistance */
		Distance am_aTotDistance;	/* aTotDistance */
		simloc* am_alocTo;	/* alocTo */
		int32 am_alocFromBay;	/* alocFromBay */
		int32 am_alocToBay;	/* alocToBay */
		ASITime am_atAssign;	/* atAssign */
		ASITime am_atUnload;	/* atUnload */
		int32 am_aID;	/* aID */
		int32 am_aAssign;	/* aAssign */
		int32 am_aParkBay;	/* aParkBay */
		vehicle* am_avDispatch;	/* avDispatch */
		AMLocationList* am_aRoute_ToLoc;	/* aRoute_ToLoc */
		AMLocationList* am_aRoute_FromLoc;	/* aRoute_FromLoc */
		int32 am_anFromtoType;	/* anFromtoType */
		simloc* am_alocPark;	/* alocPark */
		ASITime am_atAssignInit;	/* atAssignInit */
		int32 am_aiSTKTL[3];	/* aiSTKTL */
		double am_aPickup;	/* aPickup */
		double am_aSetdown;	/* aSetdown */
		ASITime am_atcheck;	/* atcheck */
		ASITime am_atLoad2;	/* atLoad2 */
		ASITime am_A_cgStopDelay;	/* A_cgStopDelay */
		int32 am_A_cgStopOccur;	/* A_cgStopOccur */
		ASITime am_A_cgStopTotalDelay;	/* A_cgStopTotalDelay */
		vehicle* am_A_cgStopVeh;	/* A_cgStopVeh */
		double am_atBattery;	/* atBattery */
		ASITime am_atOldtime;	/* atOldtime */
		double am_arOldaccel;	/* arOldaccel */
		double am_arOldvelocity;	/* arOldvelocity */
		int32 am_aiIndex;	/* aiIndex */
		int32 am_aiRecharge;	/* aiRecharge */
		int32 am_aiChargeIndex;	/* aiChargeIndex */
		ASI_Color am_acOldpathcolor;	/* acOldpathcolor */
		double am_arAddBattery;	/* arAddBattery */
		char* am_asOldstatus;	/* asOldstatus */
		ASITime am_atChargetime;	/* atChargetime */
		int32 am_aiRouteChange;	/* aiRouteChange */
		ASITime am_atRedIn;	/* atRedIn */
		ASITime am_atBatteryRedIn;	/* atBatteryRedIn */
		ASITime am_atBalckIn;	/* atBalckIn */
		ASITime am_atBatteryBlackIn;	/* atBatteryBlackIn */
		ASITime am_atBlackIn;	/* atBlackIn */
		ASITime am_atBatteryRedkIn;	/* atBatteryRedkIn */
		ASITime am_atBattery_Del;	/* atBattery_Del */
		ASITime am_atBattery_Ret;	/* atBattery_Ret */
		ASITime am_atBattery_Idle;	/* atBattery_Idle */
		int32 am_aiLoadMakeID;	/* aiLoadMakeID */
		ASITime am_atNoHID_Start;	/* atNoHID_Start */
		int32 am_aiPathSearched;	/* aiPathSearched */
		int32 am_aiCheck;	/* aiCheck */
		int32 am_aiUnder50;	/* aiUnder50 */
		ASITime am_atRedStart;	/* atRedStart */
	} am_model;
} loadatt;

#define ValidIndex(NAME, INDEX, MAXINDEX) validindex(NAME, INDEX, MAXINDEX)
#define ValidPtr(VALUE, KIND, CAST) ((CAST)validptr(VALUE, KIND))

#endif // __USER_H__
