#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/17 16:24:52 (CST) daisuke>
#

# importing datetime module
import datetime

# current time in UTC
time_now_utc = datetime.datetime.now (tz=datetime.timezone.utc)

# printing result
print (f'current time in UTC = {time_now_utc}')
