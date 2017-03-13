__author__ = 'anna'

import logging


def logger_demo_console():

    #logger will take a string from the log and create a logger object from it and pass it to the handler
    logger = logging.getLogger(logger_demo_console.__name__)
    logger.setLevel(logging.DEBUG)

    #handler is responsible for the output and pass it to the formatter
    #here is output to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    #formatter will take the output from handler and format it in the way we want and output it
    formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    #pass the formatter to the console handler
    console_handler.setFormatter(formatter)

    # pass the handler to the logger
    logger.addHandler(console_handler)

    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')

logger_demo_console()

