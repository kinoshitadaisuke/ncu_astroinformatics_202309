#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 16:33:00 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy array (2x2 matrix)
A = numpy.array ([ [5.0, 3.0], [6.0, 4.0] ])

# printing A
print (f'A:\n{A}')

# calculating inverse matrix of A
B = numpy.linalg.inv (A)

# priting B
print (f'B = A^-1:\n{B}')

# calculation of A @ B
C = A @ B

# printing C
print (f'C = A @ B:\n{C}')
