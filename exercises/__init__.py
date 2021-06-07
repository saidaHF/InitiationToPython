import numpy as np
from numpy.lib import math

M = np.array([[1, 2, 0],
              [0, 2, 0],
              [0, 0, 3]])

total = M.sum()
print("the sum is : " + str(total))
""" The new list copy M list and you can to do changes without affecting the previous list (M) """
print(" ")
newList = M.copy()
print(newList)
"""
newList[0][0] = 3
print(newList)
print(M)
"""

""" create a copy of M called M2. Change the element in the first row and
second column (which is a 2) by its square root. Make sure that M did not
change. Then print the elements of the diagonal of M2 """

print(" ")
newList[0][1] = math.sqrt(newList[0][1])
print(newList.astype(float))

