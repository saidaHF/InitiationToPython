#!/usr/bin/env python

# solution by cpascual@cells.es

"""
Exercise: converter1
--------------------

Make sure that you work on the "exercises" directory and that it contains
the file named `sp8c.dat`

The file sp8c.dat contains the data of a positron-decay spectrum (detector
counts as a function of time) saved in ASCII with the following format:

- A 3-line header that provides the information to construct the time values
(in ps):

`time = ChannelNumber * GAIN + OFFSET`

- the values of the counts for 256 channels, written as 8 channels per row.

For this exercise, assume that you know beforehand that the header has 3 lines
and that the gain is 50.0 and the offset is 1000 (i.e., you do not need to
process the data in the header and you can skip the first 3 lines).

Write a python script that writes converted data to a file called
"converted1.dat" with 2 columns where:
  - There is no header
  - Column 1 is the time (calculated as `time = channel_index * 50 + 1000` )
  - Column 2 is the number of counts normalised by the maximum value of counts
    in the input data

Important: do not import modules. Do it using the basic python built-in
functions (https://docs.python.org/2/library/functions.html ).

Tips:

- for opening the file see the open() function (do "open?" in ipython)
- for reading the file see: file.read()
- for writing, see file.write() and file.close()
- use the str.split() method to split a string into a list of "words"
- use float() to convert a string that represents a number to the number itself
- use max() to find the largest number in a list of numbers
- [Official Solution](exercises/cheat/converter1.py)

"""

# Write your solution here
