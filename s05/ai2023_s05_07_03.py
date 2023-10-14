#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/14 10:15:59 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# constructing a parser object
descr  = 'Finding minimum value for a function within a specific range'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-a', type=float, default=1.0, \
                     help='a of a*sin(bx+c)+d (default: 1)')
parser.add_argument ('-b', type=float, default=1.0, \
                     help='a of a*sin(bx+c)+d (default: 1)')
parser.add_argument ('-c', type=float, default=0.0, \
                     help='a of a*sin(bx+c)+d (default: 0)')
parser.add_argument ('-d', type=float, default=0.0, \
                     help='a of a*sin(bx+c)+d (default: 0)')
parser.add_argument ('-r0', '--range0', type=float, default=0.0, \
                     help='start of range of minimum value search (default: 0)')
parser.add_argument ('-r1', '--range1', type=float, default=1.0, \
                     help='end of range of minimum value search (default: 1)')
parser.add_argument ('-min', type=float, default=0.0, \
                     help='minimum value of x for plotting (default: 0)')
parser.add_argument ('-max', type=float, default=1.0, \
                     help='maximum value of x for plotting (default: 1)')
parser.add_argument ('-n', type=int, default=1000, \
                     help='number of data points to produce (default: 1000)')
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.png)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')

# parsing arguments
args = parser.parse_args ()

# input parameters
a              = args.a
b              = args.b
c              = args.c
d              = args.d
r0             = args.range0
r1             = args.range1
range_min      = args.min
range_max      = args.max
n              = args.n
file_output    = args.output
resolution_dpi = args.resolution

# making a pathlib object for output file
path_output = pathlib.Path (file_output)

# check of existence of output file
if (path_output.exists ()):
    # printing a message
    print (f'ERROR: output file "{file_output}" exists!')
    # stopping the script
    sys.exit (0)

# check of extension of output file
if not ( (path_output.suffix == '.eps') \
         or (path_output.suffix == '.pdf') \
         or (path_output.suffix == '.png') \
         or (path_output.suffix == '.ps') ):
    # printing a message
    print (f'ERROR: output file must be either EPS or PDF or PNG or PS file.')
    # stopping the script
    sys.exit (0)

# function of a curve
def curve (x, a, b, c, d):
    # curve
    y = a * numpy.sin (b * x + c) + d
    # returning y-value
    return y

# finding minimum
minimum = scipy.optimize.minimize_scalar (curve, method='bounded', \
                                          args=(a, b, c, d), bounds=(r0, r1))

# minimum value
min_x = minimum.x
min_y = minimum.fun

# printing minimum value
print (f'function: {a} * sin ({b} x + {c}) + {d}')
print (f'minimum:  y = {min_y} at x = {min_x}')

# data to plot
data_x = numpy.linspace (range_min, range_max, n)
data_y = curve (data_x, a, b, c, d)

#
# making plot using Matplotlib
#
    
# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')

# range
ax.set_ylim (None,  (numpy.abs (a) + d) * 1.3)

# plotting data
ax.plot (data_x, data_y, \
         linestyle='-', linewidth=3.0, color='blue', \
         label=f'$f(x)={a} \sin ({b} x + {c}) + {d}$')

# plotting minimum value
ax.plot (min_x, min_y, \
         linestyle='None', marker='o', markersize=5.0, color='red', \
         label='minimum')

# legend
ax.legend ()

# saving file
fig.savefig (file_output, dpi=resolution_dpi)
