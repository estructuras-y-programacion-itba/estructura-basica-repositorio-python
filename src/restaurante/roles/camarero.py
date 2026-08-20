"""Rol responsable de servir platos."""

from restaurante.roles.comensal import Comensal
from restaurante.utensilios import Bandeja


class Camarero:
    """Traslada un plato desde una bandeja hasta un comensal."""

    def servir(self, bandeja: Bandeja, comensal: Comensal) -> None:
        """Entrega al comensal el plato disponible en la bandeja."""
        comensal.recibir(bandeja.retirar())
