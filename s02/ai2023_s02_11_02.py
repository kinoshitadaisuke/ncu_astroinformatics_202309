#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/17 17:25:29 (CST) daisuke>
#

# importing random module
import random

# initialisation of random number generator
random.seed ()

#
# generating 10 random numbers of Gaussian dist. of mean=100 and stddev=10
#

# parameters
mean   = 100.0
stddev = 10.0

# generating 10 random numbers
print (f'10 random numbers of Gaussian distribution', \
       f'of mean={mean} and stddev={stddev}')
for i in range (10):
    # generation of a random number of Gaussian distribution
    r = random.gauss (mean, stddev)
    # printing generated random number
    print (f'  {r:15.11f}')
