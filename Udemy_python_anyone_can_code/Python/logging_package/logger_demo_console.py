__author__ = 'anna'

import logging

class LoggerDemoConsole():

    def test_log(self):

        #logger will take a string from the log and create a logger object from it and pass it to the handler
        logger = logging.getLogger('Sample_log')
        logger.setLevel(logging.INFO)

        #handler is responsible for the output and pass it to the formatter
        #here is output to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        #formatter will take the output from handler and format it in the way we want and output it
        formatter = logging.Formatter('%(asctime)s', '%(levelname)s: %(message)s: %(name)s',
                                      datefmt='%m/%d/%Y %H:%M:%S')

        #pass the formatter to the console handler
        console_handler.setFormatter(formatter)

        # pass the handler to the logger
        logger.addHandler(console_handler)

        logging.debug('Debug')
        logging.info('Info')
        logging.warning('Warning')
        logging.error('Error')
        logging.critical('Critical')

demo = LoggerDemoConsole()
demo.test_log()





