N = int (input("Type a range to calculate the numbers Fibonacci "))
if N <=0:
    print("The number should be an integer positive number")
else:
    print("The numbers Fibonacci")
    a = 0
    b = 1
    c = a + b
    print (f"\a{a}\n{b}")
    for i in range (N-2):
        print (c)
        a = b
        b = c
        c = a + b