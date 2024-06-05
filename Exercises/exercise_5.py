num1 = int(input("Type a number: "))
num2 = int(input("Type another number: "))

if num1 < num2:
    for meter in range(num1, (num2 + 1)):
        print(meter)
else:
    print("The first number should be greater than the second number")