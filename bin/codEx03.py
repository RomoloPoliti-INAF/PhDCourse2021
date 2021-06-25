#! /usr/bin/env python3
import argparse
__version__= '0.1.0'

def example(name):
    print(f"Ciao {name}")
    
if __name__ == '__main__':
    parser=argparse.ArgumentParser(prog="codEx03", description="Software fo the test of parameters")
    parser.add_argument('-v','--version',action='version',help="Show the software version", version=__version__)
    parser.add_argument('name', metavar="NAME",type=str,help="name to print")
    args=parser.parse_args()
    example(args.name)