__author__ = 'anna'

import logging
from . import custom_logger as cl

class LoggingDemo2():

    log = cl.CustomLogger(logging.DEBUG)

    def method1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warn('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        method2_log = cl.CustomLogger(logging.INFO)
        method2_log.debug('debug message')
        method2_log.info('info message')
        method2_log.warn('warn message')
        method2_log.error('error message')
        method2_log.critical('critical message')

    def method3(self):
        method3_log = cl.CustomLogger(logging.WARNING)
        method3_log.debug('debug message')
        method3_log.info('info message')
        method3_log.warn('warn message')
        method3_log.error('error message')
        method3_log.critical('critical message')

demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()