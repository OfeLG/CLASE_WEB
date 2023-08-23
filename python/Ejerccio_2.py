"""
Un palindromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda.
Ejemplo Ojo, Oso, Ana, Anna, Otto...
Su misión es, realizar un algoritmo que me permita conocer dada una palabra por el usuario si es palíndromo 
o no.

"""

#SOLUCIÓN
palabra = input("Ingrese una palabra: ")
palabra = palabra.lower().replace(" ", "")  # Se convierte a minúsculas y se eliminan los espacios por si las moscas
if  palabra == palabra[::-1]: # Se verifica si la palabra se lee igual de izquierda a derecha que de derecha a izquierda
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")


