def absoluto(numero):
    if numero == 0:
        return 0

    if numero < 0:
        return numero * -1
    else:
        return numero

print (absoluto(-20))