"""i = 1
while i <=10:
    print(i)
    i+=1
    
#

while True:
    print("isto é um loop infinito")
    #break
    """

####
#Loop Controlo de sentinela
"""sum = 0
while True:
    num = int(input("Introduza um numero (-1 até ao fim): "))
    if num == -1:
        break
    sum += num
print("Esta soma é", sum)"""

"""# Loop controlado por condições
num = int(input("Introduza um numero: "))
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print("O factorial é", factorial)

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print( i*j , end='\t') 
        j += 1
    print()
    i += 1
"""
###########Pre test Loop
"""while True:
    num = int(input("Introduza um numero de 1 a 10: "))
    if num >= 1 and num <= 10:
        break


print("O numero é ", num)"""

rang = range(0,11)
num = 1
while True:
    num = int(input())
    if num in rang:
        print("numero pertence ao grupo")
        break
####
password = "python"

while True:
    input_pass = input("Introduza uma pass: ")
    if input_pass == password:
        break
    else:
        print( "A password está errada")

print("entrou no sistema")        