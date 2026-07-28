### Classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname,alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"
        self.__name = name # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Luis", "Nuñez")
print(my_person.full_name)
print(my_person.get_name())  # Esto va a imprimir "Luis"
my_person.walk()

my_other_person = Person("Juan", "Perez", "Juancho")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector Perez (Hectorito)"
print(my_other_person.full_name)