#!/usr/bin/env python

# solution by cpascual@cells.es

"""
Exercise fitting1
-----------------

1. Generate 3 vectors (1D arrays) called data_x, data_y0 and data_y  of 100
   elements each containing:
   * `data_x` <-- numbers from -5 to +5 in 0.1 increments
   * `data_y0` <-- 3x^2 + 5x - 10
   * `data_y = data_y0 + random_noise` where `random_noise` is randomly
   distributed gaussian values with standard deviation=10

2. Plot data_y0 and data_y as a function of data_x. Plot data_y0 as a blue line
   and data_y as red dots.

3. smooth data_y with a median filter using a kernel size of 7.
   Plot the filtered data (with dashed lines) superimposed to data_y
   and data_y0.

4. make a polynomial fit of data_y to the function f(x) = a*x**2+b*x+c .
   Obtain the values of a, b and c from the fit and print them. Then use them
   to plot the fitted curve (in green) superimposed to data_y0, data_y
   and the filtered data. Make the script automatically save this
   plot as "fit.png"


Tips:

- "import numpy as np"

- See numpy.arange(), numpy.randn() --or even better, numpy.random.normal()--

- For filters, "import scipy.signal" and see scipy.signal.medfilt()

- For polynomial fits, see numpy.polyfit() .
  Note: the scipy.optimize module allows arbitrary function fitting and much
  more powerful optimisers. If you are interested, check them as well.

- Have a look at:
  - http://glowingpython.blogspot.com.es/2011/07/polynomial-curve-fitting.html
  - http://matplotlib.sourceforge.net/users/pyplot_tutorial.html

- [Official Solution](exercises/fitting1.py)
"""

# Write your solution here
