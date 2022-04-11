from data import *
from fastapi import HTTPException
from bot import *

class Engine:

    async def login(request):
        try:
            body = await request.json()
            result = Data.rescueUser(body["username"])
            if(result == None or len(result) != 1):
                raise HTTPException(status_code=401, detail="Usuário Não encontrado!")
            else:
                if(result[0]["password"] != body["password"]):
                    raise HTTPException(status_code=401, detail="Credenciais Inválidas")
                else:
                    return True
        except Exception as exp:
            raise exp


    async def rescueMessages():
        try:
            return Data.rescueMessages()
        except Exception as exp:
            raise exp

    async def rescueMessage(id):
        try:
            return Data.rescueMessage(id)
        except Exception as exp:
            raise exp

    async def registerMessage(request):
        try:
            body = await request.json()
            return Data.registerMessage(body)
        except Exception as exp:
            raise exp

    async def excluirMessage(id):
        try:
            return Data.excluirMessage(id)
        except Exception as exp:
            raise exp

    async def rescueUsers():
        try:
            return Data.rescueUsers()
        except Exception as exp:
            raise exp

    async def registerUser(request):
        try:
            body = await request.json()
            return Data.registerUser(body)
        except Exception as exp:
            raise exp

    async def excluirUser(id):
        try:
            return Data.excluirUser(id)
        except Exception as exp:
            raise exp

    async def rescueContatos():
        try:
            return Data.rescueContatos()
        except Exception as exp:
            raise exp

    async def registerContato(request):
        try:
            body = await request.json()
            return Data.registerContato(body)
        except Exception as exp:
            raise exp

    async def excluirContato(id):
        try:
            return Data.excluirContato(id)
        except Exception as exp:
            raise exp

    async def sendBot(request):
        try:
            body = await request.json()
            ret = await Engine.rescueMessage(body["msg"])
            Bot.__init__(body["contatos"], ret["mensagem"])
            Bot.send()
        except Exception as exp:
            raise exp