import mongoengine

host = 'mongodb://admin:admin@cluster0-shard-00-00.xnyh2.mongodb.net:27017,cluster0-shard-00-01.xnyh2.mongodb.net:27017,cluster0-shard-00-02.xnyh2.mongodb.net:27017/project-hieu?ssl=true&replicaSet=atlas-ctdkuq-shard-0&authSource=admin&retryWrites=true&w=majority'
db_name = "project-hieu"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(
        db_name, 
<<<<<<< HEAD
        host='mongodb://admin:admin@cluster0-shard-00-00.xnyh2.mongodb.net:27017,cluster0-shard-00-01.xnyh2.mongodb.net:27017,cluster0-shard-00-02.xnyh2.mongodb.net:27017/project-hieu?ssl=true&replicaSet=atlas-ctdkuq-shard-0&authSource=admin&retryWrites=true&w=majority',
=======
        host='mongodb+srv://admin:admin@cluster0.xnyh2.mongodb.net/project-hieu?retryWrites=true&w=majority',
>>>>>>> 20e51d6c4a6f7562fd9428cfa89c7585ce97ab69
        username='admin',
        password='admin'
    )
    