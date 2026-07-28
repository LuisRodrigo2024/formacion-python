### Exception Hadling ###

try:
    print(5 + 5)
except:
    print("Ha ocurrido un error")
else: # Opcional
    # Se ejecuta si no se produce ningún error
    print("No ha ocurrido ningún error")
finally: # Opcional
    # Se ejecuta siempre, haya o no error
    print("Se ejecuta siempre")

# Exceptiones por tipo

try:
    print(5 + "5")
except ValueError:
    # Se ejecuta si se produce un error de tipo ValueError
    print("Se ha producido un error de tipo ValueError")
except TypeError:
    # S e ejecuta si se produce un error de tipo TypeError
    print("Se ha producido un error de tipo TypeError")

# Captura de la información del error
try:
    print(5 + "5")
except ValueError as e:
    # Se ejecuta si se produce un error de tipo ValueError
    print(f"Error: {e}")
except TypeError as e:
    # S e ejecuta si se produce un error de tipo TypeError
    print(f"Error: {e}")