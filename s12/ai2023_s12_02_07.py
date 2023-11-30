#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/30 21:02:21 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'ai2023_s12_02_02.data'

# output file name
file_output = 'ai2023_s12_02_07.png'

# empty numpy arrays for storing data
data_per = numpy.array ([])
data_var = numpy.array ([])

# opening file
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # removing line feed at the end of line
        line = line.strip ()
        # splitting data
        (per_day_str, per_hr_str, per_min_str, var_str) = line.split ()
        # conversion from string into float
        per_hr = float (per_hr_str)
        var    = float (var_str)
        # appending the data at the end of numpy arrays
        data_per = numpy.append (data_per, per_hr)
        data_var = numpy.append (data_var, var)

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Period [hr]')
ax.set_ylabel ('Variance')

# axes
ax.set_xlim (3.15, 3.19)
ax.set_ylim (0.00, 0.12)

# plotting data
ax.plot (data_per, data_var, \
         linestyle='-', linewidth=3, color='blue', \
         label='result of PDM analysis')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=150)
