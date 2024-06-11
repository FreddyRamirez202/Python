#This is a string
name = "Freddy Ramirez"
#The first value of name is 0
print(name[0]) #output F
print(name[7]) #output R

name = "Michael Jackson"
#The last one value is -1
print(name[-1]) #output n

#The first could be a -15
print(name[-15]) #output -15

#We can treat the string as a sequence and perform sequence operations:
print(name[0:4], name[8:12]) #output Mich Jack

#The two indicates we'd select every second variable
print(name[::2]) #output McalJcsn

#In this case we return every second value up to index four
print(name[0:5:2]) #output Mca

#This is slicing
my_string = len("Hello, world!")
print(my_string) #output 13

#Thi is a concatenation
print(name + " is the best") #output Michael Jackson is the best
print(name + "\nis the best") #output Michael JAckson 
                              #is the best
print(name + "is the\tbest")#output Michael Jackson is the  best


#Methods
a = "This a method whit uppercase"
b = a.upper()
print(b) #output  THIS A METHOD WHIT UPPERCASE

c = a.replace("This", "For this") #We need the argument the first is the real and the second is the replace
print(c) #output For this a method whit uppercase

d = a.find("method")
print(d) #output the index 7 because there is it
e = a.find("here there is nothing")        #if the substring is not in the string the result will be -1

name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.") #My name is John and I am 30 years old.

name = "John"
age = 50
print("My name is {} and I am {} years old.".format(name, age)) #My name is John and I am 50 years old.

x = 10
y = 20
print(f"The sum of x and y is {x+y}.")  #The sum of x and y is 30.
