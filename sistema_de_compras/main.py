from productos import agregar_producto, mostrar_productos
from calculos import calcular_total, filtrar_productos

def main():
    productos = []

    while True:
        print("\n1. Agregar")
        print("2. Mostrar")
        print("3. Total")
        print("4. Filtrar")
        print("5. Salir")

        op = input("Opción: ")

        if op == "1":
            agregar_producto(productos)
        elif op == "2":
            mostrar_productos(productos)
        elif op == "3":
            print("Total:", calcular_total(productos))
        elif op == "4":
            limite = float(input("Mayor a: "))
            filtrados = filtrar_productos(productos, limite)
            print(filtrados)
        elif op == "5":
            break

if __name__ == "__main__":
    main()