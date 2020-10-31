from mongoengine import *
from models.user import User

def create_user(email, password, firstname, lastname, phone):
    all_user = User.objects(email=email)

    if len(all_user) > 0:
        return False
    else:
        try:
            new_user = User(
                email = email,
                password = password,
                firstname = firstname,
                lastname = lastname,
                phone = phone
            ) 
            new_user.save()
            return True
        except:
            return False

def validate_user(email, password):
    found_user = User.objects(email=email,password=password)
    if found_user:
        found_user = User.objects.get(email=email,password=password)
        return found_user
    else:
        return False

