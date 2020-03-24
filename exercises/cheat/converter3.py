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


def split_file(name):
    """
    Accepts the name of a positron anihilation file and returns a tuple
    containing the header and the channel values
    """
    f = open(name, "r")
    text = f.read()  # the whole file is read as text
    f.close()
    header_text, data_text = text.split("DATA")
    data_words = data_text.split()
    channels = [int(w) for w in data_words]
    return header_text, channels


def parse_header(header):
    """
    accepts the header text and returns a dictionary contaiining "gain" and
    "offset" read from the header
    """
    ret = {}
    words = header.split()
    ret["offset"] = float(words[1 + words.index("OFFSET")])
    ret["gain"] = float(words[1 + words.index("GAIN")])
    return ret


def write_2columns(data, gain=1, offset=0, norm=None, name="converted3.dat"):
    """
    writes a two-column normalized positron anihilation spectrum file.
    It accepts the following arguments:

    - "data": the channel data as a sequence of numbers. Mandatory.
    - "gain": the gain (default = 1)
    - "offset": the offset (default = 0)
    - "norm": the normalization value (default= max(data) )
    - "name": the name of the output file (default "converted3.dat")
    """
    if norm is None:
        norm = max(data)
    f = open(name, "w")
    for i, d in enumerate(data):
        f.write("{x:f}\t{y:f}\n".format(x=i * gain + offset, y=d / norm))
    f.close()


# Process the input file
header, channels = split_file("../sp8c.dat")
parameters = parse_header(header)

# write output (note that I can leave norm and name at their defaults)
write_2columns(channels, gain=parameters["gain"], offset=parameters["offset"])
