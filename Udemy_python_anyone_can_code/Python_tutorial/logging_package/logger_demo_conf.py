__author__ = 'anna'

import logging
import logging.config

class LoggerDemoConf(object):

    def test(self):

        #create logger
        logging.config.fileConfig('logging.conf')
        # in the configuration file defined that output is going to test.log file - no output to console
        logger = logging.getLogger(LoggerDemoConf.__name__)

        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')



demo = LoggerDemoConf()
demo.test()