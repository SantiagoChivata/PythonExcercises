"""
Programa que solicite al usuario los datos para calcular el área de un Triángulo (▲), 
finalmente mostrar el resultado en pantalla.

► Fórmula: Área del Triángulo
Area = (Base*Altura)/2
"""
base = int(input('Escriba cuanto mide la base del triangulo: '))
altura = int(input('Escriba cuanto mide la altura del triangulo: '))
area = (base * altura) / 2
print(f'El area para un triangulo con una base que mide {base} y una altura que mide {altura} es de: {area}')
