#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/17 16:55:28 (CST) daisuke>
#

# importing re module
import re

# making a pattern for regular expression
pattern_type = re.compile ('[OBAFGKM][.\d+][V]')

# catalogue file of BSC
file_bsc = 'bsc.data'

# opening file for reading
with open (file_bsc, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # pattern matching using regular expression
        match_type = re.search (pattern_type, line)
        # if matched, print the information of the star
        if (match_type):
            # HR number
            HR    = line[0:4].strip ()
            # name
            name  = line[4:14].strip ()
            # RAh
            RAh   = line[75:77].strip ()
            # RAm
            RAm   = line[77:79].strip ()
            # RAs
            RAs   = line[79:83].strip ()
            # Decpm
            Decpm = line[83].strip ()
            # Decd
            Decd  = line[84:86].strip ()
            # Decm
            Decm  = line[86:88].strip ()
            # Decs
            Decs  = line[88:90].strip ()
            # Vmag
            Vmag  = line[102:107].strip ()
            # SpType
            SpType = line[127:147].strip ()
            # RA
            RA = f'{RAh}:{RAm}:{RAs}'
            # Dec
            Dec = f'{Decpm}{Decd}:{Decm}:{Decs}'

            # converting string into float
            try:
                Vmag_float = float (Vmag)
            except:
                Vmag_float = +999.999

            # if brighter than or equal to 1.0 mag, then print
            if (Vmag_float <= 1.0):
                # printing information about star
                print (f'{HR:4} {name:10} {RA:10} {Dec:9} {Vmag:5} {SpType}')
