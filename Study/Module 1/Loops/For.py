frutas = ["maças", "banana", "cereja"]
for x in frutas:
    print(x)
###############################

nums=[1,3,5,7,9]

soma = 0    

for num in nums:
    soma += num
    print(soma)

print( "A soma é:", soma)

############################
nums = [2,3,5,7,8,9,11,13,14,15]

for num in nums:
    
    if num % 2 == 0:
        print("O primeiro número par é:", num)
        break
       #############################################

##############################################################
"""nums =[1,2,3,4,5,6,7,8,9,10]
for num in nums:
    print(num)
"""
for i in range(1,11):
    print(i)

 ############################

for i in range(1, 11):
    print(f"5 x {i} = {i * 5}") 
##############################
num = 5
for i in range(1,11):
    print(num, "x", i, "=", i * num)
##########################

string = "Hello World!"
search_term ="l"
cont = 0
for i, character in enumerate(string):
    print(i, character)
    """
    if character == search_term:
        cont += 1
        print(search_term, "foi encontrado no index", i)
        #break
print(cont)"""