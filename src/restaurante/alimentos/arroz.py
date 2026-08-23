"""Ingrediente arroz."""

# El punto = "esta misma carpeta". Traé la clase Ingrediente desde ingrediente.py
# para que Arroz pueda heredar de ella. No hace falta el camino completo restaurante.alimentos.
from .ingrediente import Ingrediente


class Arroz(Ingrediente):
    """Representa arroz dentro de una preparación."""

    def __init__(self) -> None:
        super().__init__("arroz")
