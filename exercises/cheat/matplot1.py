#!/usr/bin/env python


# Solutions to scipy course
# By carlos.pascual@cells.es

"""
Exercise: matplot1
------------------

Do a script that reads the "converted1.dat" created in the converter1
exercise and plots counts VS time. The script should automatically
save this plot in a file called "mp1.png"

Once you got it, change the Y axis to log scale.
Add titles for the axes in the plot. The script should automatically
save this plot in a file called "mp2.png"

Tips:

- See http://matplotlib.sourceforge.net/users/pyplot_tutorial.html
- For semilog plots you can use matplotlib.pyplot.semilogy()
- For saving a figure, see matplotlib.pyplot.savefig()
- Note that calling matplotlib.pyplot.show() clears the plot
- [Official Solution](exercises/matplot1.py)
"""

import numpy
from matplotlib import pyplot as plt

# note: to use the alternative pyplot implementation from guiqwt, just do:
# from guiqwt import pyplot as plt

inputfilename = "converted1.dat"

time, norm = numpy.loadtxt(inputfilename, unpack=True)

# show in linear scale
plt.title(inputfilename + " (linear)")
plt.xlabel("time [ns]")
plt.ylabel("yield [arbitrary]")
plt.plot(time, norm)
plt.savefig("mp1.png")
plt.show()

# show in log scale
plt.title(inputfilename + " (log)")
plt.xlabel("time [ns]")
plt.ylabel("yield [arbitrary]")
plt.semilogy(time, norm)
plt.savefig("mp2.png")
plt.show()
