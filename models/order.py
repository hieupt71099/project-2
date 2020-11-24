from mongoengine import *
from models.helper import mongo_to_dict

class CartItem(Document):
    product_id: StringField()
    category: StringField()
    name: StringField()
    price: IntField()
    quantity: IntField()

    def to_dict(self):
        return mongo_to_dict(self)

class Order(Document):
    user_id = StringField()
    fullname = StringField()
    email = EmailField()
    phone = StringField()
    address = StringField()
    total_price = IntField()
    total_quantity = IntField()
    status = StringField()
    order_time = IntField(default=0)
    item_list = ListField(ReferenceField(CartItem))

    def to_dict(self):
        return mongo_to_dict(self)