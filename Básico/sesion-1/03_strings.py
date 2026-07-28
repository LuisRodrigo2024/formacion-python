### Strings ###
my_string = "Mi string"

my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "Este es un string con comillas \"dobles\" y comillas \'simples\'"
print(my_scape_string)


# Formateo

name, surname, age = "Luis", "Nuñez", 20

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
"""
print(a)
print(b)
""" 

# Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse
language_slice = language[:: -1]
print(language_slice)

# Funciones
print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count("o"))
print(language.isnumeric())
print(language.isalpha())
print(language.lower().isupper())
print(language.startswith("Py"))
print(language.endswith("on"))
print(language.replace("thon", "py"))