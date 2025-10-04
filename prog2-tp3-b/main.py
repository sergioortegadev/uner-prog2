import empresa
import producto
import empleado

# Ejercicio 10
empresa1 = empresa.Empresa('Soft Factory II - UNER')
empresa2 = empresa.Empresa('Proceres Soft')


empleado1 = empleado.Empleado('Juan' , 'Perez')
empleado2 = empleado.Empleado('Maria' , 'Gomez')
empleado3 = empleado.Empleado('John' , 'Doe')
empleado4 = empleado.Empleado('Manuel', 'Belgrano')
empleado5 = empleado.Empleado('Juana' , 'Azurduy')
empleado6 = empleado.Empleado('Mariano' , 'Moreno')

producto1 = producto.Producto('Systema Contable')
producto2 = producto.Producto('CRM Ultra Bueno')

producto3 = producto.Producto('Revolución de Mayo')
producto4 = producto.Producto('Guerra de Independencia')

empresa1.agregar_producto(producto1)
empresa1.agregar_producto(producto2)
empresa1.alta_empleado(empleado1)
empresa1.alta_empleado(empleado2)
empresa1.alta_empleado(empleado3)

empresa2.agregar_producto(producto3)
empresa2.agregar_producto(producto4)
empresa2.alta_empleado(empleado4)
empresa2.alta_empleado(empleado5)
empresa2.alta_empleado(empleado6)


empresa1.baja_empleado(empleado1)
empresa1.baja_empleado(empleado3)

print(' - Imprime Empresa Completa -\n')
print(empresa1)
print(empresa2)