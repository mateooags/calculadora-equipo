num1 = float(input("Ingrese el primer número: "))
operacion = input("Ingrese la operación (+, -, x, /): ")
num2 = float(input("Ingrese el segundo número: "))
if operacion=="+":
    print("Resultado:", num1+num2)
else:
    if operacion=="-":
        print("Resultado:", num1-num2)
    else:
        if operacion=="x":
            print("Resultado:", num1*num2)
        else:
            if operacion=="/":
                if num2!= 0:
                    print("Resultado:", num1/num2)
                else:
                    print("No se puede dividir por cero. Operacion invalida")
