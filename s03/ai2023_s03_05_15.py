#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 16:27:55 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy array (3x3 matrix)
C = numpy.array ([ [1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0] ])

# printing C
print (f'C:\n{C}')

# making Numpy array (3x3 unit matrix)
E3 = numpy.identity (3)

# printing E3
print (f'E3:\n{E3}')

# calculation
D = E3 @ C

# printing D
print (f'D = E3 @ C:\n{D}')
