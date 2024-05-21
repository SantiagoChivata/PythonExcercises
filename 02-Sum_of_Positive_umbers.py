"""
Escribir un programa que lea un entero positivo, introducido por el usuario y después muestre en pantalla 
la suma de todos los enteros desde 1.
La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
suma= n(n+1)/2
"""

numeroEntero = int(input('Escriba un numero entero positivo: '))
suma = numeroEntero * (numeroEntero + 1) /2
print(f'La suma desde el 1 hasta el {numeroEntero} es: {suma}')