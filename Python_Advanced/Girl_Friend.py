from datetime import datetime

def main():
    fecha_inicio = datetime(2023, 7, 14)
    print("Recuerda que comenzaste tu relación el día 14 de julio.")

    input("¿Olvidaste la fecha? Presiona Enter para continuar y proporciona la fecha actual.")

    while True:
        try:
            fecha_actual_str = input("Ingrese la fecha actual (YYYY-MM-DD): ")
            fecha_actual = datetime.strptime(fecha_actual_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Error: La fecha ingresada es inválida. Por favor, asegúrate de seguir el formato YYYY-MM-DD.")

    tiempo_transcurrido = fecha_actual - fecha_inicio
    anios = tiempo_transcurrido.days // 365
    meses = (tiempo_transcurrido.days % 365) // 30

    print("Han pasado", anios, "años y", meses, "meses desde que comenzaste tu relación.")

if __name__ == "__main__":
    main()
