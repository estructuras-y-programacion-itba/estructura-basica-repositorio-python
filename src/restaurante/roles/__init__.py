"""Personas que colaboran en el servicio del restaurante."""

from .camarero import Camarero
from .cocinero import Cocinero
from .comensal import Comensal

# `__all__` documenta qué nombres del paquete forman parte de su API pública.
__all__ = ["Camarero", "Cocinero", "Comensal"]
