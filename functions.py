#functions.py

#by User
def hello():
    return "Hello World! XD"

print(hello())
#
s=hello()
ss= "Bani Garcia"
print(s+" - "+ss)

num=5
def add(num2,num=1):
    num=num+1
    return num

print(add(3,1))

x=int(input("Escribe un numero: "))
y=int(input("Escribe otro numero: "))
def add(num2,num=1):
    num=num+num2
    return num
# #
print(add(x,y))
#
from mylib import suma
from mylib import restar
#
print(suma(x,y))
print(restar(x,y))

#by Python

import random
import math
from math import pi
#
print(random.random())
for i in range(1000):
    print(random.random())
for i in range(10):
    print(random.random()*math.cos(i))
    print(pi)

import os
#
print(os.getcwd())
print(dir(os))

import random
lista=[1, 2, 3, 4, 5, 6, 7, 8, 9]

print(random.choice(lista))
