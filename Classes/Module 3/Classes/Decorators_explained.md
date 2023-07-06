# Decorators in Python

 Decorators are a powerful feature in Python that allow you to modify the behavior of functions or classes by adding additional functionality to them. They provide a clean and concise way to extend or modify the functionality of existing code without explicitly modifying the original code.
In Python, decorators are implemented using the @decorator_name syntax, which is placed above the function or class definition that you want to decorate. The decorator is essentially a callable object that takes a function or class as an argument, and returns a modified version of that function or class.
Decorators can be used for various purposes and offer a wide range of use cases. Let's explore some of the different use cases for decorators:

## Function Decorators:
Function decorators are the most common use case for decorators in Python. They allow you to modify the behavior of a function by wrapping it with additional code. Here's an example:

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        result = func(*args, **kwargs)
        print("Function", func.__name__, "returned:", result)
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

result = add(3, 5)  # Output: Calling function: add
                    #         Function add returned: 8
```

In this example, the logger function is a decorator that wraps the add function. It adds logging statements before and after calling the add function, allowing us to see when the function is called and what it returns.

## Class Decorators:
Decorators can also be applied to classes, allowing you to modify the behavior of a class or its methods. Class decorators receive the class object as an argument and can return a modified version of the class. Here's an example:

```python
def add_method(cls):
    def multiply(self, a, b):
        return a * b
    cls.multiply = multiply
    return cls

@add_method
class Math:
    def add(self, a, b):
        return a + b

math = Math()
result = math.multiply(3, 5)  # Output: 15
```

In this example, the add_method decorator adds a new method multiply to the Math class. The decorator modifies the class object by adding the multiply method to it, allowing instances of the class to call the new method.

## Decorators with Arguments:
Decorators can also accept arguments, allowing you to customize their behavior. This is achieved by defining a decorator factory function that returns the actual decorator. Here's an example:

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print("Hello,", name)

greet("Alice")  # Output: Hello, Alice
                #         Hello, Alice
                #         Hello, Alice
```

In this example, the repeat decorator factory function takes an argument n and returns the actual decorator. The decorator itself wraps the function greet and repeats its execution n times.

### Decorators for Authentication and Authorization:
Decorators can be used to enforce authentication and authorization checks on functions or methods. They can ensure that only authenticated users or users with the appropriate privileges can access certain parts of the code. Here's a simplified example:

```python
 def authenticate(func):
     def wrapper(*args, **kwargs):
         if user_authenticated():
             return func(*args, **kwargs)
         else:
             raise Exception("User not authenticated.")
     return wrapper

 def authorize(roles):
     def decorator(func):
         def wrapper(*args, **kwargs):
             if user_has_roles(roles):
                 return func(*args, **kwargs)
             else:
                 raise Exception("User unauthorized.")
         return wrapper
     return decorator

 @authenticate
 @authorize(roles=["admin", "manager"])
 def delete_user(user_id):
     # Delete user logic here
     pass

 delete_user(123)  # Only authorized users with the roles "admin" or "manager" can delete users.
```

In this example, the authenticate decorator ensures that the user is authenticated before executing the delete_user function. The authorize decorator checks if the authenticated user has the required roles (e.g., "admin" or "manager") before allowing the function to proceed.
