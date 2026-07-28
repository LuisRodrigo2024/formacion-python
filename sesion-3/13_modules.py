### Modules ###

# import my_module
import my_module

print(my_module.sumValue(2, 3, 4))
my_module.printValue("Hello, World!")

from my_module import sumValue, printValue

sumValue(2, 3, 4)
printValue("Hola python")

import math

print(math.pi)
print(math.sqrt(16))
print(math.pow(2,8))

from math import pi as PI_VALUE

print(PI_VALUE)