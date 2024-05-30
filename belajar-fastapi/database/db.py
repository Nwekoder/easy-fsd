from peewee import PostgresqlDatabase, Model

db = PostgresqlDatabase('belajar_fastapi', user="nwekoder", password="c1250425", host="127.0.0.1", port=5432)

class BaseModel(Model):
    class Meta:
        database = db