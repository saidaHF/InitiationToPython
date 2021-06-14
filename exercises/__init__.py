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

# age = 24
# print("Guess my age, you have 1 chances!")
# guess = int(input("Guess: "))
#
# if guess != age:
#     print("Wrong!")
# else:
#     print("Correct")
#
# print(" ")
# We use this syntax to define as function:
#
# def function(parameters):
#     instructions
#     return value

# for x in range(1,10):
#     for y in range(1,10):
#         print("(" + str(x) + "," + str(y) + ")")


# print(list(range(5)))

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

# try:
#   print(1 / 0)
# except ZeroDivisionError:
#   #raise ValueError
#     print("exception")

# It is good practice to avoid wasting resources by making sure that files are always closed after they have been used.
# One way of doing this is to use try and finally

file = open("sp8c.dat", "r")
print(file.read(16))
# print(file.read(4))
# print(file.read(4))
# print(file.read())
# file.close()

file.close()
# read for lines
file = open("sp8c.dat", "r")
print(file.readlines())
file.close()

# Dictionaries
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"], ages["Dave"])

# a list comprehension (0^3, 1^3, 2^3, 3^3...)
cubes = [i**3 for i in range(5)]
print(cubes)

print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

# LAMBDA:
# Here we have a function created to add. (sumar +)
def suma(x,y):
    return(x + y)
# The same with lambda:
lambda x,y : x + y
# You need to save it in a variable to be used
suma_dos = lambda x,y : x + y