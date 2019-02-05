from mongoengine import Document, StringField, DateTimeField, IntField, ImageField, FileField, FloatField
from datetime import datetime

class Order(Document):
    book = StringField()
    cash = FloatField()
    user_name = StringField()
    user_email = StringField()
    user_phone = StringField()
    user_adress = StringField()
    data = DateTimeField(default=datetime.utcnow())
