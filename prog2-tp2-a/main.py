import persona
import cuadrado
import cuenta_bancaria
print('\n\n   Prog2 - Tp2 - Parte A')

sergio_ortega = persona.Persona('Sergio', 'Ortega')
sergio_ortega.establecerGrupoSanguineo('A+')
sergio_ortega.establecerAltura('176')

juan_perez = persona.Persona('Juan', 'Perez')
ana_gomez = persona.Persona('Ana', 'Gomez')

print(sergio_ortega.obtenerNombreCompleto())
print(juan_perez.obtenerNombreCompleto())
print(ana_gomez.obtenerNombreCompleto())

saludo = 'hola'

#saludo = 1

print(saludo)
print(type(saludo))

# Ejercicio 7
print('\n Ejercicio 7')

cuadrado1 = cuadrado.Cuadrado(10)
cuadrado2 = cuadrado.Cuadrado(57)
cuadrado3 = cuadrado.Cuadrado(12.8)

# Ejercicio 8
print('\n Ejercicio 8')
print(cuadrado1.obtener_perimetro())
print(cuadrado2.obtener_perimetro())
print(cuadrado3.obtener_perimetro())

# Ejercicio 9
print('\n Ejercicio 9')
print(f' En la clase: {cuadrado.Cuadrado.instancias_creadas}')
print(f' En el primer objeto: {cuadrado1.instancias_creadas}')

# Ejercicio 10
print('\n Ejercicio 10')
cuadrado4 = cuadrado.Cuadrado(13)
cuadrado5 = cuadrado.Cuadrado(13)

print(cuadrado4 == cuadrado5)

# Ejercicio 11
print('\n Ejercicio 11')

print(cuadrado4.obtener_lado() == cuadrado5.obtener_lado())

# Ejercicio 14
print('\n Ejercicio 14 - instanciar 2 cuentas')

cuenta1 = cuenta_bancaria.Cuenta_bancaria(101)
cuenta2 = cuenta_bancaria.Cuenta_bancaria(102)

# Ejercicio 15
print('\n Ejercicio 15 - deposito 1010')

cuenta1.realizar_deposito(1010)

# Ejercicio 16
print('\n Ejercicio 16 - extraccion 500 y saldo')

cuenta1.realizar_extraccion(500)
print(cuenta1.obtener_saldo())

# Ejercicio 16.b
print('\n Ejercicio 16.b - extraccion 1500 y saldo')

print(f'El metodo retorna: {cuenta1.realizar_extraccion(1500)}')
print(cuenta1.obtener_saldo())

