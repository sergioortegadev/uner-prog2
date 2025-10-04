import tienda
import producto

tienda1 = tienda.Tienda()

producto1 = producto.Producto('Chocolates')
producto2 = producto.Producto('Gaseosa')
producto3 = producto.Producto('Mani')

tienda1.agregar_productos(producto1)
tienda1.agregar_productos(producto2)
tienda1.agregar_productos(producto3)

print((tienda1))

tienda1.remover_productos(producto1)

print((tienda1))