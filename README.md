# SR6: TRansformaciones

## 📡 Tecnologias Utilizadas
- Python 🐍: Modern syntax, Interpreted Languaje
  > Python 10.0 or higher needed

## ✅ Rúbrica:

  - [x] Código fuente capaz de cargar un archivo .obj al software renderer
  - [x] Archivo obj de su elección 

  - Su código debe implementar las siguientes transformaciones utilizando matrices:
    - [x] Model
    - [x] View
    - [x] Projection
    - [x] Viewport

  - Photoshoot! Deben renderizar 4 tomas de su modelo:
    - [x] Medium shot
    - [x] Low angle
    - [x] High angle
    - [x] Dutch angle

## 🗃️ Estructura de Archivos

- **`models`**

  - Dentro de esta carpeta se encuentran los modelos a utilizar.
  - **`NoText`**: En esta carpeta estan los modelos sin texturas.
  - En las demás carpetas estan los modelos con texturas.

- **`src`**

  - `util.py`: Funciones de uso general.
  - `IO_bmp`: Funciones de lectura y escritura de archivos bmp.
  - `Obj.py`: Objeto interno que se utiliza para leer y cargar modelos en formato obj al framebuffer.
  - `Texture.py`: Objeto que representa el mapa de texturas de un modelo.
  - `Render.py`: Objeto interno que utiliza el software renderer.
  - `gl.py`: Implementación de las funcionalidades del software renderer.

  - **`MStructs`**: Contiene Implementacion de estructuras matematicas (vectores y matrices).
    - `Vector.py`: Contiene **V3** (Objeto interno que representa un vector en 3D).
    - `Matrix.py`
      * Contiene **V4** (Objeto interno que representa un vector en 4D).
      * Contiene **M4** (Objeto interno que representa una matriz en 4D).

- **`Renders`**: Dentro de esta carpeta se encuentran las imagenes resultantes de las renderizaciones realizadas.

- `Drivers.py`: Funciones de renderizado de modelos.
- `main.py`: Programa principal.

## 🕹️ Getting Started

1. Ejecute el archivo `main.py`.
2. Se mostrará un menú con las opciones de renderización disponibles.
3. Si no existen errores en ejecución, se escribirá un achivo `.bmp` con la imagen resultante en la carpeta **`Renders`**.

## 🤓 Autor

Diego Cordova - 20212
