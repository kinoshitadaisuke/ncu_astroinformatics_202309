#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/24 18:13:54 (CST) daisuke>
#

# importing numpy module
import numpy

# random number generator
rng = numpy.random.Generator (numpy.random.Philox ())

# generating 100 random numbers of Gaussian distribution
# of mean of 100.0 and standard deviation of 10.0
array_x = rng.normal (100.0, 10.0, 100)

# printing generated random numbers
print (f'{array_x}')
