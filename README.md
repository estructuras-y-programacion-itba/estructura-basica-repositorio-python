# Estructura base para proyectos de POO con Python

Este repositorio es una referencia para organizar el primer proyecto grande de Programación Orientada a Objetos. **No es una solución de trabajo práctico**: el dominio de restaurante existe solo para mostrar cómo separar módulos, escribir pruebas y ejecutar un proyecto con `uv`.

En este documento:

- [Motivación](#motivación)
- [Instalar `uv`](#instalar-uv)
- [Pista A — correr este ejemplo](#pista-a--correr-este-ejemplo)
- [Pista B — armar tu propio proyecto](#pista-b--armar-tu-propio-proyecto-con-uv)
- [Dependencias durante el curso](#dependencias-durante-el-curso)
- [Checklist inicial](#checklist-inicial)

## Motivación

En Python ya usaste módulos sin llamarlos así. Cuando escribís:

```python
from random import random
from math import pi

# random() es una función: la llamás y te da un float entre 0 y 1.
probabilidad = random()

# pi es una constante: un número ya calculado. No lleva paréntesis.
circunferencia = 2 * pi * 3
```

estás pidiendo a Python que busque un archivo (o un paquete) con un nombre — `random`, `math` — y te preste algo que está definido ahí: la función `random` o la constante `pi`. El resto del programa no necesita saber cómo está implementado `math`; solo lo importa y lo usa.

Un **módulo** es, en la práctica, un archivo `.py` que agrupa código relacionado. Un **paquete** es una carpeta con varios módulos (y un `__init__.py`) que se importan con el punto, como `restaurante.alimentos` o `restaurante.roles`. Es el mismo mecanismo que `math`, pero aplicado al dominio de *tu* proyecto: en vez de un solo archivo gigante, el código vive en piezas con un nombre y una responsabilidad.

Eso importa especialmente en un TP **grupal**. Van a trabajar sobre **el mismo repositorio, al mismo tiempo**, sin partir el trabajo en líneas paralelas de Git. Si todo el grupo edita el mismo `main.py`, se pisan los cambios: dos personas no pueden escribir cómodas en el mismo archivo. Separar el código en paquetes baja esas colisiones; **no reemplaza a Git**. Siguen haciendo falta commits y `push` sobre ese repo compartido.

Con esta arquitectura cada integrante puede **llevar un paquete** — por ejemplo alguien lleva `src/mi_proyecto/roles/`, otra persona lleva `src/mi_proyecto/utensilios/`, etc. — e importar el trabajo del resto, como si importaran `pi`. Acuerden las interfaces (qué clases y funciones se ven desde afuera) y dejen el detalle adentro del módulo. El `main` del proyecto solo junta esas piezas y las pone a correr.

Las pruebas en `tests/` siguen la misma idea: quien arma un módulo puede verificarlo sin esperar a que el resto termine el programa entero.

---

En este documento hay dos pistas. Elegí la que corresponde a lo que estés haciendo ahora:

- **Pista A:** ya clonaste *este* repositorio y querés correr el ejemplo.
- **Pista B:** ya tenés el repositorio de *tu* TP (una carpeta casi vacía) y querés armar la misma estructura de carpetas.

En ambos casos, primero instalá `uv`.

[`uv`](https://docs.astral.sh/uv/) es un programa de consola que arma el entorno del proyecto. Usa el Python que ya tenés en la máquina (este ejemplo pide 3.12 o posterior), baja las bibliotecas que el proyecto necesita y las deja en una carpeta `.venv` propia de este repo. Así todo el grupo corre los mismos comandos (`uv sync`, `uv run …`) y no depende de cómo cada uno tenga Python instalado en la máquina.

## Instalar `uv`

Hacé esto **antes** de cualquier otro comando de este README.

**Mac** (si ya tenés [Homebrew](https://brew.sh/)):

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

Si usás Linux, instalá `uv` con el [script oficial de Astral](https://docs.astral.sh/uv/getting-started/installation/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`), no con Homebrew.

## Pista A — Correr este ejemplo

Estás en la carpeta de este repositorio, que **ya tiene** el código del restaurante (esto significa, ya clonaste este repositorio).

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
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── roles/
│   └── utensilios/
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

Cada carpeta de paquete (`alimentos`, `roles`, `utensilios`) también lleva su `__init__.py`.

- `src/restaurante/` es el programa. Cada carpeta adentro (`alimentos`, `roles`, `utensilios`) junta clases que tienen que ver entre sí, para que no esté todo en un solo archivo.
- `tests/` es donde van las pruebas. No se mezclan con el código que corre el ejemplo: así podés probar una parte sin tener el programa entero armado. Si te ayuda a orientarte, podés repetir acá las mismas carpetas que en `src/`.
- `docs/diagrama_restaurante.drawio` es un dibujo de cómo se relacionan las clases del ejemplo. Se abre en el navegador con [draw.io](https://app.diagrams.net/).
- `pyproject.toml` es la ficha del proyecto: qué versión de Python hace falta, qué bibliotecas se usan y cómo se llama el paquete. `uv` lo lee cuando corrés `uv sync`.
- `uv.lock` anota las versiones exactas que `uv` instaló. Si está en el repo, todas las máquinas instalan lo mismo. Este archivo **sí** se sube al repositorio.

Los archivos `__init__.py` marcan qué carpetas son paquetes de Python y permiten importar así:

```python
from restaurante.alimentos import Arroz, Pollo
from restaurante.roles import Camarero, Cocinero
```

### Qué muestra el ejemplo del Restaurante

El flujo es deliberadamente pequeño:

1. Se agregan ingredientes a una `Olla`.
2. Un `Cocinero` prepara un `Plato` a partir de esa olla.
3. Un `Camarero` retira el plato de una `Bandeja` y se lo entrega a un `Comensal`.

El ejemplo no prescribe las clases, carpetas ni decisiones de diseño de un trabajo práctico. En cada proyecto, el dominio debe guiar la organización y las responsabilidades.

## Pista B — Armar tu propio proyecto con uv

Estás **adentro** de la carpeta que clonaste para tu TP. No hace falta crear otra carpeta con `uv`.

`mi-proyecto` es un **nombre de ejemplo**. Reemplazalo por un nombre que describa el dominio de *tu* trabajo (no uses `restaurante` salvo que ese sea el problema).

### Estado 1 — carpeta clonada, antes de `uv init`

Así se ve el repositorio vacío del TP: documentación de referencia, licencia y README. Todavía no hay `src/`, `pyproject.toml` ni `tests/`.

```text
.
├── docs/
│   └── diagrama_de_clases.drawio
├── LICENSE
└── README.md
```

Para inicializar la estructura modular, ejecutá este comando:

```bash
uv init --package --name mi-proyecto
```

> Nota: `--name` pone el nombre del proyecto en `pyproject.toml`, sin crear un directorio nuevo.

### Estado 2 — después de `uv init`

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

El nombre del proyecto en `pyproject.toml` puede tener guiones, como `mi-proyecto`. La carpeta bajo `src/` tiene que ser un nombre válido en Python, como `mi_proyecto`. Si esos dos nombres no coinciden (por ejemplo, el proyecto se llama como el repo y el paquete se llama como el dominio), decíselo a `uv` como en este repositorio:

```toml
[tool.uv.build-backend]
module-name = "restaurante"
```

Agregá `pytest` como dependencia de desarrollo:

```bash
uv add --dev pytest
```

### Estado 3 — después de `uv add --dev pytest`

Aparecen `uv.lock` y, en tu máquina, un `.venv`. El `.venv` **no** se sube al repositorio (suele estar en `.gitignore`). El `uv.lock` **sí** se sube.

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

### Estado 4 — después de `mkdir tests`

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

[`pytest`](https://docs.pytest.org/) es una dependencia de desarrollo: se usa para verificar el proyecto, pero no forma parte de su ejecución normal.

Cuando la materia lo requiera, agregá las bibliotecas de análisis y visualización al proyecto ([NumPy](https://numpy.org/), [Matplotlib](https://matplotlib.org/)) con:

```bash
uv add numpy matplotlib
```

Ese comando actualiza `pyproject.toml` y `uv.lock`. No agregues dependencias por adelantado: cada biblioteca debe tener un uso concreto en el proyecto.

## Checklist inicial

- [ ] El código que corre el programa está en `src/<nombre_del_paquete>/`, no suelto en la raíz.
- [ ] Las pruebas están en `tests/` y se corren con `uv run pytest`.
- [ ] Las bibliotecas que usás están anotadas en `pyproject.toml`.
- [ ] `uv.lock` está en el repositorio (sí se subió).
- [ ] Las clases y carpetas son del dominio de *tu* TP: no copies `restaurante` ni sus nombres.
