"""Rol responsable de preparar platos."""

# De alimentos, traé Plato (el resultado de cocinar).
from restaurante.alimentos import Plato
# De utensilios, traé Olla (de dónde salen los ingredientes). El cocinero no define la olla.
from restaurante.utensilios import Olla


class Cocinero:
    """Prepara platos a partir de los ingredientes de una olla."""

    def preparar(self, nombre_plato: str, olla: Olla) -> Plato:
        """Crea un plato y deja la olla vacía."""
        return Plato(nombre_plato, olla.retirar_ingredientes())
