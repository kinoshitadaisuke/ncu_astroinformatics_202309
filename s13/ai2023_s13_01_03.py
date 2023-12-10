#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/10 09:50:08 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing datetime module
import datetime

# importing numpy module
import numpy.ma

# importing astropy module
import astropy.io.fits
import astropy.stats

# importing photutils module
import photutils.segmentation

# date/time
now = datetime.datetime.now ()

# constructing parser object
descr  = 'Generating 2-D sky background map for astronomical image'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input-file', default='', \
                     help='input file name')
parser.add_argument ('-o', '--output-file', default='', \
                     help='output file name')
parser.add_argument ('-s', '--sigma', type=float, default=3.0, \
                     help='threshold for sky estimate (default: 3 [sigma])')
parser.add_argument ('-m', '--maxiters', type=int, default=10, \
                     help='maximum number of iterations (default: 10)')
parser.add_argument ('-b', '--box-size', type=int, default=50, \
                     help='box size for sky background estimate (default: 50)')
parser.add_argument ('-f', '--filter-size', type=int, default=3, \
                     help='filter size (default: 3)')

# command-line argument analysis
args = parser.parse_args ()

# file names
file_input  = args.input_file
file_output = args.output_file

# input parameters
sigma_sky   = args.sigma
maxiters    = args.maxiters
box_size    = args.box_size
filter_size = args.filter_size

# making pathlib objects
path_input  = pathlib.Path (file_input)
path_output = pathlib.Path (file_output)

# check of input file name
if not (path_input.suffix == '.fits'):
    # printing message
    print ("ERROR: Input file must be a FITS file.")
    # exit
    sys.exit ()

# existence check of input file
if not (path_input.exists ()):
    # printing message
    print ("ERROR: Input file '%s' does not exist." % (file_input) )
    # exit
    sys.exit ()

# check of output file name
if not (path_output.suffix == '.fits'):
    # printing message
    print ("ERROR: Output file must be a FITS file.")
    # exit
    sys.exit ()

# existence check of output file
if (path_output.exists ()):
    # printing message
    print ("ERROR: Output file '%s' exists." % (file_output) )
    # exit
    sys.exit ()

# opening FITS file
with astropy.io.fits.open (file_input) as hdu:
    # reading header and image
    header = hdu[0].header
    image  = hdu[0].data
    # if no image in PrimaryHDU, then read next HDU
    if (header['NAXIS'] == 0):
        header = hdu[1].header
        image  = hdu[1].data

# sigma-clipping algorithm for removing stars
sigma_clip = astropy.stats.SigmaClip (sigma=sigma_sky, maxiters=maxiters)

# sky background estimator
skybg_estimator = photutils.background.SExtractorBackground ()

# making 2-D sky background map for a given image
image_skybg = photutils.background.Background2D \
    (image, box_size=(box_size, box_size), \
     filter_size=(filter_size, filter_size), \
     sigma_clip=sigma_clip, bkg_estimator=skybg_estimator)

# sky background subtraction
image_skysub = image - image_skybg.background

# adding comments to the header
header['history'] = "FITS file created by the command \"%s\"" % (sys.argv[0])
header['history'] = "Updated on %s" % (now)
header['comment'] = "sky-background-subtracted image using 2D sky map"
header['comment'] = "Options given:"
header['comment'] = "  sigma_sky   = %f [sigma]" % (sigma_sky)
header['comment'] = "  maxiters    = %d" % (maxiters)
header['comment'] = "  box_size    = %d" % (box_size)
header['comment'] = "  filter_size = %d" % (filter_size)

# writing a FITS file
astropy.io.fits.writeto (file_output, image_skysub, header=header)
