"""Bandeja usada para trasladar un plato al comensal."""

from restaurante.alimentos import Plato


class Bandeja:
    """Contiene como máximo un plato listo para servir."""

    def __init__(self) -> None:
        # `Plato | None` significa: hay un plato o todavía no hay ninguno.
        self._plato: Plato | None = None

    @property
    def plato(self) -> Plato | None:
        """Devuelve el plato que está en la bandeja, si existe."""
        return self._plato

    def colocar(self, plato: Plato) -> None:
        """Coloca un plato en la bandeja."""
        self._plato = plato

    def retirar(self) -> Plato:
        """Retira y devuelve el plato de la bandeja.

        Raises:
            ValueError: Si no hay un plato para servir.
        """
        if self._plato is None:
            raise ValueError("No hay un plato en la bandeja.")

        plato = self._plato
        self._plato = None
        return plato
