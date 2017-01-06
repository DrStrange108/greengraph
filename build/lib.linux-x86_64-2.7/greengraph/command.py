#!/usr/bin/env python

from matplotlib import pyplot as plt
from greengraph import Greengraph
from argparse import ArgumentParser

def process():
    parser = ArgumentParser(description = "Generate Graph of Green Pixels between 2 places")
    parser.add_argument('--origin', '-o', default='London', help="Origin (default = London)")
    parser.add_argument('--destination','-d', default= 'Coventry', help="Destination: (default = Coventry)")
    parser.add_argument('--steps', '-s', default='20', help="Steps required - (default = 20)")
    parser.add_argument('--filename', '-f', help="Filename output. (default graph.png if not entered)", default='graph.png')
    arguments= parser.parse_args()

    mygraph=Greengraph(arguments.origin,arguments.destination)
    data = mygraph.green_between(arguments.steps)

    plt.plot(data)
    #  Add custom title for graph
    title = "Green Pixels Between " + arguments.origin + " & " +       arguments.destination + " in " + arguments.steps+ " steps"

    plt.title(title)
    plt.xlabel('Steps')
    plt.ylabel('Green Pixels')
    plt.savefig(arguments.filename)
    plt.show()

if __name__ == "__main__":
    process()

# Got it to work after removing arguments.from (turns out it's a keyword in python)
# Need to add argparse fix for names with spaces to work (eg: New York)





