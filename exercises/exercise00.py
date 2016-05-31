#!/usr/bin/env python


# Solutions to scipy course
# By carlos.pascual@cells.es

"""
Exercise 0 (format conversor).
==============================

Download the file sp8c.dat and save it in your working directory:

http://www.cells.es/Intranet/Divisions/Computing/Controls/howto/scipy/sp8c.dat

It is positron-decay spectrum (counts as a function of time) saved in ASCII 
with a 3-line header and the data packed in 8 columns.

The header contains the information needed to reconstruct the time scale 
(in ps):

time = ChannelNumber * GAIN + OFFSET

Part 1:
-------

Assume that you know beforehand that the header has 3 lines and that the 
gain is 50.0 and the offset is 1000 ((i.e., you can skip reading the header).
Write a python script that writes converted data to a file called "sp2c.dat"
in 2 columns where:

- There is no header
- column 1 is the time
- column 2 is the number of counts normalised by the maximum value of counts


Part 2:
-------

Modify the program you did in Part 1but assuming that you need to read the 
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

"""


inputfilename='sp8c.dat'  
outputfilename='sp2c.dat'

# read the spectrum
f = open(inputfilename,"r")
text = f.read() # the whole file is read as text
f.close()
words = text.split() # we split on white space (includes blanks, tabs,...)

offset = float(words[1+words.index('OFFSET')])
gain = float(words[1+words.index('GAIN')])
data = [float(w) for w in words[1 + words.index('DATA'):] ]  # note the ':' 

# calculate time and normalised counts
time = [(i * gain + offset) for i in range(len(data))]
maxdata = max(data)
normalised = [d/maxdata for d in data]

# write to output file
f = open(outputfilename,'w')
for i in range(len(data)):  # note: think how to do this for-loop using zip()
    f.write('%f\t%f\n' % (time[i], normalised[i]))
f.close()

raw_input('press enter to finish') # useful when launching outside a console
