import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

conso = logging.StreamHandler()
conso.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')
conso.setFormatter(formatter)
logger.addHandler(conso)

logger.info('Logger started')
#logger.warning('warning message')
#logger.error('err message')
#logger.critical('critical message')