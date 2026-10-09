#Ejercicio 2 - Producto de almacen

class Producto:

  def __init__(self, nombre, precio_unitario, cantidad_stock):
    self.nombre = nombre
    self.precio_unitario = precio_unitario
    self.cantidad_stock = cantidad_stock

  def calcular_valor_total(self):
    # Multiplica cuántas unidades tenemos por el precio para saber la plata total en stock
    return self.precio_unitario * self.cantidad_stock

  def __str__(self):
    total = self.calcular_valor_total()
    return f"Producto: {self.nombre} - Precio Unitario: Gs. {self.precio_unitario:,} - Stock: {self.cantidad_stock} un. (Valor total: Gs. {total:,})"


# Probando con tres productos de despensa
prod1 = Producto("Yerba Mate 1kg", 28000, 15)
prod2 = Producto("Fideos 500g", 7500, 30)
prod3 = Producto("Aceite de Girasol 900ml", 15000, 10)

print(prod1)
print(prod2)
print(prod3)