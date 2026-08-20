"""Ingrediente arroz."""

from .ingrediente import Ingrediente


class Arroz(Ingrediente):
    """Representa arroz dentro de una preparación."""

    def __init__(self) -> None:
        super().__init__("arroz")
