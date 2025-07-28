import time
import unittest
from unittest import TestCase
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class Test(TestCase):

    def test_given_date_time_model_normal_case(self):
        now: datetime = datetime.now()
        now_date: datetime.date = now.date()
        now_time: datetime.time = now.time()
        # timedelta 操作的最大维度为 day
        now_date_10days = now_date + timedelta(days=10)
        now_date_10months = now_date + relativedelta(months=10)
        now_date__10months = now_date - relativedelta(months=10)
        pass

    def test_given_time_model_normal_case(self):
        unix_timestamp: float = time.time()
        now = time.localtime(unix_timestamp)
        print(f'{now.tm_year}年{now.tm_mon}月份');
        pass


if __name__ == '__main__':
    unittest.main()
