"""Problem: 
Create a dictionary to store information about different cats, 
such as their names, ages, and favorite toys. """

cats = {
    "Fluffy": {"age": 3,"favorite_toy": "feather wand"},
    "Whiskers": {
        "age": 5,
        "favorite_toy": "catnip mouse"
    },
    "Mittens": {
        "age": 2,
        "favorite_toy": "yarn ball"
    }
}

def get_cat_info(name):
    if name in cats: 
        return cats[name]
    else:
        return "O gato fugiu de casa!!"


cat_name = input("Enter a cat's name: ")
cat_info = get_cat_info(cat_name)
print("Cat information:", cat_info)

#######################################################
"""Merge Dictionaries 

Write a function merge_dicts(dict1, dict2) 
that takes two dictionaries as input and 
returns a new dictionary that combines the 
key-value pairs from both dictionaries. """

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
result = merge_dicts(dict1, dict2)
print(result)




##################################################
"""Word Anagram Groups 

Write a function anagram_groups(words) that takes a 
list of words as input and returns a dictionary where 
the keys are sorted strings of letters representing 
anagrams, and the values are lists of words that are 
anagrams of each other. """

def anagram_groups(words):
    anagram_dict = {}
    for word in words:

        sorted_word = ''.join(sorted(word))
        
        print(word)
        print()
        print(sorted_word)

        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word]=[word]
    return anagram_dict


words = ['cat', 'dog', 'tac', 'god', 'act']
result = anagram_groups(words)
print(result)


##################################################
"""Nested Dictionary Manipulation 

Consider a dictionary representing a company's 
employee structure. Each employee has a name and a 
department. Write a function 
get_department_size(company, department) that takes 
the company dictionary and a department name as input. 
 The function should return the number of employees in 
 the specified department.  """

def get_department_size(company, department):
    if department in company:
        return len(company[department])
    else:
        return 0

company = {
    'IT': {
        'John': 'Developer',
        'Jane': 'Designer',
        'Mike': 'Manager'
    },
    'HR': {
        'Alice': 'Recruiter',
        'Bob': 'HR Assistant'
    },
    'Sales': {
        'Tom': 'Sales Manager',
        'Emily': 'Sales Representative'
    }
}


department_size = get_department_size(company, 'IT')
print(f"Number of employees in IT department: {department_size}")

department_size = get_department_size(company, 'HR')
print(f"Number of employees in HR department: {department_size}")

department_size = get_department_size(company, 'Marketing')
print(f"Number of employees in Marketing department: {department_size}")
 
 ##################################################
"""Dictionary Inversion 

Write a function invert_dictionary(dictionary) 
that takes a dictionary as input and returns 
a new dictionary where the keys and values are swapped. """

def invert_dictionary(dictionary):
    inverted_dictionary = {}
    for key, value in dictionary.items():
        inverted_dictionary[value]  = key
    return inverted_dictionary


dictionary = {'apple': 'fruit', 'carrot': 'vegetable', 'banana': 'fruit', 'broccoli': 'vegetable'}

inverted_dictionary = invert_dictionary(dictionary)
print(inverted_dictionary)
