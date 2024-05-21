"""
Programa que solicite al usuario los datos para llevar Grados Fahrenheit a Grados Celcius.

► Fórmula: Grados Fahrenheit a Grados Celcius
celcius = (fahrenheit - 32.0) * 5.0 / 9.0
"""
fahrenheit = float(input('Escriba los grados Farenheit a convertir: '))
celcius = (fahrenheit - 32.0) * 5.0 / 9.0

print(f'{fahrenheit} grados farenheit son {celcius} grados Celsius')