#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time
from GrabFundValue import grabFundValue

if(__name__=='__main__'):
    currentDateString = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    print("当前时间：",currentDateString)
    grabFundValue('160119',currentDateString)
