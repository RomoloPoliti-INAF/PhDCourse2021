#! /usr/bin/env python3
import logging
import argparse
import pandas as pd
__version__= '0.1.0'


def logInit(logName, debug = False):
    if debug:
        logLevel = logging.DEBUG
    else:
        logLevel = logging.INFO
    logging.basicConfig(filename=logName,
                        level=logLevel,
                        filemode='w',
                        format='%(asctime)s | %(levelname)-8s | %(name)s | %(module)-8s | %(funcName)-16s | %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    a1 = logging.getLogger('PhD2021')
    return a1  # logging

def main(file, debug):
    logger = logInit('myLog.log', debug)
    logger.info("Inizia il programma")
    logger.debug(f"leggo il file {file}")
    df= pd.read_csv(file)
    print(df)
    logger.info("Finisce il programma")
    
if __name__ == '__main__':
    parser=argparse.ArgumentParser(prog="codEx07", description="Software fo the test of parameters")
    parser.add_argument('-v','--version',action='version',help="Show the software version", version=__version__)
    parser.add_argument('-f', '--file', metavar="NAME",type=str,help="filename to print", default='../data/testData01.csv')
    parser.add_argument('-d','--debug', action='store_true', help = 'abilita il debug', default= False)
    args=parser.parse_args()
    main(args.file, args.debug)
