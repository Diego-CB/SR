# SR1: Point

## 🕹️ Tecnologias Utilizadas
- Python 🐍: Modern syntax, Interpreted Languaje

## ✅ Rúbrica:

- [x] (05 puntos) Deben crear una función glInit() que inicialice cualquier objeto interno que requiera su software renderer
- [x] (05 puntos) Deben crear una función glCreateWindow(width, height) que inicialice su framebuffer con un tamaño (la imagen resultante va a ser de este tamaño
- [x] (10 puntos)  Deben crear una función glViewPort(x, y, width, height) que defina el área de la imagen sobre la que se va a poder dibujar (hint)
- [x] (20 puntos) Deben crear una función glClear() que llene el mapa de bits con un solo color
- [x] (10 puntos) Deben crear una función glClearColor(r, g, b) con la que se pueda cambiar el color con el que funciona glClear(). Los parámetros deben ser números en el rango de 0 a 1.
- [x] (30 puntos) Deben crear una función glVertex(x, y) que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron con glViewPort. glVertex(0, 0) cambia el color del punto en el centro del viewport, glVertex(1, 1) en la esquina superior derecha. glVertex(-1, -1) la esquina inferior izquierda. (hint)
- [x] (15 puntos) Deben crear una función glColor(r, g, b) con la que se pueda cambiar el color con el que funciona glVertex(). Los parámetros deben ser números en el rango de 0 a 1.
- [x] (05 puntos) Deben crear una función glFinish() que escriba el archivo de imagen

## Estructura de Archivos
- `src`
  - *util.py*: Funciones de uso general.
  - *Render.py*: Objeto interno que utiliza el software renderer.
  - *gl.py*: Implementación de las funcionalidades del software renderer.
- *main.py*: Programa principal
## 🤓 Autor

Diego Cordova - 20212