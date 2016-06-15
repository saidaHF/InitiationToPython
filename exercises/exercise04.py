
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
- [Official Solution](exercises/cheat/exercise04.py)
"""

# Write your solution here
