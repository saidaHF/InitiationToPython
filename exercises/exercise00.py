
"""
Exercise 0 (format conversor).
------------------------------

Download the file [sp8c.dat](exercises/sp8c.dat) and save it in your working 
directory:

It is a positron-decay spectrum (counts as a function of time) saved in ASCII 
with a 3-line header and the data packed in 8 columns.

The header contains the information needed to reconstruct the time scale 
(in ps):

`time = ChannelNumber * GAIN + OFFSET`

The exercise is done in two parts:

1. Assume that you know beforehand that the header has 3 lines and that the 
gain is 50.0 and the offset is 1000 ((i.e., you can skip reading the header).
Write a python script that writes converted data to a file called "sp2c.dat"
in 2 columns where:
  - There is no header
  - column 1 is the time
  - column 2 is the number of counts normalised by the maximum value of counts


2. Modify the program you did in part 1 but assuming that you need to read the 
header. Particularly, not only the GAIN and OFFSET items may have different 
values, but also the order of the items in the header can vary and there could
be more items in the header (it won't always be 3 lines). The marker for 
end-of-header is the keyword "DATA".


Important: do not import modules. Do it with the basic python built-in 
functions.

Tips:

- for opening the file see the open() function (do "help(open)" or "open?" 
  in ipython)
- for reading the file see: file.readlines()
- for writing, see file.write() and file.close()
- Use the function str.split() and float() to obtain the data as separate 
  numerical values (instead of strings).
- [Official Solution](exercises/cheat/exercise00.py)

"""

# Write your solution here