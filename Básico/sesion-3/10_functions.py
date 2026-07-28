### Functions ###

def my_function():
    print("Esto es una función")

my_function() # Llamada a la función

def potencia(base, exponente):
    """
    Calcula la potencia de un número dado una base y un exponente.
    
    Args:
        base (float): La base de la potencia.
        exponente (float): El exponente al que se eleva la base.
        
    Returns:
        float: El resultado de la potencia.
    """
    return base ** exponente

print(potencia(2, 3)) # Imprime 8

def suma(a, b):
    """
    Calcula la suma de dos números.
    
    Args:
        a (float): El primer número.
        b (float): El segundo número.
        
    Returns:
        float: La suma de los dos números.
    """
    return a + b

print(suma(2, 3)) # Imprime 5
print(suma("6","7")) # Imprime 67 (concatenación de cadenas)

def print_name(name, surname):
    """
    Imprime un saludo con el nombre proporcionado.
    
    Args:
        name (str): El nombre a saludar.
        surname (str): El apellido a saludar.
    """
    print(f"Hola, {name} {surname}!")

print_name(surname="Nuñez", name="Luis") # Llamada a la función con argumentos nombrados

def print_name_with_default(name, surname, alias="Sin alias"):
    """
    Imprime un saludo con el nombre proporcionado y un apellido opcional.
    
    Args:
        name (str): El nombre a saludar.
        surname (str, optional): El apellido a saludar. Por defecto es una cadena vacía.
        alias (str, optional): El alias a saludar. Por defecto es una cadena vacía.
    """
    print(f"Hola, {name} {surname} - {alias}!")

print_name_with_default("Luis", "Nuñez") # Llamada a la función con el valor por defecto del alias
print_name_with_default("Luis", "Nuñez", "Promaster") # Llamada a la función con un alias proporcionado

def print_texts(*texts):
    """
    Imprime una lista de textos proporcionados como argumentos.
    
    Args:
        *texts (str): Una lista de textos a imprimir.
    """
    for text in texts:
        print(text)

print_texts("Hola", "Mundo", "Desde", "Python") # Llamada a la función con múltiples argumentos