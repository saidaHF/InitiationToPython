#!/usr/bin/env python

"""
Exercise converter4
--------------------

Do the same as you did in exercise **converter1** but using the numpy module.
Work with the data in the form of numpy.arrays

Tips:

- you can save typing by doing: "import numpy as np" (you could even do
  "from numpy import *" but it is not recommended because it would pollute
  your namespace and make debugging more difficult)
- Use numpy.loadtxt() for reading and and numpy.savetxt() for writing
- You will find the following functions and methods very useful: numpy.max(),
  numpy.arange() numpy.zeros() and numpy.array.flatten()
- Remember that arithmetical operations on numpy arrays are element-wise
  (you do not need any explicit loop in this exercise!)
- [Official Solution](exercises/converter4.py)
"""

import numpy

input_file_name = "../sp8c.dat"
output_file_name = "converted4.dat"


# I am assuming I know the values of the header (as in ex. converter1).
hdr_lines = 3
gain = 50.0
offset = 1000.0

# read the data (I skip the 3 first rows -the header-)
data = numpy.loadtxt(input_file_name, skiprows=hdr_lines)

# make a vector out of the Nx8 matrix read by loadtxt() and normalise it
data = data.flatten() / data.max()

# calculate the time (column x)
time = numpy.arange(data.size) * gain + offset

# stack time and data as columns in a Nx2 matrix
output = numpy.column_stack((time, data))

# write to output file
numpy.savetxt(output_file_name, output)
