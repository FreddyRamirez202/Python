squares = ["red", "yellow", "green", "purple", "blue"]
for i in range(0,5):
    squares[i]="white"
    print(i)
    print(squares)
    
    
numbers = [1,1,1,1,1,1,1,1,1111,11]
new_numbers = []
i = 0
while(numbers[i]==1):
    new_numbers.append(numbers[i])
    i=i+1
    print(i)
    print(numbers)
    print(new_numbers)
else:
    print("It's not = 1 ")