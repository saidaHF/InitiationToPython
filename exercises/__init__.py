import numpy as np

M = np.array([[1, 2, 0],
              [0, 2, 0],
              [0, 0, 3]])
total = M.sum()
print("the sum is : " + str(total))