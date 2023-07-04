class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")

    def stop(self):
        print(f"The {self.brand} {self.model} has stopped.")




class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying.")

    def take_exam(self):
        print(f"{self.name} is taking an exam.")

''' 
+------------------------+
|    Online Shopping     |
+------------------------+
| - customer: Customer   |
| - cart: ShoppingCart  |
+------------------------+
| + browseProducts()     |
| + addToCart(product)   |
| + checkout()           |
+------------------------+
'''

'''
+------------------------+
|   Library Management   |
+------------------------+
| - librarian: Librarian |
| - member: Member       |
+------------------------+
| + addBook(book)        |
| + lendBook(book)       |
| + returnBook(book)     |
+------------------------+
'''

'''
+------------------------+
|  Ticket Booking System |
+------------------------+
| - user: User           |
| - event: Event         |
+------------------------+
| + searchEvents()       |
| + selectEvent(event)   |
| + bookTicket()         |
+------------------------+

'''