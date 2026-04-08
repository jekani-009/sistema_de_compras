#productos
def agregar_producto(lista):
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    lista.append({"nombre": nombre, "precio": precio})

def mostrar_productos(lista):
    for p in lista:
        print(p["nombre"], p["precio"])