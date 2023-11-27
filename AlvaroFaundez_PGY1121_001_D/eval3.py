import os
os.system("cls")

tipos = []
patentes= []
marcas = []
precios= []
multas= []
fecharesitrovehiculo=[]
nombres=[]

def menu():
    print("menu")
    print("1. Registrar vehiculo")
    print("2. Buscar vehiculo")
    print("3. imprimir certificado")
    print("4. Salir")
    return input("digita opcion: ")

def registrar():
    print("registro")
    while True: 
        try:
            tipo = int(input("ingresa eñ tipo de vehiculo ya sea (auto,camioneta,suv): "))
            if tipo == "auto" or tipo == "camioneta" or tipo== "suv":
                tipos.append(tipo)
                break 
            else:
                print("Error, tipo debe ser igual a auto, camioneta o suv")
        except:
            print("excepcion en tipo")
    
    while True:

            paten = input("ingresa patente del vehiculo: ")
            patentes.append(paten)
            break
  

    while True:
        try:
            marca = input("ingresa la marca del vehiculo: ")
            if len(marca) >= 2 and len(marca) <= 15:
                marcas.append(marca)
                break
            else:
                print("Error, marca debe tener a lo min 2 char y maximo 15 char")
        except:
            print("Excepcion en marca")
    
    while True: 
        try:
            multa = int(input("ingresa monto de multa: "))
            if multa >=0:
                multas.append(multa)
                break 
            else:
                print("Error, multa debe ser positivo o 0")
        except:
            print("excepcion en multa, no tiene multa")

    while True: 
        try:
            fecharegis=input("ingrese la fecha de registro del vehiculo: ")
            fecharesitrovehiculo.append(fecharegis)
            break
        except:
            print("excepcion en nombre")


    while True: 
        try:
            nombre=input("ingrese el nombre del dueño: ")
            if len(nombre) >=1 and len(nombre)<=15:
                nombres.append(nombre)
                break
            else:
                print("error el nombre debe tener minimo 1 char y max 15 char")
        except:
            print("excepcion en nombre")

    while True:
        try:
            precio=float(input("ingrese el precio del vehiculo: "))
            if precio>= 5000000:
                precios.append(precio)
                break
            else:
                print("precio debe ser mayor o igual a $5000000")
        except: 
            print("excepcion en precio")

def buscar():
    print("buscar")
    try:
        paten = int(input("patente a buscar: "))
        if paten in patentes: 
            indice = patentes.index(paten)
            print("vehiculo encontrado: ")
            print(f"tipo: {tipos[indice]}")
            print(f"patente   : {patentes[indice]}")
            print(f"marca : {marcas[indice]}")
            print(f"precio: {precios[indice]}")
            print(f"multas   : {multas[indice]}")
            print(f"dueño: {nombres[indice]}")
            print(f"fecha de registro del vehiculo: {fecharesitrovehiculo[indice]}")
        else:
            print("patente no se encuentra en la lista")
    except:
        print("Excepcion de patente,")

def certificados():
    print("""que certificado desea imprimir: 
          1. certificado de emision de contaminantes 
          2. certificado de multas 
          
          """)
    opc=input("ingrese una opcion")

    if opc== "2":
        print("                 certificadosde multas")
        print("---------------------------------------------------------------------")
        for i in range(len(multas)):
            if multas[i] < 1500:
            print(f"{patentes[i]:20s}| {nombres[i]:15} {multas[i]:5d}")
        print("---------------------------------------------------------------------")
    

def salir():
    print("\nSalir")

# principal
while True:
    try:
        opcion = menu()
        if opcion == "4":
            salir()
            break
        elif opcion == "1":
            registrar()
        elif opcion == "2":
            buscar()
        elif opcion == "3":
            certificados()
        else:
            print("\nopcion incorrecta, enter para continuar ...")
        input("Enter para continuar")
    except:
        print("Excepcion")