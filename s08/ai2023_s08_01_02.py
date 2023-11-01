#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/01 12:56:38 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing astropy module
import astropy.modeling.models
import astropy.units

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'ai2023_s08_01_02.png'

# resolution in DPI
resolution_dpi = 225

# units
unit_K      = astropy.units.K
unit_m      = astropy.units.m
unit_micron = astropy.units.micron

# temperature of blackbody
T = [3000.0, 6000.0, 12000.0, 24000.0] * unit_K

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

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Wavelength [$\mu$m]')
ax.set_ylabel ('Specific Intensity [erg sec$^{-1}$ sr$^{-1}$ cm$^{-2}$ Hz$^{-1}$]')

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')
ax.set_xlim (0.01, 100)
ax.set_ylim (10**-12, 10**-2)

for i in range (len (T)):
    # blackbody radiation model
    bb_model = astropy.modeling.models.BlackBody (temperature=T[i])
    # blackbody radiation
    bb_data  = bb_model (wavelength_micron)

    # label
    text_label = f'T = {T[i]}'
    
    # plotting data
    ax.plot (wavelength_micron, bb_data, \
             linestyle='-', linewidth=3, \
             label=text_label)

# grid
ax.grid ()
    
# legend
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=resolution_dpi)
