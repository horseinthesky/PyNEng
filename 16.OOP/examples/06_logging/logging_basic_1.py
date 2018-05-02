import logging

logging.basicConfig(level=logging.DEBUG)

vara = 'TEST'
varb = "dhcp_snooping.db"

logging.debug('Сообщение уровня debug %s', vara)
logging.info('Сообщение уровня info {}'.format(varb))
logging.warning('Сообщение уровня warning')
