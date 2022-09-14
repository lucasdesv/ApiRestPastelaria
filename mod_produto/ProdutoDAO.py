from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()
class Produto(BaseModel):
    codigo: int = None
    nome: str
    descricao: str
    foto: bytes
    valor_unitario: str = None

# Criar os endpoints de Produto: GET, POST, PUT, DELETE
@router.get("/produto/{id}", tags=["produto"])
def get_funcionario(id: int):
    return {"msg": "get executado", "id": id}, 200

@router.post("/produto/{id}", tags=["produto"])
def post_produto(id: int, f: Produto):
    return {"msg": "post executado", "id": id, "nome": f.nome, "descricao": f.descricao, "valor_unitario": f.valor_unitario}, 200

@router.put("/produto/{id}", tags=["produto"])
def put_produto(id: int, f: Produto):
    return {"msg": "post executado", "id": id, "nome": f.nome, "descricao": f.descricao, "valor_unitario": f.valor_unitario}, 201

@router.delete("/produto/{id}", tags=["produto"])
def delete_produto(id: int):
    return {"msg": "delete executado", "id": id}, 201