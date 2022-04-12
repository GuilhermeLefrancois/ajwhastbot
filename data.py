from pymongo import *
from bson.objectid import ObjectId

class Data:
    def connectDB():
        try:
            client = MongoClient("mongodb://sa:200021@aj-wb.hghht.mongodb.net/ajdb?retryWrites=true&w=majority&ssl=true&")
            return client["ajdb"]
        except Exception as exp:
            print(exp.args)

    def rescueUser(username):
        db =  Data.connectDB()
        ret = []
        collection = db["users"]
        for item in collection.find({"username": username}):
            ret.append(item)
        db.client.close()
        return ret

    def rescueMessages():
        db = Data.connectDB()
        ret = []
        collection = db["mensagens"]
        for item in collection.find():
            ret.append({'id': str(item["_id"]), 'descricao': item["descricao"], "funcao": item["funcao"], "mensagem": item["mensagem"]})
        db.client.close()
        return ret

    def rescueMessage(id):
        db = Data.connectDB()
        ret = []
        collection = db["mensagens"]
        print(id)
        for item in collection.find({"_id": ObjectId(id)}):
            ret.append(item)
        db.client.close()
        return ret[0]

    def registerMessage(body):
        try:
            db = Data.connectDB()
            collection = db["mensagens"]
            collection.insert_one(body)
            db.client.close()
            return True
        except Exception as exp:
            return False

    def excluirMessage(id):
        try:
            db = Data.connectDB()
            collection = db["mensagens"]
            collection.delete_one({"_id": ObjectId(id)})
            db.client.close()
            return True
        except Exception as exp:
            return False


    def rescueUsers():
        try:
            db = Data.connectDB()
            ret = []
            collection = db["users"]
            for item in collection.find():
                ret.append({'id': str(item["_id"]), 'username': item["username"]})
            return ret
        except Exception as exp:
            return []

    def registerUser(body):
        try:
            db = Data.connectDB()
            collection = db["users"]
            collection.insert_one(body)
            db.client.close()
            return True
        except Exception as exp:
            return False

    def excluirUser(id):
        try:
            db = Data.connectDB()
            collection = db["users"]
            collection.delete_one({"_id": ObjectId(id)})
            db.client.close()
            return True
        except Exception as exp:
            return False

    def rescueContatos():
        try:
            db = Data.connectDB()
            ret = []
            collection = db["contatos"]
            for item in collection.find():
                print(item)
                ret.append({'id': str(item["_id"]), 'nome': item["nome"], 'telefone': item["telefone"]})
            print(ret)
            return ret
        except Exception as exp:
            return []

    def registerContato(body):
        try:
            db = Data.connectDB()
            collection = db["contatos"]
            collection.insert_one(body)
            db.client.close()
            return True
        except Exception as exp:
            return False

    def excluirContato(id):
        try:
            db = Data.connectDB()
            collection = db["contatos"]
            collection.delete_one({"_id": ObjectId(id)})
            db.client.close()
            return True
        except Exception as exp:
            return False
