# Ejercicio 7
print(" - Ejercicio 7 - ")
def calcular_hipotenusa(cateto1, cateto2):
    if cateto1>0 and cateto2>0:
        return (cateto1 ** 2 + cateto2 ** 2) ** 0.5
    return 'los valores deben ser mayor a cero'