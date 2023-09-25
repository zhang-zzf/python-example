import logging
import unittest
from datetime import datetime
from unittest import TestCase

from peewee import ModelSelect, Select

from _peewee.config import LogConfig
from _peewee.db_mysql_localhost import DoubanPO


class Douban:
    def __init__(self, imdb_id: str, name: str = ''):
        self.imdb_id = imdb_id
        self.name = name
        self.created_at = datetime.now()


class Test(TestCase):

    def setUp(self):
        LogConfig().load_log_cfg()
        # logger = logging.getLogger('peewee')
        # logger.addHandler(logging.StreamHandler())
        # logger.setLevel(logging.DEBUG)

    def test_save_from_obj(self):
        item = {
            'id': 1,
            'imdb_id': 'imdb:item',
            'created_at': datetime.now()
        }
        po = DoubanPO(**item)
        logging.info(f'DoubanPo.save() req -> {po}')
        # Returns: Number of rows modified.
        # Save the data in the model instance.
        # By default, the presence of a primary-key value will cause an **UPDATE** query to be executed
        # 更新的时候会更新 **所有** 字段
        saved: int = po.save()
        logging.info(f'DoubanPo.save() resp -> {saved}')

    def test_save_from_domain_model(self):
        douban = Douban('imdb:domain_model')
        item = douban.__dict__
        DoubanPO(**item).save()

    def test_save_by_imdb_id_no_tx(self):
        po = DoubanPO(imdb_id='imdb:save_by_imdb_id_no_tx')
        saved = po.save_by_imdb_id_no_tx()
        logging.info(f'test_save_by_imdb_id_tx resp -> {saved}')

    def test_save_by_imdb_id_tx(self):
        po = DoubanPO(imdb_id='imdb:save_by_imdb_id_tx')
        logging.info(f'test_save_by_imdb_id_tx req -> {po}')
        saved, row_id = po.save_by_imdb_id_with_tx()
        logging.info(f'test_save_by_imdb_id_tx resp -> {saved}, {row_id}')

    def test_save_by_imdb_id_ctx_tx(self):
        po = DoubanPO(imdb_id='imdb:save_by_imdb_id_ctx_tx')
        saved = po.save_by_imdb_id_with_ctx_tx()
        logging.info(f'test_save_by_imdb_id_ctx_tx resp -> {saved}')

    def test_save_by_imdb_id_ctx_tx_and_lock(self):
        po = DoubanPO(imdb_id='imdb:save_by_imdb_id_tx_and_lock')
        saved, row_id = po.save_by_imdb_id_with_tx_and_lock()
        logging.info(f'save_by_imdb_id_tx_and_lock resp -> {saved}, {row_id}')

    def test_select_one(self):
        query: ModelSelect = DoubanPO.select().where(DoubanPO.imdb_id == 'imdb:domain_model')
        # first() == get_or_none()
        db_data: DoubanPO = query.first()
        logging.info(f'select by imdb_id resp -> {db_data}')
        pass

    def test_select_list(self):
        query: Select = DoubanPO.select().where(DoubanPO.imdb_id == 'imdb:domain_model')
        for doubanPO in query.execute():
            logging.info(f'select by imdb_id list resp -> {doubanPO}')
        pass

    def test_delete_all(self):
        DoubanPO.delete().execute()


if __name__ == '__main__':
    unittest.main()
