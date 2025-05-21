from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]  # Libera acesso de qualquer origem (para frontend React)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exemplo de rota
@app.get("/")
def root():
    return {"message": "ERP Backend FastAPI online"}

@app.get("/clientes")
def listar_clientes():
    return [{"id": 1, "nome": "Cliente Exemplo"}]
