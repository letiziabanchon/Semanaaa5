# clase.py
# Clase que representa una figura geométrica.

class Figura:
    def __init__(self, id_figura: int, nombre: str, radio: float):
        self.id_figura = id_figura      # int
        self.nombre = nombre            # string
        self.radio = radio              # float
        self.validada = False           # bool