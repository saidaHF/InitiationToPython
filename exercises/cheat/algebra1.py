#!/usr/bin/env python

# solution by cpascual@cells.es

"""
Exercise: algebra1
-------------------

Use numpy arrays for performing algebraic manipulations of matrices and vectors

1. create the following 3x3 square matrix:

        M = np.array([[1,2,0],
                      [0,2,0],
                      [0,0,3]])

2. Print the sum of all the columns and of all the rows.

3. Print the transpose of M. Compare the first column of M with the first row
of its transpose (check if they are the same with the "==" operator).
Make an "if" block that prints "Maths work" if the comparison is true.

4. create a copy of M called M2. Change the element in the first row and
second column (which is a 2) by its square root. Make sure that M did not 
change. Then print the elements of the diagonal of M2

5. invert M and then check that M multiplied by its inverse gives an Identity
matrix (note: round off to 3 decimal points)

6. Find the eigenvectors and eigenvalues of M. Then check that, for a given
eigenvalue (w) and its associated eigenvector (v), the following 
is true: M v = w v

 
Tips:


- Important: for this exercise, it is more convenient to use the methods of
  the arrays. i,e, it is better to use M.transpose() than numpy.transpose(M).

- For summing, see the .sum() method. Pay attention to the 'axis' parameter.

- For comparisons: comparing two arrays implies element-by-element comparison.
  See the methods .any(), .all() and np.allclose()

- See numpy.linalg submodule for inversion and eigenvectors

- To round-off any numpy data type, you can use the .round() method
- [Official Solution](exercises/algebra1.py)

"""


import numpy as np

# step 1
M = np.array([[1, 2, 0], [0, 2, 0], [0, 0, 3]])

print("M=\n", M)

# step 2
# I will demonstrate two alternative ways of doing it:

# a) calculate the sum of rows using the using the axis parameter
sumcols = M.sum(axis=1)  # 1 means summing over the second index (first is 0))!
print("Sum of rows:", sumcols)

# b)  calculate the sum of columns using slicing and then summing (slower)
_, ncols = M.shape
for i in range(ncols):
    print("the sum of column %i is %i" % (i, M[:, i].sum()))

# step 3
MT = M.transpose()
print("1st col of M : ", M[:, 0])
print("1st row of MT: ", MT[0, :])
print("element-wise comparison: ", M[:, 0] == MT[0, :])
if (M[:, 0] == MT[0, :]).all():
    print("Maths work")

# step 4
M2 = M.astype("float")  # cast it to float to allow it to contain float values
M2[0, 1] = np.sqrt(M2[0, 1])
print("M: \n", M)
print("M2: \n", M2)
print("Diagonal:", M2.diagonal())

# step 5
Minv = np.linalg.inv(M)
print("Minv:\n", Minv)
print("Minv x M:\n", np.dot(Minv, M).round(3))

# step6
print("Eigenvalues (w) and eigenvectors (v):")
w, v = np.linalg.eig(M)
for i in range(len(w)):
    eigval = w[i]
    eigvec = v[:, i]
    print("w=", eigval, "v=", eigvec)
    print("M v = w v? :", np.dot(M, eigvec), eigval * eigvec, "?")
    # compare the two solutions allowing for finite-precision errors:
    if np.allclose(np.dot(M, eigvec), eigval * eigvec):
        print("yes!")
    else:
        print("no")
    print("----")

