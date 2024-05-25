def calcular(operacion):
    numeros = []  # Lista para almacenar los números a operar
    while True:
        num = input(f"Ingrese un número para {operacion} o 's' para realizar la {operacion}: ")
        if num.lower() == 's':
            break  # Sale del bucle interno si se ingresa 's'
        num = float(num)
        numeros.append(num)  # Agrega el número a la lista

    if operacion == '+':
        resultado = sum(numeros)  # Suma todos los números de la lista
    elif operacion == '-':
        resultado = numeros[0] - sum(numeros[1:])  # Resta los números de la lista
    elif operacion == '*':
        resultado = 1
        for num in numeros:
            resultado *= num  # Multiplica todos los números de la lista
    elif operacion == '/':
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado /= num  # Divide los números de la lista

    print(f"El resultado de la {operacion} es:", resultado)


def main():
    while True:
        print("Seleccione la operación que desea realizar:")
        print("1. Suma (+)")
        print("2. Resta (-)")
        print("3. Multiplicación (*)")
        print("4. División (/)")
        opcion = input("Ingrese el número correspondiente a la operación deseada: ")

        if opcion == '1':
            calcular('+')
        elif opcion == '2':
            calcular('-')
        elif opcion == '3':
            calcular('*')
        elif opcion == '4':
            calcular('/')
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

        continuar = input("¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() != 's':
            break  # Sale del bucle si se ingresa algo diferente de 's'


if __name__ == "__main__":
    main()
