from __future__ import annotations
from playhouse.pool import PooledMySQLDatabase, PooledSqliteDatabase

import datetime

from peewee import *
from peewee import CharField

db = PooledMySQLDatabase('test',
                         user='root', password='test',
                         host='localhost', port=3306,
                         max_connections=16,
                         stale_timeout=300)


class DoubanTop250(Model):
    id = PrimaryKeyField()
    name = CharField(default='')
    language = CharField()
    imdb_id = CharField()
    rating_num = DecimalField(default=0.0)
    desc = TextField(default='')
    poster_img_path = CharField(default='')
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db
        table_name = 'douban_top250'
