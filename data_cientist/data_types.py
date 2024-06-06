"""
#This is an integer
int = 11
#This is a float
float = 21.213
#This is a string
string = "Hello Python 101"
#This is a boolean
boolean = True
boolean = False
"""

#We can see the actual data type in Python by using the type command
example_1 = type(290) #<class 'int'>
example_2 = type(213.3) #<class 'float'>
example_3 = type("Hello") #<class 'str'>
example_4 = type(True) #<class 'bool'>
example_5 = type(False) #<class 'bool'>
#print(example_5)

#You can convert or cast the integer to a float
#This is a int
int_number = 11
#Convert int to float
float_number = float(int_number)
#print(float_number) #11.0

#You can convert or cast the float to a integer
float_number = 2322.54
#Convert float to integer
int_number = int(float_number)
#print(int_number)

#You can convert or cast the float to string
int_string = str(float_number)
#print(float_number)

string_number = "2"
string_float = "223.4"
#Convert string to integer
int_number = int(string_number)
#Convert string to float
float_number = float(string_float)
#print(int_number)
#print(float_number)

#Convert boolean to int
boolean = int(False) #True = 1 False = 0
#print(boolean)

#Convert int to boolean
boolean = bool(1) # 1 = True, 0 = False 
#print(boolean)
