number = int(input("Type a number to add: "))
if number <=0:
    print("The number should be a positive integer")
else:
    number = str(number)
    add = 0
    for digit in number:
        digit = int (digit)
        add = add + digit
    print ("The addition the number", number, "is", add)
        