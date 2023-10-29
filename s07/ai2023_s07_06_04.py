#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/29 17:05:50 (CST) daisuke>
#

# importing astropy module
import astropy.io.fits
import astropy.wcs

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'm3.fits'

# output file name
file_output = 'm3.png'

# object name
object_name = 'Globular Cluster M3'

# colour map
cmap = 'gray'

# resolution in DPI
resolution_dpi = 225

# opening FITS file
with astropy.io.fits.open (file_input) as hdu_list:
    # printing HDU information
    print (hdu_list.info ())
    
    # reading FITS header, WCS information, and image data
    header = hdu_list[0].header
    wcs    = astropy.wcs.WCS (header)
    image  = hdu_list[0].data

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection=wcs)

# axes
ax.set_title (object_name)
ax.set_xlabel ('Right Ascension')
ax.set_ylabel ('Declination')

# plotting image
im = ax.imshow (image, origin='lower', cmap=cmap)
fig.colorbar (im)

# saving file
print (f'{file_input} ==> {file_output}')
fig.savefig (file_output, dpi=resolution_dpi)
