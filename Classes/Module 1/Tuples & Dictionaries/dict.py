# Creating a dictionary
person = {"name": "John", "age": 30, "city": "New York"}

# Accessing dictionary elements
print(person["name"])  # Output: John
print(person["age"])   # Output: 30
print(person["city"])  # Output: New York

print()
#-------------------------------------------------------------#
# Modifying a dictionary element
person["age"] = 35

# Accessing the modified element
print(person["age"])  # Output: 35
print()
#-------------------------------------------------------------#
# Adding a new element to the dictionary
person = {"name": "John", "age": 30}
person["city"] = "New York"
print()
# Accessing the new element
print(person["city"])  # Output: New York
print()
# Removing an element from the dictionary
del person["age"]

# Trying to access the removed element
# print(person["age"])  # Raises KeyError: 'age'
print()
#-------------------------------------------------------------#

# Iterating over dictionary keys
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key)  # Output: name, age, city

# Iterating over dictionary values
for value in person.values():
    print(value)  # Output: John, 30, New York

# Iterating over dictionary key-value pairs
for key, value in person.items():
    print(key, value)  # Output: name John, age 30, city New York


"""

Exercise 1: Student Grades
Implement a function called calculate_average_grade that takes a 
dictionary student_grades as input. The student_grades dictionary 
contains student names as keys and their corresponding grades as 
values (a list of numbers). The function should calculate and return 
the average grade for each student.
"""
def calculate_average_grade(student_grades):
    average_grades = {}
    for student, grades in student_grades.items():
        total_grades = sum(grades)
        average = total_grades / len(grades)
        average_grades[student] = average
    return average_grades



"""
Implement a function called count_word_frequency that takes a string 
text as input and returns a dictionary where the keys are unique words 
in the text, and the values are the frequencies of those words (how many 
times they appear in the text).
Explanation:

The function calculate_average_grade takes a dictionary student_grades as input, where the keys 
are student names and the values are lists of grades.

We create an empty dictionary average_grades to store the average grades 
for each student.
We iterate over each key-value pair in the student_grades dictionary using 
the items() method.
Inside the loop, we calculate the total of grades for the current student 
using the sum() function.
We calculate the average grade by dividing the total by the number of grades 
using the len() function.
Finally, we add the student name as the key and the average grade as the 
value to the average_grades dictionary.
After iterating over all students, we return the average_grades dictionary
containing the average grades for each student.

"""


student_grades = {
    "Alice": [80, 90, 75],
    "Bob": [85, 95, 70],
    "Charlie": [90, 80, 85]
}

"""
We start with an empty average_grades dictionary. The function iterates 
over each student in the student_grades dictionary 
and calculates the average grade.

For student "Alice", the grades are [80, 90, 75]. The function calculates 
the average by summing the grades (80 + 90 + 75 = 245) and dividing by the 
number of grades (3). The average grade is 245 / 3 = 81.67. 
The result is added to the average_grades dictionary with the key "Alice" and value 81.67.
The process is repeated for "Bob" and "Charlie" with their respective grades. 
The calculated average grades are added to the average_grades dictionary.
The resulting average_grades dictionary will be:

"""
{
    "Alice": 81.67,
    "Bob": 83.33,
    "Charlie": 85.0
}



#Exercise 2: Word Frequency Counter
"""Problem: Implement a function called count_word_frequency that takes a string text as input and returns a dictionary where the 
keys are unique words in the text, and the values are the frequencies of those words (how many times they appear in the text)."""

def count_word_frequency(text):
    words = text.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

"""
Explanation:

The function count_word_frequency takes a string text as input.
We split the text into a list of words using the split() method, which splits the text on whitespace by default.
We create an empty dictionary word_frequency to store the frequency of each word.
We iterate over each word in the words list.
Inside the loop, we check if the word is already a key in the word_frequency dictionary using the in operator.
If the word is present, we increment its frequency by 1.
If the word is not present, we add it to the word_frequency dictionary with an initial frequency of 1.
After processing all the words, we return the word_frequency dictionary.
"""

text = "the quick brown fox jumps over the lazy dog"

"""
The function splits the text into individual words and counts their frequencies.

We start with an empty word_frequency dictionary. The first word is "the".
Since "the" is not present in the dictionary, we add it with a frequency of 1.
The next word is "quick".
We add "quick" to the dictionary with a frequency of 1.
The word "brown" is also not present, so we add it with a frequency of 1.
The word "fox" is added to the dictionary with a frequency of 1.
The word "jumps" is added with a frequency of 1.
The word "over" is added with a frequency of 1.
The word "the" is already present in the dictionary, so we increment its frequency by 1, resulting in a frequency of 2.
We continue this process for the remaining words.
The resulting word_frequency dictionary will be:
"""
{
    "the": 2,
    "quick": 1,
    "brown": 1,
    "fox": 1,
    "jumps": 1,
    "over": 1,
    "lazy": 1,
    "dog": 1
}

#Exercise 3: Phonebook
"""
Implement a simple phonebook using a dictionary. The phonebook should 
allow users to add contacts, retrieve contact details by name, and list all contacts.
"""

def add_contact(phonebook, name, number):
    phonebook[name] = number

def get_contact(phonebook, name):
    if name in phonebook:
        return phonebook[name]
    else:
        return None

def list_contacts(phonebook):
    for name, number in phonebook.items():
        print(f"{name}: {number}")


"""
Explanation:

Instead of using a class, we define three separate functions to handle the phonebook operations.
The add_contact function takes a phonebook dictionary, name, and number as input, and adds 
the contact to the phonebook dictionary.
The get_contact function takes a phonebook dictionary and a name as input, and returns the 
corresponding contact number if it exists in the phonebook dictionary. If the contact is not 
found, it returns None.
The list_contacts function takes a phonebook dictionary as input and iterates over 
the dictionary, printing the name and number of each contact.
"""
phonebook = {}

add_contact(phonebook, "Alice", "123456789")
add_contact(phonebook, "Bob", "987654321")
add_contact(phonebook, "Charlie", "555555555")

list_contacts(phonebook)

