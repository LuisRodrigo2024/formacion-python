 ### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Luis","Nuñez",20}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Promast")

print(my_other_set) # Un set no es una estructura ordenada

print("Nuñez" in my_other_set)
print("Principe" in my_other_set)

my_other_set.remove("Nuñez")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Luis","Nuñez",20}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Spring Boot","Java","Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript","C++"}))

print(my_new_set.difference(my_set))