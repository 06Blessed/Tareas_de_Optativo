# Ejercicio 13 - Habitación de un hotel

class Habitacion:

  def __init__(self, numero, tipo, tarifa_noche):
    self.numero = numero
    self.tipo = tipo
    self.tarifa_noche = tarifa_noche
    self.ocupada = False  # False = Libre, True = Ocupada

  def ocupar(self):
    # Validamos el estado antes de cambiarlo para no ocupar una ya ocupada
    if not self.ocupada:
      self.ocupada = True
      print(
          f"🏨 La habitación {self.numero} ({self.tipo}) ha sido ocupada con"
          " éxito."
      )
    else:
      print(
          f"❌ Error: La habitación {self.numero} ya se encuentra ocupada"
          " actualmente."
      )

  def liberar(self):
    self.ocupada = False
    print(f"🚪 La habitación {self.numero} ha sido liberada y ya está disponible.")

  def calcular_costo_estadia(self, noches):
    return self.tarifa_noche * noches


# Simulación del ciclo completo requerida
habitacion_hotel = Habitacion(204, "Doble", 180000)
habitacion_hotel.ocupar()
habitacion_hotel.ocupar()  # Intento fallido de ocupar una ya ocupada

noches_hospedaje = 3
costo_total = habitacion_hotel.calcular_costo_estadia(noches_hospedaje)
print(
    f"Costo total por {noches_hospedaje} noches: Gs. {costo_total:,.0f}"
)

habitacion_hotel.liberar()