#Tipos de datos en python
#Cadenas o Strings (cadenas de texto) 
#''string'' 
#'string'
#'''string'''  
#''''''strin'''''' 

string = "Hello I'm Freddy Ramirez"
print(type(string))

#Numeros (numeros enteros numeros con  .)
#Int numeros enteros sin  . 
#Float numeros flotantes con una  un .#

int = 12
print (type(int))

float = 4.2
print(type(float))

#Bool/Boolean  (valores booleanos verdaderos o falsos) 
#True or False se escribe la primera letra en mayúscula 

boolean = True
print (type(boolean))

#Datos compuestos
#List son modificables
#List = [] el número que está dentro de los [] es el elemento que se va a mostrar
#En Programación se cuenta desde el 0, aunque se empiece por el primer el elemento, sería el índice 0#

list = [ 10, 20, 30, 100, 200]
print (list)
print (type (list))

liststring = [ 30, "treinta", 40, "cuarenta"]
print (liststring)
print (type (liststring))

#Tupla es similar a list con la diferencia de que se usan () y no se pueden cambiar 
#Tupla () 

tupla = ("Python")
print(tupla)
print(type(tupla))

#Conjuntos (set) no accede a datos por índice y no almacena datos duplicados
#Conjunto = {} son similares a las listas a excepción de que estos no tienen un orden en especifico, sus datos pueden ser desordenados. Pero elimina datos duplicados 

text = "Hello this is a text"
int = str(428)
print (text + " and this is a number " + int )