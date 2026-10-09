
# Ejercicio 3 - Empleado y su sueldo
class Empleado:

  def __init__(self, nombre, cargo, salario_mensual):
    self.nombre = nombre
    self.cargo = cargo
    self.salario_mensual = salario_mensual

  def calcular_salario_anual(self):
    # En Paraguay se paga el aguinaldo (un sueldo más al año), así que sumamos 13 meses en total
    return self.salario_mensual * 13

  def __str__(self):
    anual = self.calcular_salario_anual()
    return f"Empleado: {self.nombre} | Cargo: {self.cargo} | Salario Mensual: Gs. {self.salario_mensual:,} | Anual (con aguinaldo): Gs. {anual:,}"


emp1 = Empleado("Juan Pérez", "Contador", 4500000)
print(emp1)