#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/10 09:50:57 (Taiwan_Standard_Time_UT+8) daisuke>
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
descr  = 'Local peak detection and masking for astronomical image'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input-file', default='', \
                     help='input file name')
parser.add_argument ('-o', '--output-file', default='', \
                     help='output file name')
parser.add_argument ('-s', '--sigma', type=float, default=3.0, \
                     help='threshold for sky estimate (default: 3 [sigma])')
parser.add_argument ('-t', '--threshold', type=float, default=2.0, \
                     help='threshold for source detection (default: 2 [sigma])')
parser.add_argument ('-n', '--npixels', type=int, default=5, \
                     help='minimum number of pixels for detection (default: 5)')
parser.add_argument ('-d', '--dilate-size', type=int, default=21, \
                     help='dilate footprint size (default: 21)')
parser.add_argument ('-m', '--maxiters', type=int, default=10, \
                     help='maximum number of iterations (default: 10)')

# command-line argument analysis
args = parser.parse_args ()

# file names
file_input  = args.input_file
file_output = args.output_file

# input parameters
sigma_sky   = args.sigma
sigma_det   = args.threshold
npixels     = args.npixels
dilate_size = args.dilate_size
maxiters    = args.maxiters

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

# finding threshold value for detecting local peaks
threshold_adu = photutils.segmentation.detect_threshold (image, \
                                                         nsigma=sigma_det, \
                                                         sigma_clip=sigma_clip)

# making segmentation image
image_segmentation = photutils.segmentation.detect_sources (image, \
                                                            threshold_adu, \
                                                            npixels=npixels)

# size of dilation footprint
footprint = photutils.utils.circular_footprint (radius=dilate_size)

# making source mask
source_mask = image_segmentation.make_source_mask (footprint=footprint)
        
# making masked array
image_masked = numpy.ma.array (image, mask=source_mask)

# adding comments to the header
header['history'] = "FITS file created by the command \"%s\"" % (sys.argv[0])
header['history'] = "Updated on %s" % (now)
header['comment'] = "source detection and masking"
header['comment'] = "Options given:"
header['comment'] = "  sigma_sky   = %f [sigma]" % (sigma_sky)
header['comment'] = "  sigma_det   = %f [sigma]" % (sigma_det)
header['comment'] = "  npixels     = %d [pixel]" % (npixels)
header['comment'] = "  dilate_size = %d [pixel]" % (dilate_size)
header['comment'] = "  maxiters    = %d" % (maxiters)

# writing a FITS file
astropy.io.fits.writeto (file_output, image_masked.filled (fill_value=0.0), \
                         header=header)
