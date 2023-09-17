#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/17 16:46:02 (CST) daisuke>
#

# importing pathlib module
import pathlib

# file of Yale Bright Star Catalogue
file_bsc = 'catalog.gz'

# making pathlib object
path_bsc = pathlib.Path (file_bsc)

# existence check of file
if (path_bsc.exists ()):
    print (f'File "{file_bsc}" exists.')
    print (f'Downloading of Yale Bright Star Catalogue was successfully done!')
else:
    print (f'File "{file_bsc}" DOES NOT exist.')
    print (f'Download Yale Bright Star Catalogue!')
