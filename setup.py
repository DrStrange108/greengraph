from setuptools import setup, find_packages

setup(
    name = 'Greengraph',
    description='A tool that generates a graph of proportion of green pixels in a series of satellite images between 2 points',
    version = '1.0',
    author='Kunal Vora',
    author_email='kunal.vora.16@ucl.ac.uk',
    url='https://github.com/kunalvora1/greengraph',
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greengraph'],
    install_requires = ['argparse', 'geopy', 'numpy', 'matplotlib']
)

