# Python intro course

The following is just an index of things to explain, with references to other tutorials

tutX.Y.Z are references to the  Python Tutorial:

https://docs.python.org/3.7/tutorial/index.html

---

# Getting started

- Why python: 
    - scripted 
    - dynamic types
    - multi-platform 
    - many libraries
    - multi-purpose (science, automation, web, GUIs, ...)
    - free
    - easy!

---

# Installation:
    
for this course we will use conda (see the pre-course info)
but if you use reasonably recent linux distro, you may 
alternatively also install the packages from the official repositories

## Which version of python (2.x vs 3.x): 

- As a general rule, (at the time of writing (December 2019)
  we recommend using at least 3.7
- ... or 3.5 if you need to run code on a debian stretch (e.g. in ALBA debian machines)
- ... or 2.7 only if you need to run code in very old machines (e.g. old SuSe machines at ALBA)

---

# interactive mode vs scripts

- `ipython` (vs `python`)
- `python hello.py`
- Space matters!!! (set tabs=4 spaces in your editor)
- For a "matlab-like" IDE, use [spyder](https://www.spyder-ide.org/) or [jupyter lab](https://jupyter.org/)
- For "serious" development, we recommend [PyCharm **Community Edition**](https://www.jetbrains.com/pycharm/download)

---

# Python types

- Types:
    - [Numbers](https://docs.python.org/3.7/tutorial/introduction.html#numbers) 
    - [Strings](https://docs.python.org/3.7/tutorial/introduction.html#strings)
    - `None` 
    - [Lists](https://docs.python.org/3.7/tutorial/introduction.html#lists) and [More on lists](https://docs.python.org/3.7/tutorial/datastructures.html#more-on-lists)
    - [Tuples](https://docs.python.org/3.7/tutorial/datastructures.html#tuples-and-sequences)
    - [Sets](https://docs.python.org/3.7/tutorial/datastructures.html#sets)
    - [Dictionaries](https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries)
    - (Mention numpy arrays )
- concepts:
    - everything is a class: `type()`
    - operators
    - slicing
    - (un)packing: `a, b, c = [1, 2, 3]`
    - List comprehensions:  `["foo%i" % i for i in range(3)]`

---

# Flow control

- while
  ```python
  a = 0
  while a < 10:
      print(a)
      a += 1
  ```

- [If ...elif...else](https://docs.python.org/3.7/tutorial/controlflow.html#if-statements) 
- [for](https://docs.python.org/3.7/tutorial/controlflow.html#for-statements)
- [range](https://docs.python.org/3.7/tutorial/controlflow.html#the-range-function) (mention python2's `xrange`)
- [break, continue](https://docs.python.org/3.7/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) and [pass](https://docs.python.org/3.7/tutorial/controlflow.html#pass-statements)
- [try-except](https://docs.python.org/3.7/tutorial/errors.html#exceptions) and [using them for flow control](https://docs.python.org/3.7/tutorial/errors.html#handling-exceptions)
  ```python
  for n in range(-5, 5):
    if n == 3:
        continue
    try:
        a = 1 / n
        print(n, a)
    except ZeroDivisionError:
        print(n, '---')
  ```
