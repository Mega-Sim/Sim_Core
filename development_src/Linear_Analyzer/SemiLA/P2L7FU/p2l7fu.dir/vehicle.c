// vehicle.c
// AutoMod 12.6.1 Generated File
// Build: 12.6.1.12
// Model name:	P2L7FU
// Model path:	C:\Users\Administrator\Desktop\SemiLA_1204_EXE\P2L7FU\P2L7FU.dir\
// Generated:	Thu May 23 10:41:54 2019
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
pm_park(vehicle* am_theVehicle, simloc* am_parkLoc)
{
	AMLocationListItem* am_lv0; // 'for each' loop variable
	AMLocationList* am_ls0 = NULL; // 'for each' list

	{
		{
			if (am2_vVehicleOrTime == 1) {
				{
					if (StringCompare(VehGetType(ValidPtr(am_theVehicle, 81, vehicle*)), "DefVehicle") == 0) {
						{
							if (LocGetDistToLoc(ValidPtr(VehGetCurLoc(ValidPtr(am_theVehicle, 81, vehicle*)), 40, simloc*), ValidPtr(am_parkLoc, 40, simloc*)) > ToModelDistance(50000, UNITMILLIMETERS)) {
								{
									if (LocGetCurConts(ValidPtr(am_parkLoc, 40, simloc*)) > 1) {
										return 0;
									}
								}
								{
									am_ls0 = 0;
									ListCopy(LocationList, am_ls0, am2_vParkListFoup);
									for (am_lv0 = (am_ls0) ? (am_ls0)->first : NULL; am_lv0; am_lv0 = am_lv0->next) {
										am2_vParkLocFoup = am_lv0->item;
										{
											{
												if (LocCompare(am2_vParkLocFoup, am_parkLoc) == 0) {
	ListRemoveAllAndFree(LocationList, am_ls0);
													return 0;
												}
											}
										}
									}
									ListRemoveAllAndFree(LocationList, am_ls0); /* End of for each */
								}
								{
									ListAppendItem(LocationList, am2_vParkListFoup, am_parkLoc);	// append item to end of list
								}
								{
									if (Size(List, LocationList, am2_vParkListFoup) > 1) {
										ListRemoveFirst(LocationList, am2_vParkListFoup);	// remove first item from list
									}
								}
								{
									VehSetColor(ValidPtr(am_theVehicle, 81, vehicle*), 4);
									EntityChanged(0x01000000);
								}
								{
	ListRemoveAllAndFree(LocationList, am_ls0);
									return 1;
								}
							}
						}
						{
	ListRemoveAllAndFree(LocationList, am_ls0);
							return 0;
						}
					}
				}
				{
	ListRemoveAllAndFree(LocationList, am_ls0);
					return 0;
				}
			}
		}
		{
	ListRemoveAllAndFree(LocationList, am_ls0);
			return 0;
		}
	}
LabelRet: ;
} /* end of pm_park */

static int32
pm_work(vehicle* am_theVehicle, simloc* am_loadLoc, load* am_theLoad)
{
	{
		{
			VehSetColor(ValidPtr(am_theVehicle, 81, vehicle*), 1);
			EntityChanged(0x01000000);
		}
		{
			return 1;
		}
	}
LabelRet: ;
} /* end of pm_work */



/* init function for vehicle.m */
void
model_vehicle_init(struct model_struct* data)
{
	((MovementSystem*)data->am_pm.$sys)->srcblock.parkprc = pm_park;
	((MovementSystem*)data->am_pm.$sys)->srcblock.workprc = pm_work;
}

