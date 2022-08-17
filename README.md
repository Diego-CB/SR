# SR5: Texturas

## 📡 Tecnologias Utilizadas
- Python 🐍: Modern syntax, Interpreted Languaje

## ✅ Rúbrica:

  - [x] Código fuente capaz de cargar un archivo .obj al software renderer
  - [x] Código fuente capaz de cargar un archivo de textura .bmp al software renderer y asociarlo con su obj
  - [x] Archivo obj de su elección 
  - [x] Código fuente capaz de renderizar los vértices de textura de su archivo obj

## 🗃️ Estructura de Archivos

- **`models`**

  - Dentro de esta carpeta se encuentran los modelos a utilizar.
  - **`NoText`**: En esta carpeta estan los modelos sin texturas.
  - En las demás carpetas estan los modelos con texturas.

- **`src`**

  - `util.py`: Funciones de uso general.
  - `Vector.py`: Contiene **V3** (Objeto interno que representa un vector en 3D).
  - `IO_bmp`: Funciones de lectura y escritura de archivos bmp.
  - `Obj.py`: Objeto interno que se utiliza para leer y cargar modelos en formato obj al framebuffer.
  - `Texture.py`: Objeto que representa el mapa de texturas de un modelo.
  - `Render.py`: Objeto interno que utiliza el software renderer.
  - `gl.py`: Implementación de las funcionalidades del software renderer.

- **`Renders`**: Dentro de esta carpeta se encuentran las imagenes resultantes de las renderizaciones realizadas.

- `Drivers.py`: Funciones de renderizado de modelos.
- `main.py`: Programa principal.

## 🕹️ Getting Started

1. Ejecute el archivo `main.py`.
2. Se Creara una carpeta **`__pycache__`** dentro de la carpeta **`src`**.
3. Se mostrará un menú con las opciones de renderización disponibles.
4. Si no existen errores en ejecución, se escribirá un achivo `.bmp` con la imagen resultante en la carpeta **`Renders`**.

## 🤓 Autor

Diego Cordova - 20212
