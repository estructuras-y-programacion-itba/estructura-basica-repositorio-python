"""Ingredientes y preparaciones del restaurante."""

# El punto significa "buscar dentro de este mismo paquete".
from .arroz import Arroz
from .ingrediente import Ingrediente
from .plato import Plato
from .pollo import Pollo

# `__all__` documenta qué nombres del paquete forman parte de su API pública.
__all__ = ["Arroz", "Ingrediente", "Plato", "Pollo"]
