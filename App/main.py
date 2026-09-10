# import json
#
# with data_file.open('r') as file:
#     clientes = json.load(file)
#
# for cliente in clientes:
#     print(cliente["nombre"])
import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"message": "API"}

@app.get("/clientes")
def obtener_clientes():

   with     open("data/clientes.json", "r") as file:
        clientes = json.load(file)

    return clientes

    
@app.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id: int):
    with open("data/clientes.json", "r") as file:
        clientes = json.load(file)

    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return cliente

    return {"message": "Cliente no encontrado"}
