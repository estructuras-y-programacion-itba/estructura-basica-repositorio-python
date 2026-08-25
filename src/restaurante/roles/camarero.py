"""Rol responsable de servir platos."""

# Comensal vive en otro archivo de este mismo paquete roles. Traé la clase a este archivo.
from restaurante.roles.comensal import Comensal
# Otra carpeta: utensilios. Traé Bandeja. El camarero usa la bandeja; no la implementa.
from restaurante.utensilios import Bandeja


class Camarero:
    """Traslada un plato desde una bandeja hasta un comensal."""

    def servir(self, bandeja: Bandeja, comensal: Comensal) -> None:
        """Entrega al comensal el plato disponible en la bandeja."""
        comensal.recibir(bandeja.retirar())
