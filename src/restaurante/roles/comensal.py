"""Rol que recibe un plato servido."""

from restaurante.alimentos import Plato


class Comensal:
    """Representa a una persona a la que se le puede servir un plato."""

    def __init__(self, nombre: str) -> None:
        self._nombre = nombre
        self._plato_servido: Plato | None = None

    @property
    def nombre(self) -> str:
        """Devuelve el nombre del comensal."""
        return self._nombre

    @property
    def plato_servido(self) -> Plato | None:
        """Devuelve el último plato recibido, si existe."""
        return self._plato_servido

    def recibir(self, plato: Plato) -> None:
        """Registra el plato que fue servido al comensal."""
        self._plato_servido = plato
