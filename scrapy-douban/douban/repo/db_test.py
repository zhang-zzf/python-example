from __future__ import annotations

from peewee import *
from peewee import CharField

from douban.repo.local_host import db


class DoubanTop250(Model):
    name = CharField(default='')
    language = CharField()
    imdb_id = CharField()
    rating_num = DecimalField(default=0.0)
    desc = TextField()
    poster_img_path = CharField(default='')
    created_at = DateTimeField()
    updated_at = DateTimeField()

    class Meta:
        database = db
        table_name = 'douban_top250'


if __name__ == '__main__':
    pass
