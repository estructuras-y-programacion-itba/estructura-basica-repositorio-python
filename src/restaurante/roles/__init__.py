"""Personas que colaboran en el servicio del restaurante."""

# El punto = "esta misma carpeta" (roles/). Reexportá las clases para que
# el resto importe from restaurante.roles import Camarero (sin abrir camarero.py).
from .camarero import Camarero
from .cocinero import Cocinero
from .comensal import Comensal

# `__all__` documenta qué nombres del paquete forman parte de su API pública.
__all__ = ["Camarero", "Cocinero", "Comensal"]
