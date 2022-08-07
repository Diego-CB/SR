# SR: Software Renderer

## 📡 Tecnologias Utilizadas
- Python 🐍: Modern syntax, Interpreted Languaje

## ✅ Rúbrica:

  - [x] Código fuente capaz de cargar un archivo .obj al software renderer.
  - [x] Archivo obj de su elección.
  - [ ] Código fuente capaz de renderizar el zbuffer de su archivo obj.
  - [ ] Código fuente capaz de renderizar el modelo usando flat shading.

## 🗃️ Estructura de Archivos

- **`models`**

  - Dentro de esta carpeta se encuentran los modelos a utilizar.

- **`src`**

  - `util.py`: Funciones de uso general.
  - `Render.py`: Objeto interno que utiliza el software renderer.
  - `Obj.py`: Objeto interno que se utiliza para leer y cargar modelos en formato obj al framebuffer.
  - `Vector.py`: Contiene **V3** (Objeto interno que representa un vector en 3D).
  - `gl.py`: Implementación de las funcionalidades del software renderer.

- `main.py`: Programa principal

## 🕹️ Getting Started

1. Ejecute el archivo `main.py`.
2. Se Creara una carpeta **`__pycache__`** dentro de la carpeta **`src`**.
3. Si no existen errores en ejecución, se escribirá un achivo `out.bmp` con la imagen resultante. 
   (Es posible cambiar el nombre del archivo de la imagen en `main.py`) 

## 🤓 Autor

Diego Cordova - 20212
