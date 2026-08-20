"""Tipos base para los ingredientes."""


class Ingrediente:
    """Representa un ingrediente identificado por su nombre."""

    def __init__(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del ingrediente."""
        return self._nombre
