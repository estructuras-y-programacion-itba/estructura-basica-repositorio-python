# Estructura base para proyectos de POO con Python

Este repositorio es una referencia para organizar el primer proyecto grande de Programación Orientada a Objetos. **No es una solución de trabajo práctico**: el dominio de restaurante existe solo para mostrar cómo separar módulos, escribir pruebas y ejecutar un proyecto con `uv`.

## Motivación

En Python ya usaste módulos sin llamarlos así. Cuando escribís:

```python
from random import random
from math import pi
```

estás pidiendo a Python que busque un archivo (o un paquete) con un nombre — `random`, `math` — y te preste algo que está definido ahí: la función `random` o la constante `pi`. El resto del programa no necesita saber cómo está implementado `math`; solo lo importa y lo usa.

Un **módulo** es, en la práctica, un archivo `.py` que agrupa código relacionado. Un **paquete** es una carpeta con varios módulos (y un `__init__.py`) que se importan con el punto, como `restaurante.alimentos` o `restaurante.roles`. Es el mismo mecanismo que `math`, pero aplicado al dominio de *tu* proyecto: en vez de un solo archivo gigante, el código vive en piezas con un nombre y una responsabilidad.

Eso importa especialmente en un TP **grupal**. Van a trabajar sobre **el mismo repositorio, al mismo tiempo**, sin partir el trabajo en líneas paralelas de Git. Si todo el grupo edita el mismo `main.py`, se pisan los cambios: dos personas no pueden escribir cómodas en el mismo archivo.

Con esta arquitectura cada integrante puede apropiarse de un paquete — por ejemplo alguien en `src/mi_proyecto/roles/`, otra persona en `src/mi_proyecto/utensilios/` — e importar el trabajo del resto como ya importan `pi`. Acuerden las interfaces (qué clases y funciones se ven desde afuera) y dejen el detalle adentro del módulo. El `main` del proyecto solo orquesta esas piezas.

Las pruebas en `tests/` siguen la misma idea: quien arma un módulo puede verificarlo sin esperar a que el resto termine el programa entero.

Hay dos pistas. Elegí la que corresponde a lo que estés haciendo ahora:

- **Pista A:** ya clonaste *este* repositorio y querés correr el ejemplo.
- **Pista B:** ya tenés el repositorio de *tu* TP (una carpeta casi vacía) y querés armar el mismo tipo de andamiaje.

En ambos casos, primero instalá `uv`. No hace falta instalar Python a mano: `uv` puede bajar un intérprete compatible. Este ejemplo pide Python 3.12 o posterior.

## Instalar `uv`

Hacé esto **antes** de cualquier otro comando de este README.

**Mac** (si ya tenés Homebrew):

```bash
brew install uv
```

**Windows** (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Si el comando `uv` no aparece, cerrá y volvé a abrir la terminal. Comprobá la instalación:

```bash
uv --version
```

Si usás Linux, instalá `uv` con el script oficial de Astral (`curl -LsSf https://astral.sh/uv/install.sh | sh`), no con Homebrew.

## Pista A — Correr este ejemplo

Estás en la carpeta de este repositorio, que **ya tiene** el código del restaurante.

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

No es necesario activar a mano un entorno virtual: `uv` crea y administra `.venv` por proyecto.

### Cómo queda este repositorio

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

### Qué muestra el ejemplo

El flujo es deliberadamente pequeño:

1. Se agregan ingredientes a una `Olla`.
2. Un `Cocinero` prepara un `Plato` a partir de esa olla.
3. Un `Camarero` retira el plato de una `Bandeja` y se lo entrega a un `Comensal`.

El código muestra herencia mínima (`Arroz` y `Pollo` son ingredientes), composición (`Olla` y `Plato` contienen ingredientes), encapsulamiento y una operación inválida que se informa con `ValueError`.

El ejemplo no prescribe las clases, carpetas ni decisiones de diseño de un trabajo práctico. En cada proyecto, el dominio debe guiar la organización y las responsabilidades.

## Pista B — Armar tu propio proyecto

Estás **adentro** de la carpeta que clonaste para tu TP. No hace falta crear otra carpeta con `uv`.

`mi-proyecto` es un **nombre de ejemplo**. Reemplazalo por un nombre que describa el dominio de *tu* trabajo (no uses `restaurante` salvo que ese sea el problema).

### 📷 Estado 1 — carpeta clonada, antes de `uv init`

Así se ve el repositorio vacío del TP (como el `modulo` que clonaste): documentación de referencia, licencia y README. Todavía no hay `src/`, `pyproject.toml` ni `tests/`.

```text
.
├── docs/
│   └── diagrama_de_clases.drawio
├── LICENSE
└── README.md
```

El comando correcto, **desde esa carpeta ya clonada**, es:

```bash
uv init --package --name mi-proyecto
```

`--name` pone el nombre del proyecto en `pyproject.toml`. No crea un directorio nuevo.

**No** uses `uv init --package mi-proyecto` (sin `--name`). Ese argumento es una *ruta*: `uv` crea una carpeta `mi-proyecto/` adentro de la que ya tenías, y el andamiaje queda anidado.

### 📷 Estado 2 — después de `uv init`

`uv` conserva lo que ya estaba (`docs/`, `README.md`, `LICENSE`) y agrega el esqueleto del paquete. El nombre con guiones (`mi-proyecto`) se convierte en un identificador válido para importar: la carpeta queda `src/mi_proyecto/`.

```text
.
├── docs/
│   └── diagrama_de_clases.drawio
├── src/
│   └── mi_proyecto/
│       └── __init__.py
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml
└── README.md
```

`uv` puede agregar un script de consola en `pyproject.toml`. Para este curso alcanza con el mismo estilo que el ejemplo: `uv run python -m mi_proyecto.main` (cuando exista `main.py`).

El nombre del proyecto puede contener guiones, como `mi-proyecto`, pero el nombre que se importa desde Python debe ser un identificador válido, como `mi_proyecto`. Si ambos nombres difieren de forma deliberada (por ejemplo, el proyecto se llama como el repo y el paquete se llama como el dominio), configurá el módulo del backend de build como se muestra en este repositorio (`[tool.uv.build-backend]` con `module-name`).

Agregá `pytest` como dependencia de desarrollo:

```bash
uv add --dev pytest
```

### 📷 Estado 3 — después de `uv add --dev pytest`

Aparecen `uv.lock` y, en tu máquina, un `.venv`. El entorno virtual **no** se sube al repositorio (suele estar en `.gitignore`). El lockfile **sí** se versiona.

```text
.
├── docs/
│   └── diagrama_de_clases.drawio
├── src/
│   └── mi_proyecto/
│       └── __init__.py
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

`uv` no crea la carpeta de pruebas. Creala vos, de forma explícita:

```bash
mkdir tests
```

### 📷 Estado 4 — después de `mkdir tests`

```text
.
├── docs/
│   └── diagrama_de_clases.drawio
├── src/
│   └── mi_proyecto/
│       └── __init__.py
├── tests/
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

A partir de acá, a mano:

1. Renombrá el paquete creado dentro de `src/` si el dominio lo requiere.
2. Creá subpaquetes para agrupar responsabilidades relacionadas; cada uno necesita un `__init__.py`.
3. Escribí una prueba por cada comportamiento importante. Cuando resulte útil, replicá en `tests/` la organización de `src/`.
4. Ejecutá `uv run pytest` antes de compartir cambios.

## Dependencias durante el curso

`pytest` es una dependencia de desarrollo: se usa para verificar el proyecto, pero no forma parte de su ejecución normal.

Cuando la materia lo requiera, agregá las bibliotecas de análisis y visualización al proyecto con:

```bash
uv add numpy matplotlib
```

Ese comando actualiza `pyproject.toml` y `uv.lock`. No agregues dependencias por adelantado: cada biblioteca debe tener un uso concreto en el proyecto.
