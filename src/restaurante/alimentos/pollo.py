"""Ingrediente pollo."""

from .ingrediente import Ingrediente


class Pollo(Ingrediente):
    """Representa pollo dentro de una preparación."""

    def __init__(self) -> None:
        super().__init__("pollo")
