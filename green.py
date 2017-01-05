#!/usr/bin/env python

from matplotlib import pyplot as plt
from greengraph import Greengraph

from argparse import ArgumentParser
if __name__ == "__main__":
    parser = ArgumentParser(description = "Generate Graph of Green Steps")
    parser.add_argument('--origin', '-o')
    parser.add_argument('--destination','-d')
    parser.add_argument('--steps', '-s')
    parser.add_argument('--filename', '-f', default='graph.png')
    arguments= parser.parse_args()


    variables = arguments.origin + " " + arguments.destination + " " + arguments.steps+ " " + arguments.filename
 
    print variables  # Remove Testing Variables

mygraph=Greengraph(arguments.origin,arguments.destination)
data = mygraph.green_between(arguments.steps)

plt.plot(data)
plt.savefig(arguments.filename)
plt.show()

# Got it to work after removing arguments.from (turns out it's a keyword in python)
# Need to add argparse fix for names with spaces to work (eg: New York)





