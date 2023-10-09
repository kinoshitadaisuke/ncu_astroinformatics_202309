#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/09 22:29:00 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.linalg

# matrix A
A = numpy.array ( [ [4.0, 11.0], [2.0, 5.0] ] )

# printing matrix A
print (f'matrix A:\n{A}')

# determinant of matrix A
A_det = scipy.linalg.det (A)

# printing the determinant of matrix A
print (f'determinant of matrix A = {A_det}')

# inverse of matrix A
A_inv = scipy.linalg.inv (A)

# printing inverse of matrix A
print (f'A^{-1}:\n{A_inv}')

# calculation of A @ A_inv
B = A @ A_inv

# printing matrix B
print (f'matrix B = A @ A_inv:\n{B}')
