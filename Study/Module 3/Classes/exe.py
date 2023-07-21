class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

def check_animal_type(obj):
    if isinstance(obj, Dog):
        print("Object belongs to Dog class")
    elif isinstance(obj, Cat):
        print("Object belongs to Cat class")
    elif isinstance(obj, Animal):
        print("Object belongs to Animal class")

dog = Dog()
cat = Cat()

check_animal_type(dog)  # Output: Object belongs to Dog class
check_animal_type(cat)  # Output: Object belongs to Cat class
