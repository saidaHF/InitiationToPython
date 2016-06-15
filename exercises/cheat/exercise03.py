#!/usr/bin/env python


# Solutions to scipy course
# By carlos.pascual@cells.es

"""
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
- [Official Solution](exercises/exercise03.py)

"""

import scipy as S
import scipy.linalg

# step 2
M = S.array([[1, 2, 0],
             [0, 2, 0],
             [0, 0, 3]])

print 'M=\n', M

# step 3
# I will demonstrate two alternative ways of doing it:

# a) calculate the sum of rows using the using the axis parameter
sumcols = M.sum(axis=1)  # 1 means summing over the second index (first is 0))!
print "Sum of rows:",  sumcols

# b)  calculate the sum of columns using slicing and then summing (slower) 
nrows, ncols = M.shape
for i in xrange(ncols):
    print "the sum of column %i is %i" % (i, M[:, i].sum()) 

# step 4
MT = M.transpose()
print "1st row of M : ", M[:, 0]
print "1st col of MT: ", MT[0,:]
print "element-wise comparison: ", M[:, 0] == MT[0,:]
if (M[:, 0] == MT[0,:]).all():
    print "Maths work"

# step 5
M2 = M.astype('float')
M2[0, 1] = S.sqrt(M2[0, 1])
print 'M: \n', M
print 'M2 \n: ', M2
print 'Diagonal:', M2.diagonal()

# step 6
Minv = S.linalg.inv(M)
print "Minv:\n", Minv
print "Minv x M:\n", S.dot(Minv, M).round(3)

# step7
print "Eigenvalues (w) and eigenvectors (v):"
w, v = S.linalg.eig(M)
for i in xrange(len(w)):
    eigval = w[i]
    eigvec = v[:, i]
    print "w=", eigval, "v=", eigvec
    print "M v = w v? :", S.dot(M, eigvec), eigval*eigvec, "?",
    # compare the two solutions allowing for rounding errors:
    tolerance = 1e-5
    diff = S.dot(M, eigvec) - eigval * eigvec
    if (abs(diff).max() < tolerance): 
        print "yes!"
    else:
        print 'no'
    print "----"

raw_input('press enter to exit')
