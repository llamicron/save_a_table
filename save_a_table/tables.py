from peewee import *

db = SqliteDatabase('save_a_table.db')

class Table(Model):
    floor = CharField()
    name = CharField()
    # I could use a more efficient data type, but this is a small project
    # and i don't care. The improvement in negligible anyway.
    status = CharField()

    class Meta:
        database = db
