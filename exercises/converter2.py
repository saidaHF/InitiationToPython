#!/usr/bin/env python

# solution by cpascual@cells.es

"""
Exercise: converter2
---------------------

Same as exercise converter1 but this time you need to parse the header
to obtain the values for the gain and the offset from there.

Also, you cannot assume that the header has just 3 lines or that the order
of the items in the header is always the same.

In summary: you know that the "gain" is the number just after the word "GAIN"
and the offset is the number after word "OFFSET". You also know that the word
"DATA" marks the end of the header and that after it it comes the channels
data.

If possible, try not to use `for i in len(range(...))`. Use "enumerate" and
"zip" instead.

Note: call the output of this program "converter2.dat", and compare it
(visually) with "converted1.dat"

Important: do not import modules. Do it with the basic python built-in
functions.

Tips:

- see tips of exercise converter1 and also
- note that you can find elements in a list using the .index() method of a list

"""

# Write your solution here
