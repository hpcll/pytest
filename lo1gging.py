import logging

#　打印日志级别
def logging1():
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')
    logging.error('Python Error')
    logging.critical('Python critical')

if __name__ == '__main__':
    logging1()
