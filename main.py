''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  main.py
  - main program to write files
  
  Last modified (yy-mm-dd): 2022-07-17
--------------------------------------
'''
if __name__ == '__main__':
  from src.gl import *

  glInit() # Initalization

  # Viewport and window initialization
  glCreateWindow(1800, 1060)
  glCreateViewPort(1660, 1000)

  # Clear of the window
  glCLearColor(0, 0, 0)
  glClear()

  # Partes de la casa (Poligonos)

  TECHO = [[-.65, .8], [.8, .8], [.6, .15], [-.98, .15]]
  FRONT_WALL = [[-.76, .15], [.6, .15], [.6, -.75], [-.76, -.715]]
  COLUMN = [[-.95, .15], [-.9, .15], [-.9, -.7102], [-.95, -.7045]]
  SIDE_WALL = [
    [.8, .8], [.6, .15], [.6, -.75], [.9, -.57], [.9, .145]
  ]
  WINDOW = [
    [-.45, .15], [-.45, .26], [-.5, .265], 
    [-.15, .75], [.14, .26], [.1, .235], [.1, .15]
  ]
  WALL_DIV = [[-.45, .15], [.1, .15], [.1, -.737], [-.45, -.724]]
  TECHO2 = [
    [-.45, .26], [-.45, .25], [-.52, .2625], [-.15, .78],
    [.1, .6], [.18, .255], [.14, .26], [-.15, .75], [-.5, .265]
  ]

  VENT1 = [[-.4, .3], [-.15, .63], [.045, .3]]
  VENT2 = [[-.71, -.65], [-.71, .04], [-.5, .037], [-.5, -.657]]
  VENT3 = [[.2, -.3], [.2, 0], [.49, -.005], [.49, -.301]]
  DOOR = [[-.35, -.7265], [-.05, -.7345], [-.05, -.09], [-.35, -.0805]]

  HOUSE = [
    TECHO, FRONT_WALL, COLUMN, SIDE_WALL, WINDOW, WALL_DIV, TECHO2,
    VENT1, VENT2, VENT3, DOOR
  ]

  BACK = [[-1, 1], [1, 1], [1, -.028], [-1, 0]]
  GROUND = [[-1, 0], [1, -.028], [1, -1], [-1, -1]]

  # Pintado de poligonos

  # Fondo
  glColor(0, .5, .76)
  pintar(BACK, normalized=True)
  
  glColor(.37, .72, .09)
  pintar(GROUND, normalized=True)
  
  glColor(0, 0, 0)
  perim_fig(BACK, normalized=True)
  perim_fig(GROUND, normalized=True)

  # Casa
  WALLS = [FRONT_WALL, COLUMN, SIDE_WALL, WINDOW]
  TECHOS = [TECHO, TECHO2]
  WINDOWS = [VENT1, VENT2, VENT3]

  # Techo
  glColor(.65, 0.2, 0)
  for part in TECHOS:
    pintar(part, normalized=True)
  
  # Paredes
  glColor(.5, .55, .6)
  for part in WALLS:
    pintar(part, normalized=True)
  
  # Ventanas
  glColor(.2, .66, .7)
  for part in WINDOWS:
    pintar(part, normalized=True)

  # Puerta
  glColor(.4, .3, .25)
  pintar(DOOR, normalized=True)
  
  # Dibujo de perimetros
  glColor(0, 0, 0)
  for part in HOUSE:
    perim_fig(part, normalized=True)

  # File writting (rendering)
  glFinish('out')
