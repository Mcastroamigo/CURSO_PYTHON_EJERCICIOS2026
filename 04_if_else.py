#Pide dos numeros y muestra el resultado de dividir el mayor entre el menor

num1 = int(input("introduce el numero 1:"))
num2 = int(input("introduce el numero 2:"))

if num1>num2:
    print(f"el numero1 {num1} es mayor que el numero2 {num2} por tanto la division es {num1/num2}")
else:
    print(f"el numero2 {num2} es mayor que el numero1 {num1} por tanto la division es {num2/num1}")
