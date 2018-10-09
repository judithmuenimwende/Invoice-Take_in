
from peewee import (Model, CharField, SqliteDatabase, IntegrityError)

DATABASE = SqliteDatabase("invoice.db")


class User(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    company = CharField(max_length=200)

    class Meta:
        database = DATABASE


