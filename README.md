# Script IA - Python, Gemini

## Descripción

Este proyecto fue desarrollado con **Python** que permite tener conversaciones con IA, ya sea de manera libre o seleccionando una serie de preguntas previamente definidas. En este caso se opto por usar **Gemini** pero se puede implimentar cualquier otra IA.

## Instalación

1. **Clona el repositorio:**
    ```bash
      git clone https://github.com/edwinmghdez/script-ia-python

      cd script-ia-python
    ```

2. **Instala las dependencias:**
    ```bash
      pip install -r requirements.txt
    ```
3. **Configura las variables de entorno:**
    ```bash
      cp .env.example .env
    ```
  - Copia el archivo `.env.example` a `.env` y ajusta los valores según tu entorno.

4. **Ejecutar:**

    Desde la raíz del proyecto, ejecuta el asistente con:

    ```bash
      python src/main.py
    ```

## Estructura

- `src/config`:
  - Almacena la configuración del contexto y las preguntas que se mostrarán en el modo predefinido.
- `src/modules`:
  - Contiene todos los módulos que implementaremos en el script, en este caso se cuenta con `free_questions.py` y `predefined_questions.py`, cualquier otro caso de uso se colocaria dentro de este directorio.
- `src/services`:
  - Implementar la lógica para interactual con diferentes IAs.
- `main.py`:
  - Se encuentra la gestión de los diferentes módulos.

## Modos de uso

- **Modo libre:** Puedes hacer cualquier pregunta.
- **Modo predefinido:** Selecciona preguntas de una lista, usando el contexto empresarial definido.
