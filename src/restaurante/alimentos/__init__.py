"""Ingredientes y preparaciones del restaurante."""

# El punto = "esta misma carpeta" (alimentos/). Traé Arroz desde arroz.py.
# Así el resto puede hacer: from restaurante.alimentos import Arroz (sin abrir arroz.py).
from .arroz import Arroz
from .ingrediente import Ingrediente
from .plato import Plato
from .pollo import Pollo

# `__all__` documenta qué nombres del paquete forman parte de su API pública.
__all__ = ["Arroz", "Ingrediente", "Plato", "Pollo"]
