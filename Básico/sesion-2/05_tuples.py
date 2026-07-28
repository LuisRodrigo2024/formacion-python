### Tuples ###

my_tuple =  tuple()
my_other_tuple = ()

my_tuple = (20, 1.66, "Luis", "Nuñez")
my_other_tuple = (35,60 ,70)
print(my_tuple)

print(type(my_tuple))

print(my_tuple[-1])
print(my_tuple[-2])
#print(my_tuple[4])
#print(my_tuple[-6])

print(my_tuple.count("Luis"))
print(my_tuple.index("Nuñez"))
print(my_tuple.index(20))

# my_tuple[1] = 1.7 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Principe"
my_tuple.insert(0, "Rojo")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# el my_tuple[0] 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple)