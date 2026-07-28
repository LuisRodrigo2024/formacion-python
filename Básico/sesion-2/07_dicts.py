### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = { "Nombre":"Luis", "Apellido":"Nuñez", "Edad":20, 1:"Python"}

my_dict = {
    "Nombre":"Luis",
    "Apellido":"Nuñez",
    "Edad":20,
    "Lenguaje":{"Python","JavaScript","Postman"},
    1:1.66
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Rodrigo"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Promast"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Nuñez" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_other_dict.fromkeys(("Nombres",1)))

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

# Cuando insertas un valor, este se asigna a todas las llaves del diccionario
my_new_dict = dict.fromkeys(my_dict, "Luis")
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))