import pytest

from restaurante.alimentos import Arroz, Pollo
from restaurante.utensilios import Olla


def test_retirar_ingredientes_entrega_el_contenido_y_vacia_la_olla() -> None:
    olla = Olla()
    arroz = Arroz()
    pollo = Pollo()
    olla.agregar(arroz)
    olla.agregar(pollo)

    assert olla.retirar_ingredientes() == (arroz, pollo)
    assert olla.ingredientes == ()


def test_retirar_ingredientes_de_una_olla_vacia_lanza_un_error() -> None:
    with pytest.raises(ValueError, match="olla vacía"):
        Olla().retirar_ingredientes()
