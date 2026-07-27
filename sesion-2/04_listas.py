### Listas ###}

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [1, 2, 3, 3, 4, 5, 5]

print(my_list)
print(len(my_list))

my_other_list = [20, 1.66, "Luis", "Nuñez"]

print(type(my_list))
print(type(my_other_list))

# Las listas no son arrays, son colecciones de datos que pueden contener diferentes tipos de datos.
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[len(my_other_list) - 1])
print(my_other_list[-2])

# Contar cuantas veces aparece un elemento en una lista
print(my_list.count(3))

# print(my_other_list.index("Luis"))

age, height, name, surname = my_other_list
print(name)
surname, height, age, name = my_other_list[-1], my_other_list[1], my_other_list[0], my_other_list[2]
print(surname)

print(my_list + my_other_list)

my_other_list.append("Promast")
print(my_other_list)

my_other_list.insert(1,"1.74")
print(my_other_list)

my_list.remove(3)
print(my_list)

my_pop_element = my_list.pop(2)
print(my_list)
print(my_pop_element)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()
my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_list = "Hola Python"
print(my_list)
print(type(my_list))

## Convención para constantes ##
CONSTANTE_PI = 3.14