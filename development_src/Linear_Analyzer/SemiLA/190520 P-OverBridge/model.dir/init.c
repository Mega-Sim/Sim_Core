// init.c
// AutoMod 12.6.1 Generated File
// Build: 12.6.1.12
// Model name:	model
// Model path:	C:\Users\Administrator\Desktop\SemiLA_1204_EXE\190520 P-OverBridge\model.dir\
// Generated:	Mon May 20 11:09:18 2019
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
model_initialize()
{
	{
		{
			am2_vVehicleOrTime = 0;
			EntityChanged(0x01000000);
		}
		{
			am2_vInitDel_Time = 86400 * 15;
			EntityChanged(0x01000000);
		}
		{
			am2_vOHTDel_Time = 150;
			EntityChanged(0x01000000);
		}
		{
			return 1;
		}
	}
LabelRet: ;
} /* end of model_initialize */



/* init function for init.m */
void
model_init_init(struct model_struct* data)
{
	((ProcSystem*)data->$sys)->modelInitPtr = model_initialize;
}

