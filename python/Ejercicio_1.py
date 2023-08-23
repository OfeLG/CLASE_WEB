"""
En una playa de estacionamiento cobran $. 2.00 por hora fracción los días Lunes, Martes y Miércoles, 
$. 2.50 los días jueves y viernes, $. 3.00 los días sábado y Domingo. Se considera fracción de hora cuando 
haya pasado de 5 minutos. Diseñe un programa que determine cuánto debe pagar un cliente por su estacionamiento 
en un solo día de la semana. Si el tiempo ingresado es incorrecto imprima un mensaje de error

"""

#SOLUCIÓN
tarifas = {
    "lunes": 2.00, "martes": 2.00, "miércoles": 2.00,
    "jueves": 2.50, "viernes": 2.50, "sábado": 3.00, "domingo": 3.00
}

dia_semana = input("Ingrese el día de la semana: ").lower()
tiempo_estacionado = int(input("Ingrese el tiempo estacionado en minutos: "))

if dia_semana not in tarifas:
    print("Día inválido.")
else:
    costo_por_hora = tarifas[dia_semana]
    horas = tiempo_estacionado // 60 #El resultado se redondea hacia abajo para obtener la parte entera del cociente. 
    if tiempo_estacionado % 60 > 5: #Se verifica si el residuo de los minutos es mayor que 5.
        horas += 1
    total_pagar = costo_por_hora * horas
    print(f"El cliente debe pagar ${total_pagar:.2f}") # Se redondea el número a dos decimales después del punto.

