#shopping List
shopping_list = {}

def add_item(item, quantity, price):
    shopping_list[item]= (quantity, price)
'''
def calculate_total_cost():
    total_cost = 0
    for item, (quantity, price) in shopping_list.items():
        total_cost += quantity * price
        print(total_cost)
        print()
    return total_cost'''

def calculate_total_cost():  

    total = 0  
    for i in shopping_list.values():  
        total += i[0]*i[1]  

        print(i)
        print(total)
    return total  
 

add_item("Apples", 5, 1.5)  
add_item("Bananas", 3, 0.5) 
add_item("Cereal", 2, 3.75) 
  
total_cost = calculate_total_cost()  
print(shopping_list)
print("Total cost:", total_cost) 

'''


# Dice rolls
import random

def roll_dice(num_dice): 
    dice = (1,2,3,4,5,6)
    rolls = []

    for _ in range(num_dice):
        rolls.append(random.choice(dice))
       # print(rolls)
        #print()
    return rolls

num_dice = int(input("Enter the number of dice to roll: ")) 

dice_rolls = roll_dice(num_dice)
total_sum =sum(dice_rolls)

print("Dice rolls:", dice_rolls)
print("Total sum:",  total_sum)
'''

def check_password_strength(password):
    strength = 0
    if len(password) >=8 :
        strength +=1
    if any(char.isupper() for char in password):
            strength +=1
    if any(char.islower() for char in password):
            strength +=1
    if any(char.isdigit() for char in password):
            strength +=1
    if any(not char.isalnum() for char in password):
            strength +=1
    return strength

password = input("Enter a password: ")
password_strength = check_password_strength(password)
print("Password strength:", password_strength)


""""""""""""""""""
passwords = {}

def add_password(website, username, password):
    if website not in passwords:
        passwords[website] = {}
    passwords[website][username] = password

    print(passwords[website])
    print()

def get_password(website, username):
     if website in passwords and username in passwords[website]:
          return passwords[website][username]
     else:
          return "Password not found."
      
add_password("example.com", "user1", "password123")
add_password("example.com", "user2", "abc123")
add_password("test.com", "testuser", "testpassword")

print("Password for user1 on example.com:", get_password("example.com", "user1"))
print("Password for user2 on example.com:", get_password("example.com", "user2"))
print("Password for testuser on test.com:", get_password("test.com", "testuser"))
print("Password for user3 on example.com:", get_password("example.com", "user3"))