#!/usr/bin/env python

# solution by cpascual@cells.es

"""
Exercise: converter3
--------------------

Refactor your solution to exercise converter2 to use functions:

- Create a function called `split_file` that accepts the name of the
input file as its only argument and returns 2 values:
  1. the whole header as a single text (the "DATA" keyword can be omitted)
  2. a list of integers corresponding to the data values

- Create a function called `parse_header` that accepts the header text and
returns a dictionary with 2 keys: "gain" and "offset" , whose values are the
corresponding float values obtained from the header as in exercise converter2

- Create a function called "write_2columns" that writes the output file as
in exercise converter2 and which accepts the following arguments:
  - "data": the channel data as a sequence of integers. this argument is mandatory
  - "gain": the gain. This argument is optional and its default value is 1
  - "offset": the offset. This argument is optional and its default value is 0
  - "norm": the normalization value. This argument is optional and if not
     given, it will be calculated as the max of data
  - "name": the name of the output file. This argument is optional and its
    default value is "converted3.dat"

- Use the functions mentioned above to do the same as in exercise converter2
(except that the output file should now be called "converted3.dat")

Tips:

- see tips of exercise converter1 and converter2 and also...
- remember that the default value of a keyword argument should never be
  a mutable object (such as a list, dict, etc). Use None in this cases and
  check it in the function.


"""

# Write your solution here
