#List are also ordered sequences
# A list is represented with square brackets
l = ["Freddy Ramirez", 1090, 1090, 320]
print(l)

#This will create a new element
l.extend(["Nicolas",202, 3023.3])

#This will create a new element
l.append(["New list",74322, 4324234,4234234234,3423.423])
del l[0] 
print(l)#output will delete the first element

A = [1]
A.append([2, 3, 4, 5])
print(len(A))  #output 2

string = ["A,B,C,D"]
string_converted = string[0].split(",")
print(string_converted) #['A', 'B', 'C', 'D']

a = ["hard rock", 202323, 2323]
#This a copy of a
b = a[:]
#help(a) #Show help on the type of variable a
print(b) #output ["hard rock", 202323, 2323]