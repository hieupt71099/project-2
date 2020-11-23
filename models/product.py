from mongoengine import *
from models.helper import mongo_to_dict

class Product(Document):
    image = StringField(default="")
    name = StringField(default="")
    category = StringField()
    tag = ListField(StringField())
    description = StringField()
    price = IntField()
    def to_dict(self):
        return mongo_to_dict(self)
    