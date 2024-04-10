#Creando un conjunto con set ()
conjunto = set ("Dato 01")

# #Metiendo un conjunto dentro de otro conjunto
# conjunto1 = frozenset(["Dato 1", "Dato 2"])
# conjunto2 = {conjunto1, "Dato 3"}
# print(conjunto2)

#Verificando si es un subconjunto
conjunto1 = {1,3,5,7,9}
conjunto2 = {1,3,5}
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1
print(resultado)

#Verificando si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)
#resultado = conjunto2 > conjunto1
print(resultado)

#Verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)