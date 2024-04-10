num1 = int(input("Type a number: "))
num2 = int(input("Type another number: "))

if num1 < num2:
    for x in range(num1, num2 + 1):
        if x % 2 == 0:
            print(f"{x} is an even number")
        else:
            print(f"{x} is an odd number")
else:
    print("The first number should be less than the second number")