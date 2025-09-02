from impresiones import declarar_comida_favorita2
# Programación 2 - TP 1
print("\n   Integrantes del grupo AI\n   + Edgardo Sandoval, Jorge Ruiz y Sergio Ortega + \n\n")

# Ejercicio 1
print("\n - Ejercicio 1 - ")
def realizar_calculo():
 print(' - Ingresar tipo de operación')
 opcion = input('  1- Suma\n  2- Resta\n  3- Multiplicacion\n  4- Division\n\n')

 match opcion:
  case '1':
    print('\n - Sumar -')
    num1=float(input('   ingrese primer número: '))
    num2=float(input('   ingrese segundo número: '))
    return print(f'  La suma es = {num1 + num2}')
   
  case '2':
    print('\n - Restar -')
    num1=float(input('   ingrese primer número: '))
    num2=float(input('   ingrese segundo número: '))
    return print(f'  La resta es = {num1 - num2}')
  case '3':
    print('\n - Multiplicar -')
    num1=float(input('   ingrese primer número: '))
    num2=float(input('   ingrese segundo número: '))
    return print(f'  La multiplicación es = {num1 * num2}')
  case '4':
    print('\n - Dividir -')
    num1=float(input('   ingrese primer número: '))
    num2=float(input('   ingrese segundo número: '))
    if num2 == 0:
      print('\n   Error matematico, division por cero\n')
      return realizar_calculo()
    return print(f'  La división es = {num1 / num2}')
  case _:
   print('\n   Opción no válida, seleccione de 1 al 4')
   realizar_calculo()

realizar_calculo()


# Ejercicio 2
print("\n - Ejercicio 2 -")
def numero_en_orden_ascendente(numero):
  return list(str(numero)) == sorted(str(numero))

print(numero_en_orden_ascendente(2341))
print(numero_en_orden_ascendente(234))
print(numero_en_orden_ascendente(500))

# Ejercicio 3
print("\n - Ejercicio 3 - ")
def numeros_impares_juntos(entrada):
  num_concatenados = []
  for digito in entrada:
    if digito % 2 != 0:
      num_concatenados.append(str(digito))
  resultado=",".join(num_concatenados)
  print(resultado)
     
numeros_impares_juntos([1, 4, 7, 2, 9, 5])
numeros_impares_juntos([1, 4, 8, 0])

# Ejercicio 4
print("\n - Ejercicio 4 - ")
def lista_elementos_en_comun(lista1, lista2):
  comunes = set(lista1) & set(lista2)
  print(comunes)

lista_elementos_en_comun([1 , 5, 5, 6, 7, 8, 8, 0], [1, 7, 7 , 9, 4, 4, 6])
lista_elementos_en_comun([2 , 4, 5, 6, 7, 8, 9, 0], [2, 4, 4 , 4, 4, 4, 8])

# Ejercicio 5
print("\n - Ejercicio 5 - ")
def clave_valida(clave):
 if len(clave) < 6 or len(clave) > 20:
   return False
 if ' ' in clave:
   return False
 if not any(caracter.isdigit() for caracter in clave):
    return False
 return True
   

print(clave_valida('hola1'))
print(clave_valida('hola25')) 
print(clave_valida('holamundo') )
print(clave_valida('holamundoholamundo hola2') )
print(clave_valida('mundoholamundo hola2') )
print(clave_valida('mundoholamundo1hola2')) 

# Ejercicio 6
print("\n - Ejercicio 6 - ")
def persona_mayor_de_edad(edad):
  return edad >= 18

print(persona_mayor_de_edad(17))
print(persona_mayor_de_edad(18))
print(persona_mayor_de_edad(19))

# Ejercicio 7
print("\n - Ejercicio 7 - ")
def declarar_comida_favorita(nombre_persona,  nombre_comida):
  print("La comida favorita de " + nombre_persona + " se llama: " + nombre_comida)


declarar_comida_favorita('Pablo', 'pollo frito')
declarar_comida_favorita('Pedro', 'canelones')
declarar_comida_favorita('Juan', 'pizza')

# Ejercicio 8
print("\n - Ejercicio 8 - ")
declarar_comida_favorita2('Pablo', 'pollo frito')
declarar_comida_favorita2('Pedro', 'canelones')
declarar_comida_favorita2('Juan', 'pizza')

# Ejercicio 9
print("\n - Ejercicio 9 - ")
def cuenta_regresiva(entero_positivo):
  if entero_positivo < 0:
    return
  print(entero_positivo)
  cuenta_regresiva(entero_positivo - 1)

cuenta_regresiva(5)

# Ejercicio 10
print("\n - Ejercicio 10 - ")
print("   True ")
True