#Tuples are an ordered sequence
#Tuples are written as a comma-separated elements within parentheses
tuple = (1,2,3,4,5,6,7,8,9,0)
#The value are numbers but the called is a tuple
print (type(tuple)) #output <class 'tuple'>
print (tuple) #output (1,2,3,4,5,6,7,8,9,0)

tuple_1 = ("disco", 10, 1.2)
print(tuple_1[0]) #output disco

#We can mix the tuples
tuple_2 = tuple_1 + ("New tuple", 18, 1342.8) #It´s very important concatenaning with the symbol + to add the old value (tuple) with the new
print(tuple_2) #output (1,2,3,4,5,6,7,8,9,0)
print(tuple_2[0:3]) #('disco', 10, 1.2)
print(tuple_2[4:6]) #(18, 1342.8)
#Tuples Slicing
print (len(tuple_2)) # 6

#The tuples are immutable
tuple_3 = ("An immutable tuple", 5, 54)
#tuple_3[1] = 7
#print(tuple_3)  #output ERROR

tuple_3 = (1,5,6,7,7,4,3,5,6,7,89,9,0,56,4,3,566,65)
tuple_sorted = sorted(tuple_3)
print(tuple_sorted) 
