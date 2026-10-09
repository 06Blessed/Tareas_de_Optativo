# Ejercicio 9 - Turnos de un consultorio

class Turno:

  def __init__(self, paciente, hora):
    self.paciente = paciente
    self.hora = hora
    self.estado = "Pendiente"  # Estado inicial

  def marcar_atendido(self):
    self.estado = "Atendido"

  def __str__(self):
    return f"Paciente: {self.paciente} | Hora: {self.hora} | Estado: {self.estado}"


class AgendaConsultorio:

  def __init__(self):
    self.turnos = []

  def agendar(self, turno):
    self.turnos.append(turno)

  def listar_pendientes(self):
    print("\n📋 Turnos pendientes:")
    for t in self.turnos:
      if t.estado == "Pendiente":
        print(f" - {t}")


agenda = AgendaConsultorio()
t1 = Turno("Roberto Carlos", "08:30")
t2 = Turno("Lucía Giménez", "09:00")
agenda.agendar(t1)
agenda.agendar(t2)

t1.marcar_atendido()  # Atendemos al primero
agenda.listar_pendientes()  # Solo debe mostrar el de Lucía