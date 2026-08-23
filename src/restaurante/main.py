"""Punto de entrada para ejecutar el ejemplo de restaurante."""

# Paquete restaurante, carpeta alimentos: traé las clases Arroz y Pollo a ESTE archivo.
# Después escribís Arroz(), no restaurante.alimentos.Arroz().
from restaurante.alimentos import Arroz, Pollo
# Misma idea: carpeta roles. Traé Camarero, Cocinero y Comensal.
from restaurante.roles import Camarero, Cocinero, Comensal
# Carpeta utensilios: traé Bandeja y Olla. Quien programa alimentos no abre estos archivos.
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


# Este bloque se ejecuta al correr el módulo, pero no al importarlo desde un test.
if __name__ == "__main__":
    main()
