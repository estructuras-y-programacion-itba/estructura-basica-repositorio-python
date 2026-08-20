"""Punto de entrada para ejecutar el ejemplo de restaurante."""

from restaurante.alimentos import Arroz, Pollo
from restaurante.roles import Camarero, Cocinero, Comensal
from restaurante.utensilios import Bandeja, Olla


def main() -> None:
    """Prepara y sirve un plato para demostrar la colaboración entre módulos."""
    olla = Olla()
    olla.agregar(Arroz())
    olla.agregar(Pollo())

    plato = Cocinero().preparar("arroz con pollo", olla)
    bandeja = Bandeja()
    bandeja.colocar(plato)

    comensal = Comensal("Ana")
    Camarero().servir(bandeja, comensal)

    print(f"{comensal.nombre} recibe {comensal.plato_servido.nombre}.")


if __name__ == "__main__":
    main()
