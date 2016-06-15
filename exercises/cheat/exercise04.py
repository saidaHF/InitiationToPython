#!/usr/bin/env python


# Solutions to scipy course
# By carlos.pascual@cells.es

"""
Exercise 4 (scipy for matrix operations)
----------------------------------------

1. Generate 3 vectors (1D arrays) called datax, data0 and datay  of 100
   elements each containing:
   * `datax` <-- numbers from -5 to +5 in 0.1 increments
   * `datay0` <-- 3x^2 + 5x - 10
   * `datay = datay0 + random_noise` where `random_noise` is randomly
   distributed gaussian values with standard deviation=10

2. Plot datay0 and datay as a function of datax. Plot datay0 as a blue line
   and datay as red dots .

3. smooth datay with a median filter (you may use a kernel size of, e.g.
   7 points).  Plot the filtered data (with dashed lines) superimposed to datay
   and datay0.

4. make a polynomial fit of datay to the function f(x)=a*x**2+b*x+c .
   Obtain the values of a, b and c from the fit and print them. Then use them
   to plot the fitted curve (in green) superimposed to datay0 and datay.


Tips:

- "import scipy as S"

- See scipy.arange(), scipy.randn() --or even better, scipy.random.normal()--

- For filters, "import scipy.signal" and see scipy.signal.medfilt()

- For polynomial fits, see scipy.polyfit() .
  Note: the scipy.optimize module allows arbitrary function fitting and much
  more powerful optimisers. If you are interested, check them as well.

- Have a look at:

  - http://glowingpython.blogspot.com.es/2011/07/polynomial-curve-fitting.html

  - http://matplotlib.sourceforge.net/users/pyplot_tutorial.html
- [Official Solution](exercises/exercise04.py)
"""

import scipy as S
import matplotlib.pyplot as plt
from scipy.signal import medfilt

# generate data
datax = S.arange(-5, 5, .1)
datay0 = 3 * datax**2 + 5 * datax - 10
datay = S.random.normal(loc=datay0, scale=10.)

# filter
smoothy = medfilt(datay, 7)

# polynomial fit
[a, b, c] = S.polyfit(datax, datay, 2)
print "FIT to f(x)=a*x**2+b*x+c : a=%.3g\tb=%.3g\tc=%.3g" % (a, b, c)
fittedy = a * datax**2 + b * datax + c

# plotting everything
plt.plot(datax, datay0, "b-")
plt.plot(datax, datay, "r.")
plt.plot(datax, smoothy, "b--")
plt.plot(datax, fittedy, "g-")
plt.show()
