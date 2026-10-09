# Ejercicio 12 - Cuenta de servicio con planes

class CuentaServicio:

  def __init__(self, cliente, gigas_incluidos):
    self.cliente = cliente
    self.gigas_incluidos = gigas_incluidos
    self.gigas_consumidos = 0.0

  def registrar_consumo(self, gigas):
    self.gigas_consumidos += gigas
    print(f"[{self.cliente}] Consumiste {gigas} GB.")
    if self.gigas_consumidos > self.gigas_incluidos:
      print(
          "⚠️ ¡AVISO! Te has quedado sin datos: el paquete contratado se ha"
          " agotado."
      )

  def gigas_disponibles(self):
    restantes = self.gigas_incluidos - self.gigas_consumidos
    return max(0, restantes)


linea = CuentaServicio("Sofía Vera", 10.0)  # Plan de 10 GB
linea.registrar_consumo(6.0)
print(f"Quedan disponibles: {linea.gigas_disponibles()} GB")
linea.registrar_consumo(5.0)  # Supera los 10 GB y salta la advertencia