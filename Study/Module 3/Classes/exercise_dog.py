class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: Woof!"


class SheepDog(Dog):
    def __init__(self, breed):
        SheepDog.kennel = 200
        
    def __str__(self):
        return super().__str__() + " Don't run away, Little Lamb!"


class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " Stay where you are, Mister Intruder!"


rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")




'''
1- What is the expected output of the following piece of code?

print(rocky)
print(luna)

2- What is the expected output of the following piece of code?

print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))

3- What is the expected output of the following piece of code?
'''
print(luna is luna, rocky is luna)
print(luna.kennel)
print(rocky.kennel)
'''
4 - Define a SheepDog's subclass named LowlandDog, and equip it with 
an __str__() method overriding an inherited method of the same name. 
The new dog's __str__() method should return the 
string "Woof! I don't like mountains!" .


'''

