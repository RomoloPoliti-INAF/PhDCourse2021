#! /usr/bin/env python3
import logging
import argparse
import pandas as pd
import matplotlib.pyplot as plt
__version__= '0.1.0'


def logInit(logName, debug = False):
    if debug:
        logLevel = logging.DEBUG
    else:
        logLevel = logging.INFO
    logging.basicConfig(filename=logName,
                        level=logLevel,
                        filemode='a',
                        format='%(asctime)s | %(levelname)-8s | %(name)s | %(module)-8s | %(funcName)-16s | %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    a1 = logging.getLogger('PhD2021')
    return a1  # logging

def main(file, debug):
    logger = logInit('myLog.log', debug)
    logger.info("Inizia il programma")
    logger.debug(f"leggo il file {file}")
    df= pd.read_csv(file, index_col=0)
    df.plot(x="Azimut",y="Elevazione", kind='line')
    plt.show()
    # plt.savefig('../output/sun.png')
    logger.info("Finisce il programma")
    
if __name__ == '__main__':
    parser=argparse.ArgumentParser(prog="codEx08", description="Software fo the test of parameters")
    parser.add_argument('-v','--version',action='version',help="Show the software version", version=__version__)
    parser.add_argument('-f', '--file', metavar="NAME",type=str,help="filename to print", default='../data/SunPathDaily_40.3350551_18.1112515_1624612273248.csv')
    parser.add_argument('-d','--debug', action='store_true', help = 'abilita il debug', default= False)
    args=parser.parse_args()
    main(args.file, args.debug)
