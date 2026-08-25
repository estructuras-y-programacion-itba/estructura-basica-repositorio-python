"""Preparaciones que pueden servirse en el restaurante."""

# El punto = "esta misma carpeta". Un Plato está hecho de Ingrediente; los importás de acá al lado.
from .ingrediente import Ingrediente


class Plato:
    """Agrupa los ingredientes de una preparación terminada."""

    def __init__(self, nombre: str, ingredientes: tuple[Ingrediente, ...]) -> None:
        self._nombre = nombre
        self._ingredientes = ingredientes

    @property
    def nombre(self) -> str:
        """Devuelve el nombre de la preparación."""
        return self._nombre

    @property
    def ingredientes(self) -> tuple[Ingrediente, ...]:
        """Devuelve los ingredientes sin exponer una colección mutable."""
        return self._ingredientes
