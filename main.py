import funciones

while True:
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")


    num1 = int(input("Ingrese el primer número: "))
    num2 = int (input("Ingrese el segundo número: "))

    opcion = input("Ingrese el número de la operación deseada: ")

    if opcion == '5':
        print("Saliendo de la calculadora.")
        break


    if opcion == '1':
        print("El resultado de la suma es:", suma(num1, num2))
    elif opcion == '2':
        print("El resultado de la resta es:", resta(num1, num2))
    elif opcion == '3':
        print("El resultado de la multiplicación es:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("El resultado de la división es:", division(num1, num2))
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")