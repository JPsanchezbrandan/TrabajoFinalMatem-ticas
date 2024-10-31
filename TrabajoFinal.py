import math

class Vehiculo:
    def __init__(self, velocidad):
        # Inicializa la posición del vehículo y su velocidad
        self.posicion = [0, 0]  # Posición inicial en el plano 2D
        self.velocidad = velocidad  # Velocidad constante para simplificar

    def mover(self, direccion, tiempo):
        # Mueve el vehículo en una dirección específica durante un tiempo determinado
        angulo = math.radians(direccion)  # Convierte la dirección a radianes
        self.posicion[0] += self.velocidad * math.cos(angulo) * tiempo
        self.posicion[1] += self.velocidad * math.sin(angulo) * tiempo

    def verificar_colision(self, limite_pista):
        # Verifica si el vehículo colisiona con los límites de la pista
        if abs(self.posicion[0]) >= limite_pista[0] or abs(self.posicion[1]) >= limite_pista[1]:
            return "Colision con el borde de la pista"
        return "Sin colision"

# Parámetros de simulación
velocidad_vehiculo = 10  # Velocidad constante del vehículo
tiempo = 1  # Tiempo en segundos para cada movimiento
limite_pista = [50, 50]  # Límites de la pista en X e Y

# Crear instancia del vehículo
vehiculo = Vehiculo(velocidad_vehiculo)

# Movimiento del vehículo hacia el borde de la pista para causar una colisión
direccion = 0  # Ángulo de 0 grados (hacia la derecha en el eje X)
while True:
    vehiculo.mover(direccion, tiempo)
    print(f"Posicion actual del vehiculo: {vehiculo.posicion}")
    colision = vehiculo.verificar_colision(limite_pista)
    print(f"Estado de colision: {colision}")
    if colision != "Sin colision":
        break  # Detiene el movimiento cuando ocurre una colisión



    