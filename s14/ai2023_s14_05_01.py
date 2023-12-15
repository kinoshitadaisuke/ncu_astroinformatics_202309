#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/15 14:45:27 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing datetime module
import datetime

# importing numpy module
import numpy

# importing astropy module
import astropy.time
import astropy.units

# importing rebound module
import rebound

# date/time now
now = datetime.datetime.now ()

# units
u_day = astropy.units.day

# simulation file
file_sim = 'comets.bin'

# output file
file_output = 'comets.data'

# parameters
year       = 2.0 * numpy.pi
time_epoch = '2000-01-01T12:00:00'
t_interval = 0.1 # 0.1 ==> 365.25/(2.0*pi) * 0.1 = 5.81 days
n_output   = 3000

# objects
objects = [
    'Sun',
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune',
    'Pluto',
    '1P/Halley',
    '2P/Encke',
    '8P/Tuttle',
    '9P/Tempel',
    '17P/Holmes',
    '21P/Giacobini-Zinner',
    '22P/Kopff',
    '23P/Brorsen-Metcalf',
    '29P/Schwassmann-Wachmann',
    '55P/Tempel-Tuttle',
    '63P/Wild',
    '67P/Churyumov-Gerasimenko',
    '109P/Swift-Tuttle',
    '122P/de Vico',
    '153P/Ikeya-Zhang',
]

# reading simulation from file
sim = rebound.Simulation (file_sim)
sim.integrator = 'mercurius'
sim.dt = +0.01
sim.move_to_com ()

# particles
ps = sim.particles

# opening file for writing
with open (file_output, 'w') as fh:
    # writing header
    fh.write (f"#\n")
    fh.write (f"# results of orbital integration using rebound\n")
    fh.write (f"#\n")
    fh.write (f"#   start of integration: {now}\n")
    fh.write (f"#\n")
    fh.write (f"#   list of objects:\n")
    for name in objects:
        fh.write (f"#     {name}\n")
    fh.write (f"#\n")
    fh.write (f"#   format of the data:\n")
    fh.write (f"#     JD, date/time, x,y,z,vx,vy,vz of obj1, ")
    fh.write (f"x,y,z,vx,vy,vz of obj2, ...\n")
    fh.write (f"#\n")

    # epoch
    t_epoch = astropy.time.Time (time_epoch, scale='utc', format='isot')

    # orbital integration
    for i in range (n_output):
        # target time
        time = t_interval * i
        # integration
        sim.integrate (time)
        # time after a step of integration
        t_current  = t_epoch + 365.25 * sim.t / year * u_day
        jd_current = t_current.jd

        # writing data to file
        fh.write (f"{jd_current:.8f}|{t_current}")
        for j in range ( len (objects) ):
            fh.write (f"|{ps[j].x:+.15f},{ps[j].y:+.15f},{ps[j].z:+.15f},")
            fh.write (f"{ps[j].vx:+.15f},{ps[j].vy:+.15f},{ps[j].vz:+.15f}")
        fh.write (f"\n")

        # printing status
        if ( (i + 1) % 100 == 0 ):
            print (f"  status: {i + 1:8d} / {n_output:8d}")
