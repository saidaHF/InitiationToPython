# Python intro course

The following is just an check-list of topics to cover, with references to other tutorials

These slides are available online in:

https://alba-synchrotron.gitlab.io/controls-section/pythoncourse-intro/

And their source is in:

https://gitlab.com/alba-synchrotron/controls-section/pythoncourse-intro/

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
    
For this course we will use conda (see the pre-course info)
but if you use reasonably recent linux distro, you may 
alternatively also install the packages from the official repositories

## Which version of python (2.x vs 3.x)?: 

- As a general rule, (at the time of writing, December 2020)
  we recommend using at least 3.7
- ... or 3.5 if you need to run code on a debian stretch (e.g. in ALBA debian machines)
- ... or 2.7 only if you need to run code in very old machines (e.g. old SuSe machines at ALBA)

The interactive examples in this course will be run with python 3.7

---

# Interactive mode vs scripts

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
- [range](https://docs.python.org/3.7/tutorial/controlflow.html#the-range-function) (mention python2"s `xrange`)
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
        print(n, "---")
  ```

---

# Flow control (avoid old habits)

```python
# print the following city names...
cities = ["Barcelona", "Sydney", "Boston"]
```

:-(  
```python
i = 0
while i < 3:
    print(cities[i])
    i += 1
```

:-/
```python
for i in range(len(cities)):
    print(cities[i])
```

:-)
```python
for city in cities:
    print(city)
```

---

# Flow control (some tricks)

### zipping
```python
cities = ["Paris", "Delhi", "Boston"]
countries = ["France", "India", "USA"]

for city, country in zip(cities, countries):
    print(city, country)
```
```console
Paris France
Delhi India
Boston USA
```

### enumerating
```python
cities = ["Paris", "Delhi", "Boston"]

for i, city in enumerate(cities):
    print(i, city)
```
```console
0 Paris
1 Delhi
2 Boston
```

### reversing
```python
cities = ["Paris", "Delhi", "Boston"]

for city in cities[::-1]:
    print(city)
```
```console
Boston
Delhi
Paris
```

---

# functions

- [defining functions](https://docs.python.org/3.7/tutorial/controlflow.html#defining-functions):
    - `def f1(): print("hello")`
    - `def f2(): return 5`
    - passing arguments
    - keyword arguments
    - multiple return values (unpacking )

```python
def foo(x, n=2):
    return x**n
```

---

# modules 
- [modules](https://docs.python.org/3.7/tutorial/modules.html#more-on-modules) and [packages](https://docs.python.org/3.7/tutorial/modules.html#packages)
- Importing:
    - `import foo`
    - `import foo.bar`
    - `from foo import bar`
    - `import foo as oof`
- [Interesting modules](https://docs.python.org/3.7/tutorial/stdlib.html): os, sys, datetime, glob, re,... 
- custom modules
    - `if __name__ == "__main__":...`
    - relative imports (`import .bar`)


---

# File I/O

- [ascii IO](https://docs.python.org/3.7/tutorial/inputoutput.html#reading-and-writing-files)
    - `f = open(...)` + `f.close()`
    - `f.read()`
    - `f.readlines()`
    - `f.write()`
    - `f.flush()`
    - `with open(...) as f`

---

# numpy, scipy, plotting

References:
- Numpy tutorial NP:
    - https://docs.scipy.org/doc/numpy/user/quickstart.html
- Matplotlib tutorial :MPL
    - http://matplotlib.org/users/pyplot_tutorial.html
- Matlab to Python conversion:
    - https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html
- scipy recipes:
    - http://scipy-cookbook.readthedocs.io/

---

# numpy
### https://docs.scipy.org/doc/numpy/user/quickstart.html
- numpy VS scipy VS pylab VS matplotlib
- Concept of arrays. Differences with lists and tuples
- dtype, shape, ndim 
- Array creation 
    - `array()`
    - `ones`, `zeros`, `arange`, `linspace`, `rand`
- operations 
    - arithmetic: `a + b`, `a * b`, `dot(a, b)`
    - `sum`, `max`, `argmax`, ...
    - `reshape`, `transpose`
    - `hstack`, `vstack`, `column_stack`
- slicing:
    - Using slice notation:  `a[3:50:2,1:6,-2]`
    - Using array of booleans:  `a[a>2]`
    - Using list of indices:  `a[[1, 2, 3, 5, 7, 11]]`
- `loadtxt`, `savetxt`

---

# matplotlib.pyplot

- basic plotting (see http://matplotlib.org/users/pyplot_tutorial.html) 
  ```python
  from matplotlib import pyplot
  import numpy
  x = numpy.linspace(-6, 6, 100)
  y = numpy.sin(x)
  pyplot.plot(x, y, "r--")
  pyplot.show()
  ```

---
 
# PyTango, Taurus, Sardana

## PyTango vs Taurus vs Taurus Core vs Sardana
- PyTango:
    - http://pytango.readthedocs.io
- Taurus.core: 
    - http://taurus-scada.org/devel/core_tutorial.htmll
- Taurus (For widgets)
    - http://www.taurus-scada.org/users/introduction.html
- Sardana (The whole control system)
    - http://www.sardana-controls.org

---
 
## PyTango

https://pytango.readthedocs.io/en/stable/quicktour.html

```python
>>> import tango
>>> dev = tango.DeviceProxy("sys/tg_test/1") 
>>> dev.status()
"The device is in RUNNING state."
>>> att = dev["float_scalar"]
>>> att.value
46.0    
>>> dev.write_attribute("float_scalar", 12.3)
```

---
 
## Taurus

- Taurus.core: 
    - http://www.taurus-scada.org/devel/core_tutorial.html
    - 
    ```python
    >>> import taurus
    >>> dev = taurus.Device("sys/tg_test/1") 
    >>> dev.status()
    "The device is in RUNNING state."
    >>> att = taurus.Attribute("sys/tg_test/1/float_scalar")
    >>> att.read().rvalue
    46.0 mm
    >>> att.write(123.4)
    ```
- Taurus (For widgets)
    - http://www.taurus-scada.org/users/introduction.html

- `taurus newgui`
    - http://taurus-scada.org/users/ui/taurusgui.html




