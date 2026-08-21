"""Tipos base para los ingredientes."""


class Ingrediente:
    """Representa un ingrediente identificado por su nombre."""

    def __init__(self, nombre: str) -> None:
        # El prefijo `_` marca estado interno: se consulta mediante la propiedad.
        self._nombre = nombre

    @property
    def nombre(self) -> str:
        # `@property` permite usar `ingrediente.nombre` sin paréntesis y sin romper el encapsulamiento.
        """Devuelve el nombre del ingrediente."""
        return self._nombre
