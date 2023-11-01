#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/01 12:31:34 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.modeling.models
import astropy.units

# units
unit_K      = astropy.units.K
unit_m      = astropy.units.m
unit_micron = astropy.units.micron

# temperature of blackbody
T = 3000.0 * unit_K

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T}')

# range of wavelength (from 10**-8 m to 10**-3 m)
wavelength_min = -8.0
wavelength_max = -3.0

# wavelength in metre
wavelength_m = numpy.logspace (wavelength_min, wavelength_max, \
                               num=5001, dtype=numpy.longdouble) * unit_m

# wavelength in micron
wavelength_micron = wavelength_m.to (unit_micron)

# a function to calculate blackbody radiation for T=3000 K
bb3000  = astropy.modeling.models.BlackBody (temperature=T)

# calculation of blackbody radiation
bb_data = bb3000 (wavelength_micron)

# printing blackbody radiation
print (f'Wavelength:')
print (f'{wavelength_micron}')
print (f'Blackbody radiation:')
print (f'{bb_data}')
