"""
Programa que solicite al usuario los datos para calcular el área de un Círculo (●), 
finalmente mostrar el resultado en pantalla.

► Fórmula: Área del Círculo
Area = PI*(Radio**2)

"""
radio = int(input('Escriba cuanto mide radio del circulo: '))
pi = 3.1416
area = pi*(radio**2)
print(f'El area para un circulo que el radio mide {radio} es de: {area}')
