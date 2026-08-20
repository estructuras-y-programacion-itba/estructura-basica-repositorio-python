"""Rol responsable de preparar platos."""

from restaurante.alimentos import Plato
from restaurante.utensilios import Olla


class Cocinero:
    """Prepara platos a partir de los ingredientes de una olla."""

    def preparar(self, nombre_plato: str, olla: Olla) -> Plato:
        """Crea un plato y deja la olla vacía."""
        return Plato(nombre_plato, olla.retirar_ingredientes())
