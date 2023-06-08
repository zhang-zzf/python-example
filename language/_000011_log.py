import logging
from logging import Logger
from unittest import TestCase

logger: Logger = logging.getLogger(__name__)


class Test(TestCase):

    def test_normal_case(self):
        logger.debug('This message should go to the log file')
        logger.info('So should this')
        logger.warning('And this, too')
        logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
        try:
            1 / 0
        except ZeroDivisionError:
            logger.error("unExpected Error", exc_info=True)
        try:
            1 / 0
        except ZeroDivisionError:
            logger.exception('unExpectedException')
