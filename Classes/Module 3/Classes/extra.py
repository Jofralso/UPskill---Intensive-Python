'''class Mouse:
    def __init__(self, name):
        self.my_name = name


    def __str__(self):
        return self.my_name


the_mouse = Mouse('mickey')
print(the_mouse)  # Prints "mickey". 

'''

'''
class Mouse:
    pass


class LabMouse(Mouse):
    pass


print(issubclass(Mouse, LabMouse), issubclass(LabMouse, Mouse))  # Prints "False True"


'''
'''
class Mouse:
    pass


class LabMouse(Mouse):
    pass


mickey = Mouse()

print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse))  # Prints "True False".


class Mouse:
    pass


mickey = Mouse()
minnie = Mouse()
cloned_mickey = mickey
print(mickey is minnie, mickey is cloned_mickey)  # Prints "False True".


class Mouse:
    def __str__(self):
        return "Mouse"


class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()


doctor_mouse = LabMouse()
print(doctor_mouse)  # Prints "Laboratory Mouse".



class Mouse:
    Population = 0
    def __init__(self, name):
        Mouse.Population += 1
        self.name = name

    def __str__(self):
        return "Hi, my name is " + self.name

class LabMouse(Mouse):
    pass

professor_mouse = LabMouse("Professor Mouser")
print(professor_mouse, Mouse.Population)  # Prints "Hi, my name is Professor Mouser 1"

student_mouse = LabMouse("Student Rodent")
print(student_mouse, Mouse.Population)  

'''
class Mouse:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name

class AncientMouse(Mouse):
    def __str__(self):
        return "Meum nomen est " + self.name

mus = AncientMouse("Caesar")  # Prints "Meum nomen est Caesar"
print(mus)

'''
In order to find any object/class property, Python looks for it inside:

-the object itself;
-all classes involved in the object's inheritance line from bottom to top;
-if there is more than one class on a particular inheritance path, Python scans them from left to right;
-if both of the above fail, the AttributeError exception is raised.

'''