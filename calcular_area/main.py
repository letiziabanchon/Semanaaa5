# main.py
# Programa principal que pide datos y muestra el resultado.

from clase import Figura
from lógica import calcular_area

def main():
    print("=== Cálculo de área de un círculo ===")
    id_figura = int(input("Ingresa el ID de la figura: "))  # int
    nombre = input("Ingresa el nombre de la figura: ")      # string
    radio = float(input("Ingresa el radio (m): "))          # float

    figura = Figura(id_figura, nombre, radio)
    try:
        area = calcular_area(figura)
        print(f"\nFigura: {figura.nombre} (ID: {figura.id_figura})")
        print(f"Área: {area:.2f} m²")
        print(f"Validación: {figura.validada}")  # bool
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()