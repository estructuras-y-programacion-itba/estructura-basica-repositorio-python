# Estructura base para proyectos de POO con Python

Este repositorio es una referencia para organizar el primer proyecto grande de Programación Orientada a Objetos. No es una solución de trabajo práctico: el dominio de restaurante existe solo para mostrar cómo separar módulos, escribir pruebas y ejecutar un proyecto con `uv`.

## Primer uso

Instalá las dependencias y el paquete local:

```bash
uv sync
```

Ejecutá el ejemplo:

```bash
uv run python -m restaurante.main
```

Ejecutá las pruebas:

```bash
uv run pytest
```

No es necesario activar manualmente un entorno virtual: `uv` crea y administra `.venv` por proyecto.

## Estructura

```text
.
├── docs/
│   └── diagrama_restaurante.drawio
├── src/
│   └── restaurante/
│       ├── alimentos/
│       ├── roles/
│       ├── utensilios/
│       └── main.py
├── tests/
│   ├── roles/
│   └── utensilios/
├── pyproject.toml
└── uv.lock
```

- `src/restaurante/` contiene el código de la aplicación. Cada subpaquete agrupa clases que colaboran dentro de una misma parte del dominio.
- `tests/` contiene las pruebas automatizadas y replica, cuando resulta útil, la organización de `src/`. Las pruebas no se ubican junto al código de producción.
- `docs/diagrama_restaurante.drawio` muestra las relaciones del ejemplo. Se abre con diagrams.net / draw.io.
- `pyproject.toml` define la versión de Python, las dependencias y cómo se instala el paquete.
- `uv.lock` fija las versiones resueltas. Se versiona junto con el código.

Los archivos `__init__.py` señalan qué carpetas son paquetes de Python y permiten exponer una interfaz pública cómoda, por ejemplo:

```python
from restaurante.alimentos import Arroz, Pollo
from restaurante.roles import Camarero, Cocinero
```

## Qué muestra el ejemplo

El flujo es deliberadamente pequeño:

1. Se agregan ingredientes a una `Olla`.
2. Un `Cocinero` prepara un `Plato` a partir de esa olla.
3. Un `Camarero` retira el plato de una `Bandeja` y se lo entrega a un `Comensal`.

El código muestra herencia mínima (`Arroz` y `Pollo` son ingredientes), composición (`Olla` y `Plato` contienen ingredientes), encapsulamiento y una operación inválida que se informa con `ValueError`.

El ejemplo no prescribe las clases, carpetas ni decisiones de diseño de un trabajo práctico. En cada proyecto, el dominio debe guiar la organización y las responsabilidades.

## Cómo recrear esta estructura en tu proyecto

Creá el proyecto y elegí un nombre que describa su dominio:

```bash
uv init --package mi-proyecto
cd mi-proyecto
uv add --dev pytest
```

Luego, de forma manual:

1. Renombrá el paquete creado dentro de `src/` si el dominio lo requiere.
2. Creá subpaquetes para agrupar responsabilidades relacionadas; cada uno necesita un `__init__.py`.
3. Creá `tests/` desde el inicio y escribí una prueba por cada comportamiento importante.
4. Ejecutá `uv run pytest` antes de compartir cambios.

El nombre del proyecto puede contener guiones, como `mi-proyecto`, pero el nombre que se importa desde Python debe ser un identificador válido, como `mi_proyecto`. Si ambos nombres difieren, configurá el módulo del backend de build como se muestra en este repositorio.

## Dependencias durante el curso

`pytest` es una dependencia de desarrollo: se usa para verificar el proyecto, pero no forma parte de su ejecución normal.

Cuando la materia lo requiera, agregá las bibliotecas de análisis y visualización al proyecto con:

```bash
uv add numpy matplotlib
```

Ese comando actualiza `pyproject.toml` y `uv.lock`. No agregues dependencias por adelantado: cada biblioteca debe tener un uso concreto en el proyecto.

## Checklist inicial

- [ ] El código de producción está dentro de `src/<nombre_del_paquete>/`.
- [ ] Las pruebas están en `tests/` y se ejecutan con `uv run pytest`.
- [ ] Las dependencias están declaradas en `pyproject.toml`.
- [ ] `uv.lock` está versionado.
- [ ] Las clases y módulos reflejan el dominio del problema, no el ejemplo de este repositorio.
