# from peewee import *
from peewee import SqliteDatabase, Model, CharField, DateField, ForeignKeyField

# 路径写死了，待解决：怎么不写死
db = SqliteDatabase('/Users/chenag/Documents/PycharmProjects/python_peewee_demo' + '/quickstart/people.db')


class Person(Model):
    class Meta:
        database = db

    name = CharField()
    birthday = DateField()


class Pet(Model):
    class Meta:
        database = db

    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()


db.connect()
db.create_tables([Person, Pet])