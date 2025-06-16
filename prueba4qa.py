entradas = {}
stock_viernes = 150
stock_sabado = 180

def comprar():
    global stock_viernes, stock_sabado
    nombre = input("Nombre del comprador: ").strip()

    if nombre in entradas:
        print("Este nombre ya compró una entrada")
        return

    print("Funciones disponibles:")
    print("1. Cats - Viernes")
    print("2. Cats - Sábado")
    opcion = input("Seleccione la función (1 o 2): ")

    if opcion == "1":
        if stock_viernes > 0:
            entradas[nombre] = "viernes"
            stock_viernes -= 1
            print("Entrada comprada para el viernes")
        else:
            print("No quedan entradas para el viernes")
    elif opcion == "2":
        if stock_sabado > 0:
            entradas[nombre] = "sabado"
            stock_sabado -= 1
            print("Entrada comprada para el sábado")
        else:
            print("No quedan entradas para el sábado")
    else:
        print("Opción inválida")

def cambiar_funcion():
    global stock_viernes, stock_sabado
    nombre = input("Ingrese su nombre: ").strip()

    if nombre not in entradas:
        print("No hay ninguna entrada registrada con ese nombre")
        return

    actual = entradas[nombre]
    nueva = "sabado" if actual == "viernes" else "viernes"

    if nueva == "viernes" and stock_viernes == 0:
        print("No hay cupos para el viernes")
        return
    if nueva == "sabado" and stock_sabado == 0:
        print("No hay cupos para el sábado")
        return

    confirmar = input(f"¿Seguro que quiere cambiar a {nueva}? (s/n): ").lower()
    if confirmar == "s":
        entradas[nombre] = nueva
        if actual == "viernes":
            stock_viernes += 1
            stock_sabado -= 1
        else:
            stock_sabado += 1
            stock_viernes -= 1
        print("Cambio realizado con éxito")
    else:
        print("No se hizo el cambio")

def mostrar_stock(): 
    print(f"\nEntradas disponibles:")
    print(f"- Viernes: {stock_viernes}")
    print(f"- Sábado: {stock_sabado}")
    print(f"Total de entradas vendidas: {len(entradas)}\n")

def main():
    while True:
        print("------ CAFECONLECHE - TÓTEM DE ENTRADAS ------")
        print("1. Comprar entrada a Cats")
        print("2. Cambio de función")
        print("3. Mostrar stock de funciones")
        print("4. Salir")

        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            comprar()
        elif opcion == "2":
            cambiar_funcion()
        elif opcion == "3":
            mostrar_stock()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!\n")

main()