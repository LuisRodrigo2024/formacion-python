### Conditionals ###

my_condition = False

if my_condition:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5

# Primera condición
if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

# Segunda condición
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecución continúa")


# Tercera condición - Anidado
my_condition = 5 * 2

if my_condition > 10:
    print("Es mayor que 10")
elif my_condition > 0:
    print("Es mayor que 0 y menor o igual que 10")
else:
    print("Es menor o igual que 0")

# Cuarta condición - Con strings
my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")