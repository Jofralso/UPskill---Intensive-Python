a = 10
b = 5
# Comparison Operators - (Booleans)

print( a == b )#False - Igual a 
print( a != b )#True - Diferente de
print( a < b )#False - menor que
print(a > b)#True - maior que
print(a <= b)##False - menor ou igual que
print(a >= b )##True - maior ou igual que

c = 3

# Logical Operators
print( a > b and b > c )# TRUE
print( a > b or b < c )# TRUE
print(not( a > b or b > c))#False

#Assignment Operators
a = 10
a +=5 # a = a + 5
print(a)

b = 3
b **= 2 # b = b ** 2// b = b^2
print(b)

#Bitwise Operators

a = 0b1010 # Representação binária de 10
b = 0b1100 # Representação binária de 12

print(bin( a & b ))
print(bin( a | b ))
print(bin( a ^ b ))
print(bin( ~a ))
print(bin( a << 2 ))
print(bin( b >> 1 ))

#Identity operators
a = [1, 2 ,3]
b = a
c = [1, 2 ,3]

print (a is b)
print (a is not c)

#Membership Operators
a = [1,2,3]
b=2

print(b in a)
print(4 not in a)





