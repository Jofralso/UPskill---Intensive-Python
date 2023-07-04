
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





