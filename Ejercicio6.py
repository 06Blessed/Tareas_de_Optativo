# Ejercicio 6 - Caja registradora de una cuenta corriente

class CuentaCorriente:

  def __init__(self, cliente):
    self.cliente = cliente
    self.saldo = 0

  def acreditar_saldo(self, monto):
    if monto > 0:
      self.saldo += monto
      print(
          f"[{self.cliente}] Se acreditaron Gs. {monto:,}. Saldo actual: Gs."
          f" {self.saldo:,}"
      )
    else:
      print("El monto a acreditar debe ser mayor a cero.")

  def registrar_consumo(self, monto):
    # Nos aseguramos de que no gaste más de lo que tiene en la cuenta
    if monto <= self.saldo:
      self.saldo -= monto
      print(
          f"[{self.cliente}] Consumo exitoso por Gs. {monto:,}. Saldo restante:"
          f" Gs. {self.saldo:,}"
      )
    else:
      print(
          f"[{self.cliente}] ❌ Compra rechazada: Fondos insuficientes."
          f" Intentaste gastar Gs. {monto:,} pero tu saldo es Gs."
          f" {self.saldo:,}"
      )


# Simulación requerida
cuenta = CuentaCorriente("Ana Gómez")
cuenta.acreditar_saldo(100000)
cuenta.registrar_consumo(40000)
cuenta.registrar_consumo(
    80000
)  # Esta compra se rechaza por falta de fondos (pide más de lo que hay)