import os

menuHome="""bienvenido a el programa conversor de monedas
1. COP--->USD
2. USD--->JPY
3. JPY--->COP
4. salir"""

isActiveConversion=True

while isActiveConversion:
    os.system("clear")
    print (menuHome)
    option=int(input("seleccione una pocion: "))
     
    match option:
        case 1:
            os.system("clear")
            print ("ingresa la cantidad que quieras convertir: ")
            PesoColombiano = float(input("registra la cantidad de pesos colombianos que deseas convertir: "))
            dolares = PesoColombiano / 4032.70
            print(f'esa cantidad en dolares es: {dolares:.2f}$')
            input("presiona ENTER continuar")

        case 2:
            os.system("clear")
            print ("ingresa la cantidad que quieras convertir: ")
            dolar = float(input("ingresa la cantidad de dolares que deseas convertir: "))
            yenJapones = dolar * 147.31
            print (f'esa cantidad en yenes es {yenJapones:.2f}¥')
            input("presiona ENTER para continuar")
        
        case 3:
            os.system("clear")
            print ("ingresa la cantidad que quieras convertir: ")
            yenesJaponeses = float(input("ingresa la cantidad de yenes que quieres convertir: "))
            cop = yenesJaponeses * 0.037
            print(f'esa cantidad en pesos colombianos es {cop:.2f}$')
            input("presiona ENTER para continuar")

        case 4:
            print ("gracias por usar el programa")

            isActiveConversion=False

        case _:
            os.system("clear")
            print ("opcion invalida intente denuevo")         