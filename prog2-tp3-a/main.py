import item
import caja
import estanteria
import deposito

deposito1 = deposito.Deposito()

estanteria1 = estanteria.Estanteria()
estanteria2 = estanteria.Estanteria()

deposito1.agregarEstanteria(estanteria1)
deposito1.agregarEstanteria(estanteria2)

caja1 = caja.Caja(30,40,50,'Carton')
caja2 = caja.Caja(60,50,70,'Madera')
caja3 = caja.Caja(10,20,30,'Plastico')
caja4 = caja.Caja(60,50,70,'Madera')
caja5 = caja.Caja(70,50,30,'Carton')
caja6 = caja.Caja(35,45,25,'Plastico')

estanteria1.agregarCaja(caja1)
estanteria1.agregarCaja(caja2)
estanteria1.agregarCaja(caja3)
estanteria2.agregarCaja(caja4)
estanteria2.agregarCaja(caja5)
estanteria2.agregarCaja(caja6)

item1 = item.Item('Juego sabanas')
item2 = item.Item('Caja biromes')
item3 = item.Item('Caja juguetes 500')
item4 = item.Item('Caja juguetes 1000')
item5 = item.Item('Laptop')
item6 = item.Item('Router')
item7 = item.Item('Almohada')
item8 = item.Item('Cubiertos')
item9 = item.Item('Impresora')
item10 = item.Item('Cuadernos')
item11 = item.Item('Tornillos')
item12 = item.Item('Pintura')

caja1.agregarItem(item1)
caja1.agregarItem(item2)
caja2.agregarItem(item3)
caja2.agregarItem(item4)
caja3.agregarItem(item5)
caja3.agregarItem(item6)
caja4.agregarItem(item7)
caja4.agregarItem(item8)
caja5.agregarItem(item9)
caja5.agregarItem(item10)
caja6.agregarItem(item11)
caja6.agregarItem(item12)



# print(item12.obtenerNumero())
# print(item2.obtenerNumero())
# print(str(item1))


# print(str(caja1))
# print(str(caja2))

# print(str(estanteria1))
# print(str(estanteria2))

# deposito1 = deposito.Deposito()
print(str(deposito1))

estanteria1.removerCaja(caja1)
estanteria2.agregarCaja(caja1)

print(str(deposito1))