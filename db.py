import mongoengine

db_name = "project-hieu"
user_name = "admin"
password = "admin"
# host = f'mongodb+srv://{user_name}:{password}@cluster0.xnyh2.mongodb.net/{db_name}?retryWrites=true&w=majority'
host = 'mongodb://admin:admin@cluster0-shard-00-00.xnyh2.mongodb.net:27017,cluster0-shard-00-01.xnyh2.mongodb.net:27017,cluster0-shard-00-02.xnyh2.mongodb.net:27017/project-hieu?ssl=true&replicaSet=atlas-ctdkuq-shard-0&authSource=admin&retryWrites=true&w=majority'


def connect():
    import certifi
    ca = certifi.where()

    mongoengine.connect(
        db_name, 
        host=host,
        username='admin',
        password='admin',
        tlsCAFile=certifi.where()
    )
    