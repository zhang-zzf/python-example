#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import peewee
import datetime

db = peewee.SqliteDatabase('test.db')


class Note(peewee.Model):
    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:
        database = db
        db_table = 'notes'


if __name__ == '__main__':
    data = [
        {'text': 'a'},
        {'text': 'b'},
        {'text': 'c'},
    ]
    with db.atomic():
        many = Note.insert_many(data)
        print(many.sql())
        many.execute()
