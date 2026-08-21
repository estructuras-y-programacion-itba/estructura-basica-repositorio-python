from restaurante.alimentos import Arroz, Pollo
from restaurante.roles import Camarero, Cocinero, Comensal
from restaurante.utensilios import Bandeja, Olla


def test_el_camarero_sirve_el_plato_preparado_al_comensal() -> None:
    # Pytest descubre automáticamente funciones cuyo nombre empieza con `test_`.
    olla = Olla()
    olla.agregar(Arroz())
    olla.agregar(Pollo())

    plato = Cocinero().preparar("arroz con pollo", olla)
    bandeja = Bandeja()
    bandeja.colocar(plato)
    comensal = Comensal("Ana")

    Camarero().servir(bandeja, comensal)

    # `is` verifica que se trata exactamente del mismo objeto.
    assert comensal.plato_servido is plato
    assert [ingrediente.nombre for ingrediente in plato.ingredientes] == ["arroz", "pollo"]
    assert bandeja.plato is None
