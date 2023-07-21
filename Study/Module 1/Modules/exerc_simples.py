"""Exercise 1: Math Module 
Write a program that asks the user to enter 
two numbers and calculates their sum using 
the math module's sum() function. Print the 
result. """
import math

result = math.fsum([1, 2, 3, 4, 5])
print("A soma é:", result)

# Use a list
sum([1, 2, 3, 4, 5])


# Use a tuple
sum((1, 2, 3, 4, 5))


# Use a set
sum({1, 2, 3, 4, 5})


# Use a range
sum(range(1, 6))


# Use a dictionary
sum({1: "one", 2: "two", 3: "three"})
sum({1: "one", 2: "two", 3: "three"}.keys())

 
"""
Exercise 2: Random Module 

Write a program that generates a random number 
between 1 and 10 using the random module's randint() 
function. Print the generated number. 
"""
import random
random_num = random.randint(1,10)
print("Numero aleatório:", random_num)
"""
Exercise 3: Datetime Module 

Write a program that prints the current date 
and time using the datetime module. 
"""
import datetime

data = datetime.datetime.now()
print("Data e Horas:", data)

"""
Exercise 4: OS Module 

Write a program that lists all the files and folders 
in the current directory using the os module's 
listdir() function. Print each item on a new line. 
"""
import os

pastas_ficheiros= os.listdir()
for item in pastas_ficheiros:
    print(item)

"""Exercise 5: Calendar Module 

Write a program that asks the user to enter a year 
and month, and prints the calendar for that month 
using the calendar module's month() function. 
"""
import calendar

ano = int(input("Coloque o Ano:"))
mes = int(input("Coloque o mês: "))

print(calendar.month(ano, mes))

"""Exercise 6: CSV Module 

Write a program that reads data from a CSV file 
using the csv module and performs some operations
on the data, such as calculating the average, 
finding the maximum value, or filtering the data 
based on certain conditions. """

import csv

def read_csv_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            data.append(row)
        return data
    
def calc_average(data):
    values = [float(row[1]) for row in data]
    average = sum(values) / len(values)
    return average

def find_max_value(data):
    values = [float(row[1]) for row in data]
    maximum = max(values)
    return maximum

def filter_data(data, condition):
    filtered_data = [row for row in data if condition(row)]
    return filtered_data


file_path = 'data.csv'
data = read_csv_data(file_path)

average = calc_average(data)
print("Média:", average)

max_value = find_max_value(data)
print("Valor máximo",max_value )

filtered_data = filter_data(data, lambda row: float(row[2]) > 3000)
print("Dados filtrados:", filtered_data)
"""


data = [
    ["Nome", "Idade", "País"],
    ["José", "32", "Portugal"],
    ["John", "25", "USA"],
    ["Roberto", "44", "México"],
    ["Mark", "19", "UK"]
]
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

#Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

"""



 
"""
Exercise 7: JSON Module 

Write a program that reads data from a JSON file using
the json module and performs some operations on the data, 
such as extracting specific values, modifying the data, 
or generating reports based on the data. 
"""
 