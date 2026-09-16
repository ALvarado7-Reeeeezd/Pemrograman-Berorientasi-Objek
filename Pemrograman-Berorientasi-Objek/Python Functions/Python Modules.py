# Python Modul addition
def add(a, b):

   result = a + b
   return result

# import example  # Di-comment agar tidak menyebabkan ModuleNotFoundError
# example.add(4,5) # mengembalikan nilai 9

# impor modul standar math
import math
# menggunakan math.pi untuk mendapatkan nilai pi
print("Nilai dari pi adalah", math.pi)

# impor modul dengan mengubah namanya (alias)
import math as m
print(m.pi)# Output: 3.141592653589793

# hanya mengimpor pi dari modul math
from math import pi
print(pi)# Output: 3.141592653589793

# mengimpor semua nama dari modul standar math
from math import *
print("Nilai dari pi adalah", pi)

# print(dir(example))  # Di-comment karena modul 'example' tidak di-import

# import example
# example.__name__# Output: 'example'

a = 1
b = "hello"
import math
print(dir())
['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter']