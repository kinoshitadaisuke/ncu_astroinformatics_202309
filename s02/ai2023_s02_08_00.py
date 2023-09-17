#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/17 16:36:19 (CST) daisuke>
#

# importing datetime module
import datetime

# time offset from UTC
dt = datetime.timedelta (hours=8)

# current time in local time
time_now_local = datetime.datetime.now (tz=datetime.timezone (dt))

# printing result
print (f'current local time: {time_now_local}')
