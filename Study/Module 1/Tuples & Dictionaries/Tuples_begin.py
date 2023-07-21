tuple_1 = (1,2,3,4)
tuple_2 = 1., 5., .25, .125

print(tuple_1)
print(tuple_2)

tuple_3 = (1, 10, 100, 1000)
print(tuple_3[0])
print(tuple_3[-1])
print(tuple_3[1: ])
print(tuple_3[0 :-2])

for elem in tuple_3:
    print(elem)

##########
my_tuple = (1, 10, 100)
t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)
my_tuple = my_tuple + my_tuple
print(my_tuple)
my_tuple = my_tuple - (1, 10 ,100)
print(my_tuple)