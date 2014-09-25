#!/usr/bin/env python

import QSTK.qstkutil.qsdateutil as du
import pandas as pd

import datetime as dt

dt_start = dt.datetime(2013, 1, 1)
dt_end = dt.datetime(2013, 3, 5)
dt_timeofday = dt.timedelta(hours=16)

ldt_timestamps = du.getNextNNYSEdays(dt_start, dt_end, dt_timeofday)

print "Total days: " + len(ldt_timestamps)