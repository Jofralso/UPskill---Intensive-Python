import json
#escrever

data = {
    "nome": "Joao",
    "idade": 34,
    "país": "Espanha"
}

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)