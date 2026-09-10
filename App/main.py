import json

with data_file.open('r') as file:
    clientes = json.load(file)

for cliente in clientes:
    print(cliente["nombre"])
 
