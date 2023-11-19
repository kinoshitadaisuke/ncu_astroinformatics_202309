#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/19 19:57:45 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
desc   = 'Hubble diagram of high-z supernovae'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-i', '--input', help='input data file name')
parser.add_argument ('-o', '--output', help='output figure file name')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution in DPI (default: 225)')

# command-line arguments analysis
args = parser.parse_args ()

# input parameters
file_data      = args.input
file_fig       = args.output
resolution_dpi = args.resolution

# numpy arrays for storing data
data_zcmb   = numpy.array ([])
data_mB     = numpy.array ([])
data_mB_err = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # reading file
    for line in fh:
        # skip if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting the line
        data = line.split ()
        # extracting data
        zcmb   = float (data[1])
        mB     = float (data[4])
        mB_err = float (data[5])
        # appending data to numpy arrays
        data_zcmb   = numpy.append (data_zcmb, zcmb)
        data_mB     = numpy.append (data_mB, mB)
        data_mB_err = numpy.append (data_mB_err, mB_err)

# distance modulus
data_mu = data_mB + 19.30

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('Redshift')
ax.set_ylabel ('Distance Modulus [mag]')
ax.grid ()

# making a Hubble diagram
ax.errorbar (data_zcmb, data_mu, yerr=data_mB_err, \
             linestyle='none', marker='o', markersize=1, color='blue', \
             ecolor='black', capsize=2, \
             label='high-z supernovae from SNLS')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=resolution_dpi, bbox_inches="tight")
