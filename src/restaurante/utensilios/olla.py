"""Olla para reunir ingredientes antes de cocinar."""

from restaurante.alimentos import Ingrediente


class Olla:
    """Mantiene los ingredientes que todavía no fueron preparados."""

    def __init__(self) -> None:
        # La lista se mantiene privada para controlar cómo cambia el estado.
        self._ingredientes: list[Ingrediente] = []

    @property
    def ingredientes(self) -> tuple[Ingrediente, ...]:
        """Devuelve los ingredientes actuales sin exponer la lista interna."""
        # La tupla es una copia no modificable de la lista interna.
        return tuple(self._ingredientes)

    def agregar(self, ingrediente: Ingrediente) -> None:
        """Agrega un ingrediente a la olla."""
        self._ingredientes.append(ingrediente)

    def retirar_ingredientes(self) -> tuple[Ingrediente, ...]:
        """Entrega todos los ingredientes para preparar un plato.

        Raises:
            ValueError: Si la olla no contiene ingredientes.
        """
        if not self._ingredientes:
            raise ValueError("No se puede preparar un plato con una olla vacía.")

        # Primero tomamos una instantánea y después dejamos la olla lista para reutilizar.
        ingredientes = tuple(self._ingredientes)
        self._ingredientes.clear()
        return ingredientes
