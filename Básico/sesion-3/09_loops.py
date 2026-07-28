### Loops ###

# While
i = 0

while i < 5:
    print(f"Estamos en la iteración {i}")
    i += 1
else: # Es opcional, se ejecuta cuando la condición del while deja de cumplirse
    print("Mi condición es mayor o igual a 5")

while i < 10:
    print(f"Estamos en la iteración {i}")
    i += 1
    if i == 7:
        print("Mi condición es igual a 7, se rompe el ciclo")
        break # Rompe el ciclo y no ejecuta el else
else:
    print("Mi condición es mayor o igual a 10")

# For

my_list = [1, 2, 3, 4, 5]

for j in my_list:
    print(j)

my_tuple = (20, 1.66, "Luis", "Nuñez")

for j in my_tuple:
    print(j)

my_set = {"Luis","Nuñez",20}

for j in my_set:
    print(j)

my_dict = {"Nombre": "Luis", "Apellido": "Nuñez", "Edad": 20}
for j in my_dict:
    print(j) # Imprime las llaves del diccionario

for j in my_dict.values():
    print(j) # Imprime los valores de las llaves del diccionario
    if j == "Nuñez":
        continue
    print("Se ejecuta") # Salta a la siguiente iteración del bucle for
else : 
    print("El bucle for ha finalizado") # Se ejecuta cuando el bucle for termina de iterar