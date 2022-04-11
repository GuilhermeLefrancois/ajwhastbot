from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.requests import Request
from engine import *

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("views/index.html")

@app.post("/login")
async def login(request: Request):
    try:
        return await Engine.login(request)            
    except Exception as exp:
        raise exp

@app.get("/menssagens")
async def obterMenssagens():
    try:
        return await Engine.rescueMessages()           
    except Exception as exp:
        raise exp

@app.post("/menssagens")
async def salvarMenssagem(request: Request):
    try:
        return await Engine.registerMessage(request)           
    except Exception as exp:
        raise exp

@app.post("/menssagens/excluir/{id}")
async def excluirMenssagem(id):
    try:
        return await Engine.excluirMessage(id)           
    except Exception as exp:
        raise exp

@app.get("/usuarios")
async def obterUsuarios():
    try:
        return await Engine.rescueUsers()           
    except Exception as exp:
        raise exp

@app.post("/usuarios")
async def salvarUsuarios(request: Request):
    try:
        return await Engine.registerUser(request)           
    except Exception as exp:
        raise exp

@app.post("/usuarios/excluir/{id}")
async def excluirUsuarios(id):
    try:
        return await Engine.excluirUser(id)           
    except Exception as exp:
        raise exp

@app.get("/contatos")
async def obterContatos():
    try:
        return await Engine.rescueContatos()           
    except Exception as exp:
        raise exp

@app.post("/contatos")
async def salvarContatos(request: Request):
    try:
        return await Engine.registerContato(request)           
    except Exception as exp:
        raise exp

@app.post("/contatos/excluir/{id}")
async def excluirContatos(id):
    try:
        return await Engine.excluirContato(id)           
    except Exception as exp:
        raise exp


@app.post("/bot")
async def ativarBot(request: Request):
    try:
        return await Engine.sendBot(request)           
    except Exception as exp:
        raise exp