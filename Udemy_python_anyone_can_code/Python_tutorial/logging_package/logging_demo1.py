__author__ = 'anna'
import logging
#links:
#https://docs.python.org/3/library/logging.html#logrecord-attributes
#https://docs.python.org/3/library/time.html.html#time.strftime

def log():
    logging.basicConfig(format='%(levelname)s: %(message)s: %(asctime)s',
                        filename='logging_demo1.txt', level=logging.DEBUG, datefmt='%m/%d/%Y %H:%M:%S')
    logging.warning('Warning!')
    logging.info('Info')
    logging.debug('Debug!')


log()
