#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# import the needed libraries/packages
import logging
import time
import csv
import jinja2

# define globals/contants



def create_report():
    pass



def main():
    """ Primary Entry-point for program """

    # setup logging information so we get some nicely-formatted output
    logging.basicConfig(format='[%(asctime)s] %(levelname)s %(message)s', level=logging.INFO)
    logging.info('** Annual Report Generation Utility **')
    start_time = time.time()
  
    # actually generate the report    
    create_report()

    logging.info("Script Finished")
    logging.info("Elapsed Time: %s seconds ", (time.time() - start_time))


# stub to call the main if this script file is called 
# by itself (vs. being included into a different script)
if __name__ == '__main__':
    main()
