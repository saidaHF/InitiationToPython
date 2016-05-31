Exercise 0 (format conversor).
==============================

Download the file [sp8c.dat](exercises/sp8c.dat) and save it in your working 
directory:

It is a positron-decay spectrum (counts as a function of time) saved in ASCII 
with a 3-line header and the data packed in 8 columns.

The header contains the information needed to reconstruct the time scale 
(in ps):

time = ChannelNumber * GAIN + OFFSET

Part 1:
-------

Assume that you know beforehand that the header has 3 lines and that the 
gain is 50.0 and the offset is 1000 ((i.e., you can skip reading the header).
Write a python script that writes converted data to a file called "sp2c.dat"
in 2 columns where:

- There is no header
- column 1 is the time
- column 2 is the number of counts normalised by the maximum value of counts


Part 2:
-------

Modify the program you did in Part 1 but assuming that you need to read the 
header. Particularly, not only the GAIN and OFFSET items may have different 
values, but also the order of the items in the header can vary and there could
be more items in the header (it won't always be 3 lines). The marker for 
end-of-header is the keyword "DATA".


Important: do not import modules. Do it with the basic python built-in 
functions.

Tips:

- for opening the file see the open() function (do "help(open)" or "open?" 
  in ipython)
- for reading the file see: file.readlines()
- for writing, see file.write() and file.close()
- Use the function str.split() and float() to obtain the data as separate 
  numerical values (instead of strings).



Exercise 1 (numpy IO)
=====================
Do the same as you did in *Part 1* of Exercise 0 but using the numpy module.
Work with the data in the form of numpy.arrays

Tips:
-----

- you can save typing by doing: "import numpy as np" (you could even do 
  "from numpy import *" but it is not recommended because it would pollute
  your namespace and make debugging more difficult)
- Use numpy.loadtxt() for reading and and numpy.savetxt() for writing
- You will find the following functions and methods very useful: numpy.max(), 
  numpy.arange() numpy.zeros() and numpy.array.flatten()
- Remember that arithmetical operations on numpy arrays are element-wise!



Exercise 2 (plotting matlab-style).
===================================

Do a script that reads the "sp2c.dat" and plots counts VS time.
Once you got it, change the Y axis to log scale.
Add titles for the axes in the plot

Tips:
-----

- See http://matplotlib.sourceforge.net/users/pyplot_tutorial.html
- For semilog plots you can use matplotlib.pyplot.semilogy()



Exercise 3 (scipy for matrix operations)
========================================

1.-In ipython, explore the documentation of scipy: scipy?

2.-create the following 3x3 square matrix:

    ```
    M = S.array([[1,2,0],
                [0,2,0],
                [0,0,3]])
    ```

3.-Find the sum of all the columns and of all the rows.

4.-Find the transpose of M. Compare the first column of M with the first row of
its transpose (check if they are the same with the "==" operator). 
Make an "if" block that prints "Maths work" if the comparison is true.

5.-create a copy of M called M2. Change the element in the first row and
second column (which is a 2) by its square root. Make sure that M did not 
change. Then get the elements of the diagonal of M2

6.-invert M and then check that M multiplied by its inverse gives an Identity 
matrix (note: round off to 3 decimal points)

7.-Find the eigenvectors and eigenvalues of M. Then check that, for a given 
eigenvalue (w) and its associated eigenvector (v), the following 
is true: M v = w v

 
Tips:
-----

- Important: for this exercise, it is more convenient to use the methods of
  the arrays. i,e, it is better to use M.transpose() than scipy.transpose(M).

- For summing, see the .sum() method. Pay attention to the 'axis' parameter.

- For comparisons: comparing two arrays implies element-by-element comparison.
  See the methods .any() and .all()

- See scipy.linalg for inversion and eigenvectors

- To round-off any scipy data type, you can use the .round() method




Exercise 4 ()
=====================

1.-Generate 3 vectors (1D arrays) called datax, data0 and datay  of 100 
   elements each containing:

    datax= numbers from -5 to +5 in 0.1 increments

    datay0= 3x^2+5x-10

    datay=datay0+ random_noise  

    (where random_noise is randomly distributed gaussian values with standard 
    deviation=10)

2.-Plot datay0 and datay as a function of datax. Plot datay0 as a blue line 
   and datay as red dots .

3.-smooth datay with a median filter (you may use a kernel size of, e.g. 
   7 points).  Plot the filtered data (with dashed lines) superimposed to datay 
   and datay0.

4.-make a polynomial fit of datay to the function f(x)=a*x**2+b*x+c . 
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

 

 
Exercise 5 (numpy IO)
=====================
 
Find value of x that satisfies the following (transcendental) equation:
x = sin(x)

Tips:
-----

- Solving the equation A(x)=B(x) is just finding the roots of the function 
  f(x)=A(x)-B(x)

- See the help about scalar function solvers contained in scipy.optimize. 

- You can solve simple equations numerically using the Gauss-Newton method. 
  See scipy.optimize.newton()

- make your initial guess between -pi/2 and pi/2

- If the newton method does not converge, try playing with the tolerance and/or 
  the maximum number of iterations