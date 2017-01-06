# Greengraph
=============
A tool that generates a graph of proportion of green pixels in a series of satellite images between 2 points.

## Useage

usage: greengraph [-h] [--origin] [--destination]
                  [--steps] [--filename]

Generate Graph of Green Pixels between 2 places

optional arguments:
 * -h, --help            show this help message and exit
 * --origin -o
                        Origin (default = London)
 * --destination -d
                        Destination: (default = Coventry)
 * --steps, -s 
                        Steps required - (default = 20)
 * --filename, -f
                        Filename output. (default graph.png)


## Installation

Download this package and run:

**python setup.py install** 

from the command line (NB: May need admin or sudo privileges)

Alternatively

**sudo pip install git+git://github.com/kunalvora1/greengraph**

# Known Issues

Need to fix arge parse input for places with a space (eg'New York').
Need to complete full unit testing and mocks

# Licence
See Licence.MD file

# Author
Kunal Vora email: kunal.vora.16@ucl.ac.uk

