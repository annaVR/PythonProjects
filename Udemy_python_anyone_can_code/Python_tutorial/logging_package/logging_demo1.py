__author__ = 'anna'
import logging

def log():
    logging.basicConfig(format='%(levelname)s: %(message)s: functionName %(funcName)s: %(asctime)s',
                        filename='logging_demo1.txt', level=logging.DEBUG, datefmt='%m/%d/%Y %H:%M:%S')
    logging.warning('Warning!')
    logging.info('Info')

log()
