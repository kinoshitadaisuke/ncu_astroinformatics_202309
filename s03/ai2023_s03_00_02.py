#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/22 11:27:11 (CST) daisuke>
#

# importing numpy
import numpy

# making a list
list_a = [0.1, 2.3, 4.5, 6.7, 8.9]

# making a Numpy array (ndarray)
array_a = numpy.array (list_a)

# type of "list_a"
type_list_a = type (list_a)

# type of "array_a"
type_array_a = type (array_a)

# printing list
print (f'list_a:')
print (f'  list_a  = {list_a}')
print (f'  type    = {type_list_a}')

# printing Numpy array
print (f'array_a:')
print (f'  array_a = {array_a}')
print (f'  type    = {type_array_a}')
