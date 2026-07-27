# Variables

#Definiendo variables
#String
my_string_variable = "My String variable"
print(my_string_variable)
#Integer
my_int_variable = 5
print(my_int_variable)
#Boolean
my_bool_variable = True
print(my_bool_variable)

#Transformando un tipo de dato a otro
my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Sin tipo de dato, el print devuelve un tipo 'NoneType'
print(type(print(my_string_variable, my_int_variable, my_bool_variable))) # Tipo 'NoneType'

# Algunas funciones del sistema
print(len(my_string_variable)) # 18
print(len(my_int_to_string_variable)) # 1

# Variables en una sola línea
name, surname, alias, age = "Luis", "Nuñez", "Promast", 20
print("Me llamo:", name, surname, "y mi alias es:", alias, "y tengo", age, "años")


# Inputs
"""
name = input("Ingresa tu nombre: ")
age = input("Ingresa tu edad: ")

print("Hola", name, "tienes", age, "años")
"""


# Cambiamos su valor
name = 35
age = "Luis"
print(name, age)

# Forzamos el tipo
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))

# Variables interesantes

# List
my_list = [1, 2, 3, 4, 5]
print(my_list) # Ordered collection, mutable

# Reemplazando un elemento de una lista
my_list[0] = 0
print(my_list)
my_list[0] = 1

# Reemplazando todos los elementos de una lista con fórmula
my_list = [x-1 for x in my_list]
print(my_list)

# Dictionary
my_dict = {
    "name": "Luis",
    "surname": "Nuñez",
    "age": 20,
    "alias": "Promast"
}
print(my_dict) # Unordered collection, mutable

# Reemplazando un elemento de un diccionario
my_dict["name"] = "Juan"
print(my_dict)

# Tuple
my_tuple = (0, 1, 2, 3, 4, 5)
print(my_tuple) # Ordered collection, immutable

# Set
my_set = {1, 2, 3, 4, 5}
print(my_set) # Unordered collection, mutable #Elementos únicos
