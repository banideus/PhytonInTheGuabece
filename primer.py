#tipadoDinamico.py
#integers
a=34
b=23
c=31

# #Integers
print(a+b+c)
print ("Output Vars a,b,c",a,b,c)
print ("Output Vars a:{0},b:{1},c{2}".format(a,b,c))
print ("La suma de las variables es: ",a+b+c)
print ("La suma de las variables es:  ".format(a+b+c))

 #Float
a=20.90
b=23.12
c=22.43
#
print(a+b+c)
print(type(a))
#
#boolean
d=True
e=False
#String
s="Este es un String de comillas dobles"
ss='Este es un String de comillas dobles'
sss='Este es un String que tiene "comillas dobles" dentro'
print(s+ss)
print (sss)
print(s*3)
print(s[1:3])
print(s[11:])
print(s[-11:])
print (s.index("s"))
print(s.split())
ssss=s.split()
print(len(ssss))

#List
lista =[1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista)
print(sum(lista))

# lista.append(0)
print (lista)
lista.insert(0,0)
print(lista)

# lista.pop(0) #eliminar
# lista.pop(len(lista)-1)

lista[10]=10

lista.pop(lista.index(8))
l=len(lista)
i=0
for i in range(l):
    print (lista[i])

for i in lista:
   print(i)


#Tuplas
t=(1-2, "abc",True, [4,5] )
print(t)
print(t[2])
#
for item in t:
    print(item)

#Dict
d={1:2,"abc":34,2:"item","d":"ch", "li":[1,2,3],"dic":{11:23}}
print (d)
print (d["abc"])
print (d["dic"][11])

print (d.keys())#pura claves
print (d.values())#puro valor
print (d.items()) #cada clave y valor

#sets
s={1, 2, 3, 4}
print(s)
print(type(s))

for item in s:
    print(item)
