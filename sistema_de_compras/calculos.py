def calcular_total(lista):
    return sum(p["precio"] for p in lista)
def filtrar_productos(lista, limite):
    return [p for p in lista if p["precio"] > limite]