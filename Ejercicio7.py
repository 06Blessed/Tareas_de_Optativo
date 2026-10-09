# Ejercicio 7 - Control de stock con alertas

class ProductoConStock:

  def __init__(self, nombre, stock_actual, stock_minimo):
    self.nombre = nombre
    self.stock_actual = stock_actual
    self.stock_minimo = stock_minimo

  def ingresar_mercaderia(self, cantidad):
    self.stock_actual += cantidad
    print(
        f"Se ingresaron {cantidad} un. de {self.nombre}. Stock actual:"
        f" {self.stock_actual}"
    )

  def registrar_venta(self, cantidad):
    # Validamos que haya suficientes unidades antes de vender
    if cantidad <= self.stock_actual:
      self.stock_actual -= cantidad
      print(
          f"Venta de {cantidad} un. de {self.nombre} realizada. Stock"
          f" restante: {self.stock_actual}"
      )
      # Controlamos si quedó por debajo del mínimo para tirar alerta
      if self.stock_actual < self.stock_minimo:
        print(
            f"⚠️ ¡ALERTA DE REPOSICIÓN! El producto '{self.nombre}' está por"
            f" debajo del mínimo ({self.stock_minimo} un.)."
        )
    else:
      print(
          f"❌ No se pudo vender {cantidad} un. de {self.nombre}: Stock"
          f" insuficiente ({self.stock_actual} disponibles)."
      )


p_stock = ProductoConStock("Azúcar 1kg", 10, 5)
p_stock.registrar_venta(7)  # Deja el stock en 3, activando la alerta