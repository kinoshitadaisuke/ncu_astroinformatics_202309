#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/29 11:11:20 (CST) daisuke>
#

# importing astropy module
import astropy.units

# units
u_cm        = astropy.units.cm
u_g         = astropy.units.g
u_g_per_cm3 = u_g / u_cm**3

# density in g/cm^3
rho1 = 3.0 * u_g_per_cm3

# density in kg/m^3
rho2 = rho1.si

# printing density in SI and in CGS
print (f'rho1 = {rho1}')
print (f'rho2 = {rho2}')
