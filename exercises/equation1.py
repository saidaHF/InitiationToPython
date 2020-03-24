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

# Write your solution here
