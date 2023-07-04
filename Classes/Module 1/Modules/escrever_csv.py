import csv

data = [
    ["Nome", "Idade", "Salário"],
    ["José", 32, 4000],
    ["John", 25, 2000],
    ["Roberto", 44, 3000],
    ["Mark", 19,23000]
]


with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)