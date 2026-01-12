# logica.py
# Función que calcula el área y valida la figura.

import math
from clase import Figura

def calcular_area(figura: Figura) -> float:
    if figura.radio > 0:
        figura.validada = True  # bool cambia a True si es correcto
        return math.pi * (figura.radio ** 2)
    else:
        figura.validada = False
        raise ValueError("El radio debe ser mayor a 0.")
