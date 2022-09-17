# Lab2: Shaders

## 📡 Tecnologias Utilizadas
- Python 🐍: Modern syntax, Interpreted Languaje
  > Python 10.0 or higher needed

## ✅ Rúbrica:


  - [x] [Criterio subjetivo] 80 puntos según que tanto se parece su planeta a su imagen de referencia (deben adjuntar su render y su imagen)
  - [x] [Criterio subjetivo] 20 puntos según la complejidad de su planeta (la tierra sería el más complejo y urano el más simple)
  - [ ] 30 puntos por implementar el sistema de anillos de los planetas gaseosos (válido para saturno, jupiter, urano y neptuno)
    - Aplican las mismas reglas de no usar texturas ni materiales
  - [ ] 30 puntos por implementar las lunas en los planetas rocosos (válido para la tierra y marte)


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
  - `Shaders.py`: Contiene implementaciones de shaders.
  - `Render.py`: Objeto interno que utiliza el software renderer.
  - `gl.py`: Implementación de las funcionalidades del software renderer.

  - **`MStructs`**: Contiene Implementacion de estructuras matematicas (vectores y matrices).
    - `Vector.py`: Contiene **V3** (Objeto interno que representa un vector en 3D).
    - `Matrix.py`
      * Contiene **V4** (Objeto interno que representa un vector en 4D).
      * Contiene **M4** (Objeto interno que representa una matriz en 4D).

- **`Renders`**: Dentro de esta carpeta se encuentran las imagenes resultantes de las renderizaciones realizadas.
  - `template.png`: Imagen de referencia para el shader del planeta Jupiter.

- `Drivers.py`: Funciones de renderizado de modelos.
- `main.py`: Programa principal.

## 🕹️ Getting Started

1. Ejecute el archivo `main.py`.
2. Si no existen errores en ejecución, se escribirá un achivo `Jupiter.bmp` con la imagen resultante en la carpeta **`Renders`**.
  > path de la imagen: `./Renders/Jupiter.bmp`

## 🤓 Autor

Diego Cordova - 20212
