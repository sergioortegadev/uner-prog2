import cancion
import circulo

print(f'\n--------------------------\n  Prog2 - Tp2 - Parte B\n\n   Integrantes: \n   - Edgardo Sandoval\n   - Jorge Ruiz\n   - Sergio Ortega\n')

# Ejercicio 2

cancion_Rollings = cancion.Cancion('Let`s Spend The Night Together', 216, 'Rock and roll')
cancion_Daff_Punk = cancion.Cancion('Motherboard', 342, 'Electronica')
cancion_Pulp = cancion.Cancion('Common People', 248, 'Pop')

# Ejercicio 3
print('\n+++ Ejercicio 3 +++\n')

print(cancion_Rollings.obtener_genero())
print(cancion_Daff_Punk.obtener_genero())
print(cancion_Pulp.obtener_genero())


# Ejercicio 4
print('\n+++ Ejercicio 4 +++\n')

cancion_Daff_Punk.establecer_genero('Música Electrónica Futurista')
print(cancion_Daff_Punk.obtener_genero())


# Ejercicio 6

circulo_chico = circulo.Circulo(10.1)
circulo_mediano = circulo.Circulo(100.1)
circulo_grande = circulo.Circulo(1000.1)


# Ejercicio 7
print('\n+++ Ejercicio 7 +++\n')

print(circulo_chico.obtener_diametro())
print(circulo_mediano.obtener_diametro())
print(circulo_grande.obtener_diametro())


# Ejercicio 8
print('\n+++ Ejercicio 8 +++\n')

print(circulo_chico.pi)
print(circulo_mediano.pi)
print(circulo_grande.pi)


# Ejercicio 9
print('\n+++ Ejercicio 9 +++\n')

circulo_a = circulo.Circulo(5)
circulo_b = circulo.Circulo(5)

print(f'Comparación circulo a == b: {circulo_a == circulo_b}')


# Ejercicio 10
print('\n+++ Ejercicio 10 +++\n')

print(f'Comparación perimetros, circulo a == b: {circulo_a.obtener_perimetro() == circulo_b.obtener_perimetro()}')


print('\n+++ Fin del Ejercicio +++\n')
