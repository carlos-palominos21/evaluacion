#evaluacion fina
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock= {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}
def stock_marca(marco):
    marco=marco.lower()
    total_stock=sum(stock[marco][1] for moledo in productos if productos[marco][0].lower())
    print(f"el stock es: {total_stock}")
def busqueda_precio(p_min, p_max):
    resultado=[f"{productos[modelo][0]}--{modelo}"for modelo in stock 
               if p_min <= stock[modelo][0]<=p_max and stock[modelo][1]>0] 
    print(sorted(resultado))
def actualizar_precio(modelo,precio):
    if modelo in stock:
        stock [modelo][0]=precio
        return True
    return False
def menu():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        opc=input("ingrese una opcion valida:")
        match opc:

            case"1":
                stock_marca=input("ingrese marca a consultar:")
                stock_marca(marco)
            case"2":
                try:
                    p_min=input("ingrese precio minimo:")
                    p_max=input("ingrese precio maximo:")
                except ValueError:
                    print("estimado cliente debe poner un valos bueno porfa ")
            case"3":
                while True:
                    modelo=input("ingrese precio nuevo:")
                    try:
                        nuevo_precio=int(input("ingrese precio nuevo:"))
                        if actualizar_precio(modelo, nuevo_precio):
                            print("precio actualizado")
                        else:
                            print("modelo no existe")
                            continuar=input("desea actualizar otro preicio(s/n)?:").lower()
                        if continuar !="s": 
                            break 
                    except ValueError:
                        print("estimado cliente debe ingresar un precio valido porfa")
            case"4":
                print("muchas gracias por utilizar este programa nos vemos ")
            case _:
                print(" ingrese una opcion valida")
menu()