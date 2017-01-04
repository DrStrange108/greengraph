#!/usr/bin/env python

from matplotlib import pyplot as plt
from greengraph import Greengraph

from argparse import ArgumentParser
if __name__ == "__main__":
    parser = ArgumentParser(description = "Generate Graph of Green Steps")
    parser.add_argument('--from', '-f')
    parser.add_argument('--to','-t')
    parser.add_argument('--steps', '-s')
    parser.add_argument('--out', '-o')
    arguments= parser.parse_args()



mygraph=Greengraph(arguments.from,arguments.to)
data = mygraph.green_between(arguments.steps)

plt.plot(data)
plt.show()





