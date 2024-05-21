"""
Programa que solicite al usuario los datos para calcular el área de un Cuadrado (■), 
finalmente mostrar el resultado en pantalla.

► Fórmula: Área del cuadrado:
    Area = Lado ** 2
"""
lado = int(input('Escriba cuanto mide el cuadrado en centimetros: '))
area = lado **2
print(f'El area para un cuadrado que el lado mide {lado} cm es de: {area} centimetros al cuadrado')
