#!/usr/bin/env python
from matplotlib import pyplot as plt
from greengraph import greengraph
from argparse import ArgumentParser

#  ARE INDENTS CORRECT???
def greengraph(origin, destination, steps, filename):

    """ Generate's a Graph of Green pixels from two cities using Google Map's API.

    Parameters
    ----------
    origin: str
        The starting point (eg: London)
    destination: str
        The end point (eg: Coventry)
    steps: str
        The number of steps between start and end point (default is 20)
    filename: str
        Optional argument to change filename of graph (default will show graph in GUI and give option to save)
  
    Returns
    -------
    Graph
        Graph of Green Pixels from the 2 points specified.
    """


    if __name__ == "__main__":
    	parser = ArgumentParser(description = "Generate Graph of Green Steps")
    	parser.add_argument('--origin', '-o')
    	parser.add_argument('--destination','-d')
    	parser.add_argument('--steps', '-s')
    	parser.add_argument('--filename', '-f', default='graph.png')
    	arguments= parser.parse_args()


	mygraph=Greengraph(arguments.origin,arguments.destination)
	data = mygraph.green_between(arguments.steps)

	plt.plot(data)
	#  Add custom title for graph
	title = "Green Pixels Between " + arguments.origin + " & " + 		arguments.destination + " in " + arguments.steps+ " steps"

	plt.title(title)
	plt.xlabel('Steps')
	plt.ylabel('Green Pixels')
	plt.savefig(arguments.filename)
	plt.show()
