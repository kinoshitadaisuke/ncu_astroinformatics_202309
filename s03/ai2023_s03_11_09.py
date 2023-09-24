#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 19:48:00 (CST) daisuke>
#

# importing numpy module
import numpy
import numpy.ma

# data
data = numpy.array ([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, \
                     5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5])

# printing data
print ("data:")
print (data)

# making a mask using an operator ">="
mask = data >= 7.0

# printing mask
print ("mask:")
print (mask)

# making a masked array
masked_data = numpy.ma.array (data, mask=mask)

# printing a masked array
print ("masked_data:")
print (masked_data)

# making a mask using an operator "<="
mask2 = data <= 3.0

# printing mask
print ("mask2:")
print (mask2)

# making a masked array
masked_data2 = numpy.ma.array (data, mask=mask2)

# printing a masked array
print ("masked_data:")
print (masked_data2)
