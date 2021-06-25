#! /usr/bin/env python3
import logging
import argparse
__version__= '0.1.0'


def logInit(logName, debug = False):
    if debug:
        logLevel = logging.DEBUG
    else:
        logLevel = logging.INFO
    logging.basicConfig(filename=logName,
                        level=logLevel,
                        format='%(asctime)s | %(levelname)-8s | %(name)s | %(module)-8s | %(funcName)-16s | %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    a1 = logging.getLogger('PhD2021')
    return a1  # logging

def main(name):
    logger = logInit('myLog.log')
    logger.info("Inizia il programma")
    print(f"Ciao {name}")
    logger.info("Finisce il programma")
    
if __name__ == '__main__':
    parser=argparse.ArgumentParser(prog="codEx05", description="Software fo the test of parameters")
    parser.add_argument('-v','--version',action='version',help="Show the software version", version=__version__)
    parser.add_argument('name', metavar="NAME",type=str,help="name to print")
    args=parser.parse_args()
    main(args.name)
