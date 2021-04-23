import logging

logger = logging.getLogger('scheduler')
_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(module)s - %(lineno)d')


fh = logging.FileHandler('scheduler_log.log', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(_formatter)

cr = logging.FileHandler('error.log', encoding='utf-8')
cr.setLevel(logging.ERROR)
cr.setFormatter(_formatter)

logger.addHandler(fh)
logger.addHandler(cr)
logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    logger.info('Info')
    logger.warning('Warning')
    logger.debug('debug')
    logger.error('error')
    logger.critical('critical')
