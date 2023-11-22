#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/22 15:58:10 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing astropy module
import astropy.units
import astropy.coordinates

# importing astroquery module
import astroquery.simbad
import astroquery.gaia

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# settings for Gaia query
astroquery.gaia.Gaia.MAIN_GAIA_TABLE = "gaiadr3.gaia_source"
astroquery.gaia.Gaia.ROW_LIMIT       = -1

# parameters
target        = "M3"
file_output   = "m3.vot.gz"
radius_arcmin = 30.0
radius_deg    = radius_arcmin / 60.0

# units
u_deg    = astropy.units.deg
u_ha     = astropy.units.hourangle
u_arcmin = astropy.units.arcmin

# name resolver
result_simbad = astroquery.simbad.Simbad.query_object (target)

# coordinate from Simbad
obj_ra  = result_simbad['RA'][0]
obj_dec = result_simbad['DEC'][0]

# using skycoord of astropy
coord = astropy.coordinates.SkyCoord (obj_ra, obj_dec, frame='icrs', \
                                      unit=(u_ha, u_deg) )

# coordinate in decimal degree
ra_deg  = coord.ra.deg
dec_deg = coord.dec.deg

# coordinate in hms and dms format
ra_hms  = coord.ra.to_string (u_ha)
dec_dms = coord.dec.to_string (u_deg, alwayssign=True)

# printing result
print (f"target: {target}")
print (f" RA  = {ra_hms:>14s} = {ra_deg:10.6f} deg")
print (f" Dec = {dec_dms:>14s} = {dec_deg:+10.6f} deg")

# command for database query
table  = f"gaiadr3.gaia_source"
field  = f"*"
point  = f"POINT({ra_deg:8.4f},{dec_deg:8.4f})"
circle = f"CIRCLE(ra,dec,{radius_deg})"
query  = f"SELECT {field} from {table} WHERE 1=CONTAINS({point},{circle});"

# printing SQL query for Gaia database
print (f"SQL query for Gaia database:")
print (f" {query}")

# sending a job to Gaia database
job = astroquery.gaia.Gaia.launch_job_async (query, dump_to_file=True, \
                                             output_format="votable", \
                                             output_file=file_output)

# printing query to Gaia database
print (job)

# getting results
results = job.get_results ()

# printing results
print (results)
