import mongoengine

host = 'mongodb+srv://admin:admin@thanhcluster-soioj.mongodb.net/project-hieu?retryWrites=true&w=majority'
db_name = "project-hieu"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(
        db_name, 
        host='mongodb+srv://admin:admin@cluster0.xnyh2.mongodb.net/project-hieu?retryWrites=true&w=majority',
        username='admin',
        password='admin'
    )
    