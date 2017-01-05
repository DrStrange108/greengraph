from argparse import ArgumentParser
from .greengraph import greengraph

def process():

    parser = ArgumentParser(description = "Generate Graph of Green Steps")
    parser.add_argument('--origin', '-o')
    parser.add_argument('--destination','-d')
    parser.add_argument('--steps', '-s')
    parser.add_argument('--filename', '-f')
    arguments= parser.parse_args()

    greengraph(arguments.origin, arguments.destination, 
               arguments.steps, arguments.filename)

if __name__ == "__main__":
    process()

