#!/usr/bin/env python

# solution by cpascual@cells.es

"""
Exercise equation1
------------------

Use scipy for solving equations numerically (works also for equations without
analytical solution)

Find value of x that satisfies the following trascendental equation:

    x = sin(x)

Tips:

- Solving the equation A(x)=B(x) is just finding the roots of the function
  f(x)=A(x)-B(x)

- See the help about scalar function solvers contained in scipy.optimize.

- You can solve simple equations numerically using the Gauss-Newton method.
  See scipy.optimize.newton()

- make your initial guess between -pi/2 and pi/2

- If the newton method does not converge, try playing with the tolerance and/or
  the maximum number of iterations

- [Official Solution](exercises/equation1.py)
"""


import numpy as np
from scipy.optimize import newton


def f(x):
    return x - np.sin(x)


# let's assume we don't know the derivative of f(x)...
# Then I need to increase the maxiter to avoid a non-convergence exception
guess = 1
x = newton(f, guess, maxiter=1000)
print("x= %.5f" % x)


# we can help by giving the derivative if we know it
# Note: in this case it is not necessary to increase maxiter
def df(x):
    return 1 - np.cos(x)


x = newton(f, guess, fprime=df)
print("x= %.5f" % x)
