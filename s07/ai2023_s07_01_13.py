#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/29 11:23:57 (CST) daisuke>
#

# importing astropy module
import astropy.constants
import astropy.units

# units
u_ABmag = astropy.units.ABmag
u_Jy    = astropy.units.Jy
u_uJy   = astropy.units.uJy

# V-band magnitude of 0 in AB magnitude system
m_V = 0.0 * u_ABmag

# K-band magnitude of 20 in AB magnitude system
m_K = 20.0 * u_ABmag

# conversion of m_K = 20.0 into Jy
flux_density_V = m_V.to (u_Jy)
flux_density_K = m_K.to (u_uJy)

# printing result
print (f'm_V = {m_V:4.1f}  ==>  flux density = {flux_density_V:g}')
print (f'm_K = {m_K:4.1f}  ==>  flux density = {flux_density_K:g}')
