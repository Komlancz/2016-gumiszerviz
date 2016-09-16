from peewee import *

db = PostgresqlDatabase('gumiszerviz', user='komlancz')
print ("Database: ", db)


class BaseModel(Model):
    class Meta:
        database = db