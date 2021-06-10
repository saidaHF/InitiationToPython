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
print(" ")
""" Like "Scanner" in Java, data entry """

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# s = x + y
# print(s)

print(" ")

# lists / array
l = [ "Drake", "Derp", "Derek", "Alicia" ]
print(l)                # prints all elements
l.append("Victoria")   # add element.
print(l)                # print all elements
l.remove("Derp")       # remove element.
l.remove("Drake")      # remove element.
print(l)               # print all elements.
l.sort()    # sorts the list in alphabetical order
l.reverse() # reverse order.
print(l)
print(" ")

age = 24
print("Guess my age, you have 1 chances!")
guess = int(input("Guess: "))

if guess != age:
    print("Wrong!")
else:
    print("Correct")

print(" ")
# We use this syntax to define as function:
#
# def function(parameters):
#     instructions
#     return value

# for x in range(1,10):
#     for y in range(1,10):
#         print("(" + str(x) + "," + str(y) + ")")


print(list(range(5)))

# En Python hay las listas y las tuplas. La lista es una estructura mutable (es decir podemos modificar sus elementos,
# agregar y borrar) en cambio una tupla es una secuencia de datos inmutable, es decir una vez definida no puede cambiar.
#
# TUPLA:
# x = (3,4,5,6)
# x = x + (1,2,3)
# print(x)
#
# Puede estar vacia:
# tuple = ()
#
# O solo un elemento:
# tuple = (3,)