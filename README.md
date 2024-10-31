# TrabajoFinalMatematicas

1. Importación de la Librería math

import math
La librería math se utiliza para las operaciones matemáticas, especialmente para convertir los ángulos de grados a radianes y para calcular el coseno y el seno, necesarios para mover el vehículo en la dirección deseada.

2. Definición de la Clase Vehiculo

class Vehiculo:
Aquí se define la clase Vehiculo, que contiene los métodos para mover el vehículo y verificar si ha ocurrido una colisión.

Método __init__

def __init__(self, velocidad):
    self.posicion = [0, 0]  #Posición inicial en el plano 2D
    self.velocidad = velocidad  #Velocidad constante para simplificar
El método __init__ es el constructor de la clase. Inicializa:

posicion: La posición inicial del vehículo en el plano 2D, definida en [0, 0] (origen).
velocidad: La velocidad constante del vehículo, que se pasa como parámetro cuando se crea el objeto Vehiculo.

Método mover

def mover(self, direccion, tiempo):
    angulo = math.radians(direccion)  #Convierte la dirección a radianes
    self.posicion[0] += self.velocidad * math.cos(angulo) * tiempo
    self.posicion[1] += self.velocidad * math.sin(angulo) * tiempo
El método mover calcula la nueva posición del vehículo en el plano en función de la dirección y el tiempo:

angulo: Convierte el ángulo direccion (en grados) a radianes para poder usar las funciones trigonométricas.
self.posicion[0] y self.posicion[1]: Actualizan las coordenadas x e y respectivamente. El movimiento se calcula multiplicando la velocidad por el tiempo y por el coseno (para el eje x) o seno (para el eje y) del ángulo de dirección.

Método verificar_colision

def verificar_colision(self, limite_pista):
    if abs(self.posicion[0]) >= limite_pista[0] or abs(self.posicion[1]) >= limite_pista[1]:
        return "Colisión con el borde de la pista"
    return "Sin colisión"
Este método verifica si el vehículo ha alcanzado o sobrepasado los límites de la pista (limite_pista):

Condición de Colisión: Si la posición en x o y es mayor o igual al límite de la pista en esa dirección, entonces se detecta una colisión.

Devuelve: Un mensaje de colisión si se cumple la condición; de lo contrario, devuelve "Sin colisión".

3. Parámetros de Simulación

velocidad_vehiculo = 10  #Velocidad constante del vehículo
tiempo = 1  # Tiempo en segundos para cada movimiento
limite_pista = [50, 50]  #Límites de la pista en X e Y
Aquí se definen los parámetros iniciales:

velocidad_vehiculo: La velocidad del vehículo.
tiempo: Intervalo de tiempo de cada movimiento.
limite_pista: Límites en los ejes x e y, más allá de los cuales el vehículo colisiona.

4. Crear Instancia y Movimiento del Vehículo

vehiculo = Vehiculo(velocidad_vehiculo)
Se crea una instancia de la clase Vehiculo, que llamaremos vehiculo, pasando velocidad_vehiculo como parámetro.

5. Bucle para Mover el Vehículo hasta Colisionar

direccion = 0  #Ángulo de 0 grados (hacia la derecha en el eje X)
while True:
    vehiculo.mover(direccion, tiempo)
    print(f"Posición actual del vehículo: {vehiculo.posicion}")
    colision = vehiculo.verificar_colision(limite_pista)
    print(f"Estado de colisión: {colision}")
    if colision != "Sin colisión":
        break  #Detiene el movimiento cuando ocurre una colisión

Dirección: Se define en 0 grados, lo cual indica que el vehículo se moverá en una línea recta hacia la derecha (en el eje x positivo).
Bucle while True:
Movimiento del Vehículo: Llama al método mover, que actualiza la posición del vehículo.
Impresión de la Posición: Muestra la posición actual del vehículo después de cada movimiento.
Verificación de Colisión: Llama a verificar_colision, que revisa si el vehículo ha sobrepasado los límites de la pista.
Condición de Salida: Si se detecta una colisión, se imprime el mensaje y el bucle se detiene con break.
