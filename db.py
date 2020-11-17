import mongoengine

host = 'mongodb://admin:admin@cluster0-shard-00-00.xnyh2.mongodb.net:27017,cluster0-shard-00-01.xnyh2.mongodb.net:27017,cluster0-shard-00-02.xnyh2.mongodb.net:27017/project-hieu?ssl=true&replicaSet=atlas-ctdkuq-shard-0&authSource=admin&retryWrites=true&w=majority'
db_name = "project-hieu"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(
        db_name, 
        host='mongodb://admin:admin@cluster0-shard-00-00.xnyh2.mongodb.net:27017,cluster0-shard-00-01.xnyh2.mongodb.net:27017,cluster0-shard-00-02.xnyh2.mongodb.net:27017/project-hieu?ssl=true&replicaSet=atlas-ctdkuq-shard-0&authSource=admin&retryWrites=true&w=majority',
        username='admin',
        password='admin'
    )
    