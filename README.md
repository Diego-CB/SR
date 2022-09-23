# Proyecto 1: Software Renderer

## 📡 Tecnologias Utilizadas
- Python 🐍: Modern syntax, Interpreted Languaje
  > Python 10.0 or higher needed

## ✅ Rúbrica:

  - [ ] 10 puntos por cada modelo que se cargue y renderize. Máximo de 5 modelos
    - Pueden poner los modelos que quieran, pero solo los primeros 5 valen puntos
    - Su modelo debe estar texturizado o tener materiales asignados para que valga puntos (shaders estan bien tambien)
    - También debe estar coherente mente ubicado en el mundo (transformaciones)
    
  - [ ] 5 puntos por cada shader distinto que se aplique a un modelo. Máximo 5 shaders
    - Aplicar el mismo shader a más de un modelo sólo les da puntos la primera vez
    - El shader no debe ser trivial y debe ser significativamente distinto a los demás shaders en su escena

  - [ ] 20 puntos por implementar mapas normales o bump mapping
    - Es suficiente con que lo apliquen a un solo modelo. No puede ser un modelo trivial
    
  - [ ] 0 - 20 puntos según la complejidad del modelo más complejo (20 es muy complejo, algo cómo un personaje, 0 es algo como un cubo o una pirámide)
  - [ ] 0 - 20 puntos según la estética de la escena (20 es una escena que se mira muy bien y no deja espacios en negro, 0 es un cubo en un fondo negro)

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
