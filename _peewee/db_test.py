from __future__ import annotations

import json

from peewee import *
from peewee import CursorWrapper

from local_host import db


class DoubanPO(Model):
    id = PrimaryKeyField()
    name = CharField(default='')
    language = CharField()
    imdb_id = CharField()
    rating_num = DecimalField(default=0.0)
    desc = TextField()
    poster_img_path = CharField(default='')
    created_at = DateTimeField()
    updated_at = DateTimeField()

    # imdb_id 是业务唯一主键, 数据库没有唯一索引
    # TODO 使用 select *** for update 原子更新
    # 假设 model 中包含全部字段的数据
    @db.atomic()  # TODO 已验证：事务生效
    def save_by_imdb_id_with_tx_and_lock(self) -> (int, int):
        sql = f"select `id` from douban_top250 " \
              f"where imdb_id = %s " \
              f"for update"
        db_raw: CursorWrapper = self.raw(sql, self.imdb_id).execute()
        if db_raw:
            self.id = db_raw[0].id
        return self.save(), self.id

    # imdb_id 是业务唯一主键
    # 数据库没有唯一索引，加上事务不能解决并发问题
    # 假设 model 中包含全部字段的数据
    @db.atomic()  # TODO 已验证：事务生效
    def save_by_imdb_id_with_tx(self) -> (int, int):
        query: Select = self.select(DoubanPO.id).where(DoubanPO.imdb_id == self.imdb_id)
        db_row: DoubanPO = query.first()
        # 验证事务是否生效
        # TODO db_row11 不会发起 SQL 请求
        # TODO db_row1 会重新发起 SQL 请求
        # db_row11: DoubanPO = query.first()
        # db_row1: DoubanPO = self.select(DoubanPO.id, DoubanPO.imdb_id) \
        #     .where(DoubanPO.imdb_id == self.imdb_id) \
        #     .first()
        if db_row:
            self.id = db_row.id  # update db_row
        return self.save(), self.id

    # imdb_id 是业务唯一主键
    # 数据库没有唯一索引，加上事务不能解决并发问题
    # 2 个事务并发保存是可以保存成功的
    # 假设 model 中包含全部字段的数据
    def save_by_imdb_id_with_ctx_tx(self) -> int:
        with db.atomic() as tx:  # TODO 已验证：事务生效
            query: Select = self.select(DoubanPO.id).where(DoubanPO.imdb_id == self.imdb_id)
            db_row: DoubanPO = query.first()
            # 验证事务是否生效
            # TODO db_row11 不会发起 SQL 请求
            # TODO db_row1 会重新发起 SQL 请求
            # db_row11: DoubanPO = query.first()
            # db_row1: DoubanPO = self.select(DoubanPO.id, DoubanPO.imdb_id) \
            #     .where(DoubanPO.imdb_id == self.imdb_id) \
            #     .first()
            if db_row:
                self.id = db_row.id  # update db_row
            return self.save()

    # imdb_id 是业务唯一主键
    # 数据库没有唯一索引，加上事务不能解决并发问题
    # 假设 model 中包含全部字段的数据
    def save_by_imdb_id_no_tx(self):
        query: Select = self.select(DoubanPO.id).where(DoubanPO.imdb_id == self.imdb_id)
        db_row: DoubanPO = query.first()
        # TODO db_row11 不会发起 SQL 请求
        # db_row11 = query.first()
        # TODO db_row1 会重新发起 SQL 请求
        # db_row1: DoubanPO = self.select(DoubanPO.id, DoubanPO.imdb_id) \
        #     .where(DoubanPO.imdb_id == self.imdb_id) \
        #     .first()
        if db_row:
            self.id = db_row.id  # update db_row
        self.save()

    def __str__(self):
        return json.dumps(self.__data__, ensure_ascii=False, sort_keys=True, default=str)

    class Meta:
        database = db
        table_name = 'douban_top250'
