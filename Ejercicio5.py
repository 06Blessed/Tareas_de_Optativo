# Ejercicio 5 - Vehículo de una agencia

class Vehiculo:

  def __init__(self, marca, modelo, anio, precio):
    self.marca = marca
    self.modelo = modelo
    self.anio = anio
    self.precio = precio

  def descripcion_comercial(self):
    # Usamos f-strings para armar el texto y darle formato de miles al precio
    return f"{self.marca} {self.modelo} {self.anio} - {self.precio:,.0f} Gs."


auto1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
auto2 = Vehiculo("Kia", "Rio", 2022, 75000000)

print(auto1.descripcion_comercial())
print(auto2.descripcion_comercial())