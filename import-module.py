import module
import module as mx

module.greeting("Jhonatan")

a = module.person1["age"]
print(a)

b = mx.person1["age"]
print(b)

import platform

x = platform.system()
print(x)

x = dir(platform)
print(x)

