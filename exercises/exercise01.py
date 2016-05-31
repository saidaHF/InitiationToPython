#!/usr/bin/env python


#Solutions to scipy course
#By carlos.pascual@cells.es

"""
Exercise 1 (numpy IO)
----------------------

Do the same as you did in *Part 1* of Exercise 0 but using the numpy module.
Work with the data in the form of numpy.arrays

Tips:

- you can save typing by doing: "import numpy as np" (you could even do 
  "from numpy import *" but it is not recommended because it would pollute
  your namespace and make debugging more difficult)
- Use numpy.loadtxt() for reading and and numpy.savetxt() for writing
- You will find the following functions and methods very useful: numpy.max(), 
  numpy.arange() numpy.zeros() and numpy.array.flatten()
- Remember that arithmetical operations on numpy arrays are element-wise!
- [Official Solution](exercises/exercise01.py)
"""

import numpy
inputfilename='sp8c.dat'
outputfilename='sp2c.dat'


# I am assuming I know the values of the header. See exercise 00 Part 2
# for a implementation where the header is read.
hdr_lines =  3
gain = 50.
offset = 1000.

#read the data (I skip the 3 first rows -the header-)
data = numpy.loadtxt(inputfilename, skiprows=hdr_lines)

# make a vector out of the Nx8 matrix read by loadtxt()
data = data.flatten()  

# create an empty Nx2 matrix (to store the 2 columns)
output = numpy.zeros((data.size, 2))  

# and fill it...
output[:,0] = numpy.arange(data.size) * gain + offset  # time
output[:,1] = data / data.max()  # normalised data

# write to output file
numpy.savetxt(outputfilename, output)

