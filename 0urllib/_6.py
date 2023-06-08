# 操作 MySQL
# pip install peewee pymysql
from datetime import date

from peewee import *
from playhouse.pool import PooledMySQLDatabase

db = PooledMySQLDatabase('test',
                         user='root', password='test',
                         host='10.10.10.2', port=3306,
                         max_connections=8,
                         stale_timeout=300)


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_deleted = BooleanField()

    class Meta:
        database = db
        table_name = 'tb_person'


def test_create():
    Person.create_table()
    # use Database to create tables
    # db.create_tables([Person])


def test_save():
    person = Person(name='zhang.zzf', birthday=date(1988, 3, 29), is_deleted=False)
    person.save()


def test_update():
    Person.update({Person.birthday: date(1989, 11, 11)}) \
        .where(Person.id == 1) \
        .execute()


def test_query():
    p: Person = Person.select().where(Person.id == 1).get()
    print(p.id, p.name, p.birthday)


if __name__ == '__main__':
    # test_create()
    # test_save()
    # test_update()
    test_query()
