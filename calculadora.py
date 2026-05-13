num1=float(input("ingrese el primer numero:"))
num2=float(input("Ingrese el segundo numero:"))
print ("operaciones")
print ("1: Suma")
print ("2: Resta")
print ("3: multiplicacion")
print ("4: division")
operacion = input("Elige una operacion:")
if (operacion == "1"):
    resultado = num1+num2
    print(resultado)
elif (operacion == "2"):
    resultado = num1-num2
    print(resultado)
elif (operacion == "3"):
    resultado = num1*num2
    print(resultado)
elif (operacion == "4"):
    resultado = num1 / num2
if (num2 !=0):
    print (resultado)
else:
    print("Error, el numero es 0")
