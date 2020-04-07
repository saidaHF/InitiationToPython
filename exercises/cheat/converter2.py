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

input_file_name = "../sp8c.dat"  # I use "../" because it is in the parent dir
output_file_name = "converted2.dat"

# read the spectrum
f = open(input_file_name, "r")
text = f.read()  # the whole file is read as text
f.close()
words = text.split()  # we split on white space (includes blanks, tabs,...)

# find values for offset and gain
offset = float(words[1 + words.index("OFFSET")])
gain = float(words[1 + words.index("GAIN")])

# assume that data is anything that comes after the keyword DATA
data = [float(w) for w in words[1 + words.index("DATA") :]]  # note the ':'

# find the maximum
max_data = max(data)  # we do this outside the loop because it won't change

# write to output file (calculating time and normalisation while writing)
f = open(output_file_name, "w")
for i, d in enumerate(data):
    f.write("{x:f}\t{y:f}\n".format(x=i * gain + offset, y=d / max_data))
f.close()
