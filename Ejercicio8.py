# Ejercicio 8 - Reproductor de lista de canciones

class Cancion:

  def __init__(self, titulo, artista, duracion_minutos):
    self.titulo = titulo
    self.artista = artista
    self.duracion = duracion_minutos

  def __str__(self):
    return f"'{self.titulo}' - {self.artista} ({self.duracion} min)"


class ListaReproduccion:

  def __init__(self, nombre):
    self.nombre = nombre
    self.canciones = []  # Colección interna para guardar objetos Cancion

  def agregar_cancion(self, cancion):
    self.canciones.append(cancion)

  def duracion_total(self):
    # Recorremos la colección sumando la duración de cada tema
    total = sum(c.duracion for c in self.canciones)
    return total

  def mostrar_lista(self):
    print(f"\n🎵 Playlist: {self.nombre}")
    for c in self.canciones:
      print(f" - {c}")
    print(f"⏱️ Duración total: {self.duracion_total()} minutos.")


# Probando combinación de clases
c1 = Cancion("Bohemian Rhapsody", "Queen", 6)
c2 = Cancion("Hotel California", "Eagles", 7)
mi_lista = ListaReproduccion("Rock Clásico")
mi_lista.agregar_cancion(c1)
mi_lista.agregar_cancion(c2)
mi_lista.mostrar_lista()