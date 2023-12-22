#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/22 10:38:51 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing numpy module
import numpy

# making a random number generator
rng = numpy.random.default_rng ()

# generating random numbers
A_0     = 1.5
A_1     = 2.0
k_0     = 0.3
k_1     = 0.3
delta_0 = 0.0
delta_1 = 0.0
C_0     = 5.0
C_1     = 11.5
n_0     = 300
n_1     = 300
noise0  = rng.normal (loc=0.0, scale=1.0, size=n_0)
noise1  = rng.normal (loc=0.0, scale=1.0, size=n_1)
data_0x = rng.uniform (low=1.0, high=15.0, size=n_0)
data_0y = A_0 * numpy.sin (k_0 * data_0x + delta_0) + C_0 + noise0
data_1x = rng.uniform (low=1.0, high=15.0, size=n_1)
data_1y = A_1 * numpy.sin (k_1 * data_1x + delta_1) + C_1 + noise1

# printing data
print (f'# feature X, feature Y, classification')
for i in range (data_0x.size):
    print (f'{data_0x[i]:8.4f} {data_0y[i]:8.4f} A')
for i in range (data_1x.size):
    print (f'{data_1x[i]:8.4f} {data_1y[i]:8.4f} B')
