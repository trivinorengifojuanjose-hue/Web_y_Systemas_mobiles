import json

with data_file.open('r') as file:
    clientes = json.load(file)

    print(clientes)
