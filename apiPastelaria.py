from fastapi import FastAPI

import db
# import das classes de modelo de persistência
from mod_funcionario.FuncionarioModel import FuncionarioDB

# import das classes com as rotas/endpoints
from mod_funcionario import FuncionarioDAO

app = FastAPI()

# mapeamento das rotas/endpoints
app.include_router(FuncionarioDAO.router)

# cria, caso não existam, as tabelas de todos os modelos importados

app.include_router(FuncionarioDAO.router)

db.criaTabelas()