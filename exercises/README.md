Python Introduction exercises 
=============================

At the end of each session, some exercises from this page will be proposed, 
which you should try to solve during that day. I will review your solution and 
make comments (see the procedure below).

On the following session, we will all discuss the different approaches and 
common problems/solutions.


Procedure for submitting your exercises:
----------------------------------------

1. Go to the [exercises page][1] and download the file corresponding to the 
   exercise that you want to solve
   
2. Open the downloaded file (e.g., whith spyder) and solve the exercise, testing
   in your PC

3. When finished, go back to the [exercises page from my repository][1]
   (see important note below). Then click on the file corresponding to the 
   exercise and select `Edit`. Copy & Paste your code here and click on the 
   `Commit Changes` button

4. You will be presented with a new page called `New Merge Request`. Just click 
   on the `Submit merge request` button. If you do not get here, it is probably 
   because you are editing a file in you own repository instead of mine 
   (see Note below).
   
5. This will create a *merge-request* which is where I will add comments when I 
   review the code that you wrote. You can also add comments in this 
   merge-request. Note: You can access your merge-requests at any time from 
   [here](http://git.cells.es/cpascual/pythoncourse-intro/merge_requests)
   (tip: filter by "author" to see only your requests)
 
6. If, as a result of the review, you want to resubmit your code, just close 
   this merge-request and repeat steps 3-5.


**NOTE:** In step 3, make sure that you are editing the exercise file from 
[exercises page from MY (cpascual) repository][1], **not yours**. 
Note that if you have already submitted a merge-request, a *fork* (copy) of my 
repository will have been created for you automatically with an address like 
`http://git.cells.es/YOUR_USER_NAME/pythoncourse-intro`.
But in order for me to review your solutions, you need to edit MY file so that 
a merge-request is created.

[1]: http://git.cells.es/cpascual/pythoncourse-intro/tree/master/exercises
 
List of exercises
=================


Warm-up exercises
-----------------

Simple exercises to get used to python basics.

- From http://introtopython.org/var_string_num.html :
  - hello world
  - one variable, two messages
  - first name cases
  - full name
  - arithmetic
  
- From http://introtopython.org/lists_tuples.html :
  - first list
  - working list
  - starting from empty
  - ordered numbers (ignore the requirement of using for loops)
  - alphabet slices
  - first twenty
  
- And *also* the following exercise on dictionaries:
  Create the following dictionary to be used as a phonebook:
  
        phonebook = { "John" : 7566,  "Jack" : 7264,  "Jill" : 2781}

  Add "Jake" to the phonebook with the phone number 938273443,  and remove Jill
  from the phonebook. Then print the phonebook in alphabetical order



Exercise 0 (format conversor).
------------------------------

Download the file [sp8c.dat](exercises/sp8c.dat) and save it in your working 
directory:

It is a positron-decay spectrum (counts as a function of time) saved in ASCII 
with a 3-line header and the data packed in 8 columns.

The header contains the information needed to reconstruct the time scale 
(in ps):

`time = ChannelNumber * GAIN + OFFSET`

The exercise is done in two parts:

1. Assume that you know beforehand that the header has 3 lines and that the 
gain is 50.0 and the offset is 1000 ((i.e., you can skip reading the header).
Write a python script that writes converted data to a file called "sp2c.dat"
in 2 columns where:
  - There is no header
  - column 1 is the time
  - column 2 is the number of counts normalised by the maximum value of counts


2. Modify the program you did in part 1 but assuming that you need to read the 
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
- [Official Solution](exercises/cheat/exercise00.py)



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
- [Official Solution](exercises/cheat/exercise01.py)


Exercise 2 (plotting matlab-style).
-----------------------------------

Do a script that reads the "sp2c.dat" and plots counts VS time.
Once you got it, change the Y axis to log scale.
Add titles for the axes in the plot

Tips:

- See http://matplotlib.sourceforge.net/users/pyplot_tutorial.html
- For semilog plots you can use matplotlib.pyplot.semilogy()
- [Official Solution](exercises/cheat/exercise02.py)


Exercise 3 (scipy for matrix operations)
----------------------------------------

1. In ipython, explore the documentation of scipy: scipy?

2. create the following 3x3 square matrix:

        M = S.array([[1,2,0],
                    [0,2,0],
                    [0,0,3]])

3. Find the sum of all the columns and of all the rows.

4. Find the transpose of M. Compare the first column of M with the first row of
its transpose (check if they are the same with the "==" operator). 
Make an "if" block that prints "Maths work" if the comparison is true.

5. create a copy of M called M2. Change the element in the first row and
second column (which is a 2) by its square root. Make sure that M did not 
change. Then get the elements of the diagonal of M2

6. invert M and then check that M multiplied by its inverse gives an Identity 
matrix (note: round off to 3 decimal points)

7. Find the eigenvectors and eigenvalues of M. Then check that, for a given 
eigenvalue (w) and its associated eigenvector (v), the following 
is true: M v = w v

 
Tips:


- Important: for this exercise, it is more convenient to use the methods of
  the arrays. i,e, it is better to use M.transpose() than scipy.transpose(M).

- For summing, see the .sum() method. Pay attention to the 'axis' parameter.

- For comparisons: comparing two arrays implies element-by-element comparison.
  See the methods .any() and .all()

- See scipy.linalg for inversion and eigenvectors

- To round-off any scipy data type, you can use the .round() method
- [Official Solution](exercises/cheat/exercise03.py)




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

 

 
Exercise 5 (scipy for data reduction)
--------------------------------------
 
Find value of x that satisfies the following (transcendental) equation:
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
- [Official Solution](exercises/cheat/exercise05.py)