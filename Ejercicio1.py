#Ejercicio 1 - Ficha de clientes
class Cliente:

  def __init__(self, nombre, cedula, telefono):
    # Acá guardamos los datos básicos que nos pasa el cliente al crearlo
    self.nombre = nombre
    self.cedula = cedula
    self.telefono = telefono

  def __str__(self):
    # Esto te arma un texto ordenado y bonito para mostrar la ficha de forma legible
    return f"Cliente: {self.nombre} | Cédula: {self.cedula} | Teléfono: {self.telefono}"


# Probando con dos clientes distintos para verificar que cada objeto guarda lo suyo
cliente1 = Cliente("Carlos Gómez", "4567890", "0981123456")
cliente2 = Cliente("María Benítez", "1234567", "0972987654")

print(cliente1)
print(cliente2)