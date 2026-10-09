# Ejercicio 10 - Carrito de compras de un e-commerce

class ItemCarrito:

  def __init__(self, producto_nombre, precio_unitario, cantidad):
    self.producto_nombre = producto_nombre
    self.precio_unitario = precio_unitario
    self.cantidad = cantidad

  def subtotal(self):
    return self.precio_unitario * self.cantidad


class Carrito:

  def __init__(self):
    self.items = []

  def agregar_item(self, item):
    self.items.append(item)

  def calcular_total(self):
    return sum(item.subtotal() for item in self.items)

  def mostrar_detalle(self):
    print("\n🛒 Detalle del Carrito de Compras:")
    for item in self.items:
      print(
          f" - {item.producto_nombre} x{item.cantidad} | Subtotal: Gs."
          f" {item.subtotal():,}"
      )
    print(f"💰 Total a Pagar: Gs. {self.calcular_total():,}")


c_item1 = ItemCarrito("Yerba Mate", 28000, 2)
c_item2 = ItemCarrito("Galletitas", 6000, 3)
mi_carrito = Carrito()
mi_carrito.agregar_item(c_item1)
mi_carrito.agregar_item(c_item2)
mi_carrito.mostrar_detalle()