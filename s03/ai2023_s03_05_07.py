#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 16:01:34 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using numpy.linspace ()
a_deg = numpy.linspace (0.0, 180.0, 7)

# printing a_deg
print (f'a_deg = {a_deg}')

# angle in radian
a_rad = a_deg / 180.0 * numpy.pi

# printing a_rad
print (f'a_rad = {a_rad}')

# calculation
# no need of using "for"
sin_a = numpy.sin (a_rad)
cos_a = numpy.cos (a_rad)

# printing b
print (f'sin (a) = {sin_a}')
print (f'cos (a) = {cos_a}')
