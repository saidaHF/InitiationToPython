
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
- [Official Solution](exercises/cheat/exercise03.py)

"""

# Write your solution here
