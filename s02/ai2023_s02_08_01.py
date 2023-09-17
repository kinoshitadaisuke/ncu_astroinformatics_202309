#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/17 16:36:35 (CST) daisuke>
#

# importing datetime module
import datetime

# time offset from UTC
dt = datetime.timedelta (hours=8)

# current time in local time
time_now_local = datetime.datetime.now (tz=datetime.timezone (dt))

# getting year, month, day, hour, minute, and second
YYYY = time_now_local.year
MM   = time_now_local.month
DD   = time_now_local.day
hh   = time_now_local.hour
mm   = time_now_local.minute
ss   = time_now_local.second + time_now_local.microsecond * 10**-6

# printing current local time
print (f'current local time:')
print (f'  YYYY = {YYYY}')
print (f'  MM   = {MM}')
print (f'  DD   = {DD}')
print (f'  hh   = {hh}')
print (f'  mm   = {mm}')
print (f'  ss   = {ss}')
