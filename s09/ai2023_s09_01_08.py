#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/10 15:10:19 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.units
import astropy.coordinates

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# data file
file_data = 'bsc5c.data'

# output files
file_output = 'ai2023_s09_01_08.png'

# resolution in DPI
resolution_dpi = 225

# numpy arrays to storing data
data_hr   = numpy.array ([])
data_ra   = numpy.array ([])
data_dec  = numpy.array ([])
data_l    = numpy.array ([])
data_b    = numpy.array ([])
data_Vmag = numpy.array ([])
data_BV   = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # counting number of objects
    n = 0
    for line in fh:
        n += 1

# opening file
with open (file_data, 'r') as fh:
    i = 0
    # reading file
    for line in fh:
        # skipping line, if the line starts with '#'
        if (line[0] == '#'):
            continue
        # counting and showing progress
        i += 1
        if (i % 500 == 0):
            print ("progress: %4d / %4d" % (i, n) )
        # splitting line
        (hr_str, ra_str, dec_str, glon_str, glat_str, Vmag_str, BV_str) \
            = line.split ()
        # conversion from string to int or float
        hr = int (hr_str)
        glon_deg = float (glon_str)
        glat_deg = float (glat_str)
        Vmag = float (Vmag_str)
        BV = float (BV_str)

        # coordinate
        coord = astropy.coordinates.SkyCoord (ra_str, dec_str, \
                                              frame=astropy.coordinates.FK5, \
                                              equinox="J2000", \
                                              unit=(u_ha, u_deg) )

        # (RA, Dec) in radian
        ra_rad = coord.ra.radian
        dec_rad = coord.dec.radian
        # conversion from (RA, Dec) to (l, b) using astropy
        l_rad = coord.galactic.l.radian
        b_rad = coord.galactic.b.radian

        # changing from [0:2pi] to [-pi:pi]
        if (ra_rad > numpy.pi):
            ra_rad -= 2.0 * numpy.pi
        if (l_rad > numpy.pi):
            l_rad -= 2.0 * numpy.pi

        # appending data to numpy arrays
        data_hr   = numpy.append (data_hr, hr)
        data_ra   = numpy.append (data_ra, ra_rad)
        data_dec  = numpy.append (data_dec, dec_rad)
        data_l    = numpy.append (data_l, l_rad)
        data_b    = numpy.append (data_b, b_rad)
        data_Vmag = numpy.append (data_Vmag, Vmag)
        data_BV   = numpy.append (data_BV, BV)

# galactic plane
gal_lon = numpy.linspace (0.001, 359.999, 1000) * u_deg
gal_lat = numpy.zeros (1000) * u_deg
gal_coord = astropy.coordinates.Galactic (l=gal_lon, \
                                          b=gal_lat)
gal_ra  = gal_coord.transform_to (astropy.coordinates.ICRS) \
                   .ra.wrap_at (180.0 * u_deg).radian
gal_dec = gal_coord.transform_to (astropy.coordinates.ICRS).dec.radian

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection="hammer")

# axes
ax.grid ()
ax.set_title ('Bright Star Catalogue', loc='right')
ax.set_xlabel ('Right Ascension')
ax.set_ylabel ('Declination')

# plotting data
ax.plot (gal_ra, gal_dec, \
         linestyle='None', marker='o', color='silver', markersize=5, \
         alpha=0.1, label='Galactic plane')
size = (8.0 - data_Vmag) * 5.0
colour = 2.0 - data_BV
for j in range ( len (colour) ):
    if (colour[j] < 0.0):
        colour[j] = 0.0
ax.scatter (data_ra, data_dec, \
            marker='o', s=size, \
            c=colour, cmap=matplotlib.cm.Spectral, alpha=0.25)

# saving figure to files
fig.savefig (file_output, dpi=resolution_dpi, bbox_inches="tight")
