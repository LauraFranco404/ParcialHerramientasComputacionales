inventario = {"desayuno" : "001" , "almuerzo" : "002" , "jugo en agua" : "003" ,
              "jugo en leche" : "004" , "café" : "005" , "gaseosa" : "006" ,
              "botella de agua" : "007" , "fruta picada" : "008" , "cheesecake" : "009"}

inventario = {"001" : "desayuno" , "002" : "almuerzo" , "003" : "jugo en agua" ,
               "004" : "jugo en leche" , "005" : "café" , "006" : "gaseosa" ,
              "007" : "botella de agua" , "008" : "fruta picada" , "009" : "cheesecake"}

precios = {"001" : 9000 , "002" : 9000 , "003" : 4000 ,
               "004" : 5000 , "005" : 4500 , "006" : 3500 ,
              "007" : 3000 , "008" : 4000 , "009" : 5000}

def cafeteria():
    print("Bienvenido a la cafetería Franco :)." + "\n" + "Para facturar digite 1 , para salir de la cafetería digite 2")
    dig = int(input())
    while dig == 1:
        ans = None
        costo = 0
        code = []
        nP = 0
        print()
        print("Por favor digite su cédula")
        cc = input()
        print("Por favor digite su rol (estudiante o profesor)")
        rol = input()
        print()
        if rol == "estudiante":
            print("Estimado estudiante; si hace parte del programa de becas, por favor digite 1, de lo contrario, digite 2")
            beca = int(input())
            if beca == 1:
                descuento = 0.5
            if beca == 2:
                descuento = 0.3
        if rol == "profesor":
            descuento = 0.2

        for key in inventario:
            print(key , inventario[key])
            
        print()        
        print("Digite el código del producto")
        codigo = input()
        code.append(codigo)
        print(inventario[codigo])
        precio = precios[codigo]
        print()

        print("El precio del producto que escogió es de " + str(precio))
        print("¿Cuántas unidades desea llevar?")
        unidades = int(input())
        costo += (precio * unidades) - (precio * unidades * descuento)  
        print()
        print("¿Desea llevar otro producto? ;)" + "\n" + "Si es así, digite 1. Si desea imprimir su recibo digite 2")
        oP = int(input())
        print()
        while oP == 1:
            nP += 1
            for key in inventario:
                print(key , inventario[key])
            print()
            print("Digite el código del producto")
            codigo = input()
            code.append(codigo)
            print(inventario[codigo])
            precio = precios[codigo]
            print()
            print("El precio del producto que escogió es de " + str(precio))
            print("¿Cuántas unidades desea llevar?")
            unidades = int(input())
            costo += (precio * unidades) - (precio * unidades * descuento)          
            print()
            print("¿Desea llevar otro producto? ;)" + "\n" + "Si es así, digite 1. Si desea imprimir su recibo digite 2")
            oP = int(input())
            print()
        code = ",".join(code)
        if oP == 2:
            if nP >= 1:
                ans = "El " + rol + " con cédula " + str(cc) + ", debe pagar " + str(costo) + " por los productos con código " + code
            elif nP == 0:
                ans = "El " + rol + " con cédula " + str(cc) + ", debe pagar " + str(costo) + " por el producto con código " + code
        print(ans)



        print()
        print("Bienvenido a la cafetería Franco :)." + "\n" + "Para facturar digite 1 , para salir de la cafetería digite 2")
        dig = int(input())

    if dig == 2:
        print("Fue un placer atenderlos. Tengan un maravilloso día :D")
cafeteria()
