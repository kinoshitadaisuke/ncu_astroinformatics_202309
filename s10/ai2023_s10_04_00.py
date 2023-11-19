#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/19 15:23:06 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# URL of data file
url_data = 'http://ned.ipac.caltech.edu/Archive/Distances/' \
    + 'NED30.5.1-D-17.1.2-20200415.csv'

# output file name
file_output = 'ned1d.csv'

# printing status
print (f'Now, fetching {url_data}...')

# opening URL
with urllib.request.urlopen (url_data) as fh_read:
    # reading data
    data_byte = fh_read.read ()

# printing status
print (f'Finished fetching {url_data}!')

# printing status
print (f'Now, writing data into file "{file_output}"...')

# opening file for writing
with open (file_output, 'wb') as fh_write:
    # writing data
    fh_write.write (data_byte)

# printing status
print (f'Finished writing data into file "{file_output}"!')
