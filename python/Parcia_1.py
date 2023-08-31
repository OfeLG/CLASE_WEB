import math

# Función para calcular la distancia entre dos puntos en el plano cartesiano
def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Decorador que implementa el algoritmo "Divide y Vencerás" para encontrar los pares más cercanos
def pares_cercanos_decorator(func):
    def wrapper(*args, **kwargs):
        puntos = args[0]

        # Ordenar los puntos por coordenada x e y respectivamente
        puntos_ordenados_x = sorted(puntos, key=lambda p: p[0])
        puntos_ordenados_y = sorted(puntos, key=lambda p: p[1])

        # Función interna para encontrar los pares más cercanos recursivamente
        def encontrar_pares_cercanos(puntos_x, puntos_y):
            n = len(puntos_x)

            # Caso base: si hay pocos puntos, calcular todas las distancias y encontrar el mínimo
            if n <= 3:
                return min((distancia(puntos_x[i], puntos_x[j]), puntos_x[i], puntos_x[j])
                           for i in range(n) for j in range(i + 1, n))

            # Dividir los puntos en dos mitades según la coordenada x del punto medio
            mitad = n // 2
            punto_medio = puntos_x[mitad]

            izquierda_x = puntos_x[:mitad]
            derecha_x = puntos_x[mitad:]

            # Filtrar los puntos para obtener las mitades correspondientes en la coordenada y
            izquierda_y = [p for p in puntos_y if p[0] <= punto_medio[0]]
            derecha_y = [p for p in puntos_y if p[0] > punto_medio[0]]

            # Recursivamente encontrar los pares más cercanos en ambas mitades
            distancia_izq = encontrar_pares_cercanos(izquierda_x, izquierda_y)
            distancia_der = encontrar_pares_cercanos(derecha_x, derecha_y)

            # Encontrar la distancia mínima entre las dos mitades
            min_dist, p1, p2 = min(distancia_izq, distancia_der, key=lambda x: x[0])

            # Filtrar los puntos que están cerca de la línea vertical central
            cerca_y = [p for p in puntos_y if abs(punto_medio[0] - p[0]) < min_dist]

            # Comprobar las distancias entre los puntos cercanos en la coordenada y
            for i in range(len(cerca_y)):
                for j in range(i + 1, min(i + 7, len(cerca_y))):
                    dist = distancia(cerca_y[i], cerca_y[j])
                    if dist < min_dist:
                        min_dist = dist
                        p1, p2 = cerca_y[i], cerca_y[j]

            return min_dist, p1, p2

        puntos_x = puntos_ordenados_x
        puntos_y = puntos_ordenados_y

        # Iniciar la búsqueda recursiva
        return encontrar_pares_cercanos(puntos_x, puntos_y)

    return wrapper

# Aplicar el decorador a la función de búsqueda de pares más cercanos
@pares_cercanos_decorator
def encontrar_pares_cercanos(puntos):
    return puntos

# USO:
puntos = [(1, 2), (3, 7), (8, 4), (10, 12), (2, 9)]
distancia_min, punto1, punto2 = encontrar_pares_cercanos(puntos)
print("Punto 1:", punto1)
print("Punto 2:", punto2)
print("Distancia mínima:", distancia_min)
