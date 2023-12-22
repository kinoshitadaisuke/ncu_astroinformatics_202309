#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/22 13:06:04 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing numpy module
import numpy

# data file
file_data = 'ai2023_s15_04_00.data'

# output file for training dataset
file_training = 'ai2023_s15_04_02_training.data'

# output file for testing dataset
file_testing = 'ai2023_s15_04_02_testing.data'

# fraction of training data
fraction_training = 0.7

# random number generator
rng = numpy.random.default_rng ()

# opening output file for writing
with open (file_training, 'w') as fh_l:
    # opening output file for writing
    with open (file_testing, 'w') as fh_c:
        # opening data file for reading
        with open (file_data, 'r') as fh_r:
            # reading file line-by-line
            for line in fh_r:
                # skipping line if starting with '#'
                if (line[0] == '#'):
                    continue
                # splitting line
                (x_str, y_str, group) = line.split ()
                # converting string into float
                x = float (x_str)
                y = float (y_str)
                # generating a random number
                r = rng.random ()
                # dividing data into training set and testing set
                if (r < fraction_training):
                    fh_l.write (f'{x:8.4f} {y:8.4f} {group}\n')
                else:
                    fh_c.write (f'{x:8.4f} {y:8.4f} {group}\n')
