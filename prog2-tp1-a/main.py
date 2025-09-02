# Ejercicio 1
print(" - Ejercicio 1 - ")
def recibir():
 name = input(f'{' Ingrese su nombre: '}')
 print(f'Hola {name}')

#recibir()


# Ejercicio 2
print("\n - Ejercicio 2 - ")
def numero_no_contiene_digitos(numero, 
digitos_prohibidos):
  for digito in str(numero):
        for digito_prohibido in map(str,digitos_prohibidos):
            if digito == digito_prohibido:
                return False

  return True
 
 
#print(numero_no_contiene_digitos(12345678, []))
#print(numero_no_contiene_digitos(12345678, [15, 16 , 9]))
#print(numero_no_contiene_digitos(12345678, [5, 6 , 0]))

# Ejercicio 3
print("\n - Ejercicio 3 - ")
def invertir_palabras(entrada):
   entrada_a_lista = entrada.split(',')
   entrada_a_lista.reverse()
   return ','.join(entrada_a_lista)

#print(invertir_palabras('Hola,Mundo'))



# Ejercicio 4
print("\n - Ejercicio 4 - ")
def numeros_pares_elevados(entrada):
   num_al_cuadrado = []
   for digito in entrada:
        if digito % 2 == 0:
            num_al_cuadrado.append(digito ** 2)
   print(num_al_cuadrado)
   

#numeros_pares_elevados([1,2,3,4])
#numeros_pares_elevados([1,3,5])
#numeros_pares_elevados([1,2,3,4,5,6,7,8,9,0])


# Ejercicio 5
print("\n - Ejercicio 5 - ")
def edad_valida(edad):
    try:
        if not isinstance(edad, int):
            return False
        return 1 < edad < 120
    except TypeError: 
       return False

#print(edad_valida(1))
#print(edad_valida(5))
#print(edad_valida('5'))
#print(edad_valida(125))
#print(edad_valida(10.5))

# Ejercicio 5
print("\n - Ejercicio 5b - ")
def edad_valida(edad):
    try:
        if type(edad) != int:
            raise TypeError
        return 1 < edad < 120
    except TypeError:
       #print(f'type error {edad}')
       return False

#print(edad_valida(1))
#print(edad_valida(5))
#print(edad_valida('5'))
#print(edad_valida(125))
#print(edad_valida(10.5))

# Ejercicio 6
print("\n - Ejercicio 6 - ")
def es_fin_de_semana(dia):
    return dia in [1, 7]

#print(es_fin_de_semana(1))


# Ejercicio 7
print("\n - Ejercicio 7 - ")
def calcular_hipotenusa(cateto1, cateto2):
    if cateto1>0 and cateto2>0:
        return (cateto1 ** 2 + cateto2 ** 2) ** 0.5
    return 'los valores deben ser mayor a cero'

#print(calcular_hipotenusa(2,2))
#print(calcular_hipotenusa(3,4))
#print(calcular_hipotenusa(2,0))

# Ejercicio 8
print("\n - Ejercicio 8 - ")
import pitagoras
print(pitagoras.calcular_hipotenusa(4,5))
print(pitagoras.calcular_hipotenusa(3,4))
print(pitagoras.calcular_hipotenusa(3,0))

# Ejercicio 9
print("\n - Ejercicio 9 - ")
def suma(entero_positivo):
    return 0 if entero_positivo == 0 else entero_positivo + suma(entero_positivo - 1)

#print(suma(0))
#print(suma(5))

# Ejercicio 10
print("\n - Ejercicio 10 - ")
print(" - False - ")
False