''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  Lab1.py
  - main program to write files
  
  Last modified (yy-mm-dd): 2022-07-24
--------------------------------------
'''

if __name__ == '__main__':
  from src.gl import *

  # Poligonos 
  P1 = [[165, 380], [185, 360], [180, 330], [207, 345], [233, 330], [230, 360], [250, 380], [220, 385], [205, 410], [193, 383]]
  P2 = [[321, 335], [288, 286], [339, 251], [374, 302]]
  P3 = [[377, 249], [411, 197], [436, 249]]
  P4 = [[413, 177], [448, 159], [502, 88], [553, 53], [535, 36], [676, 37], [660, 52], [750, 145], [761, 179], [672, 192], [659, 214], [615, 214], [632, 230], [580, 230], [597, 215], [552, 214], [517, 144], [466, 180]]
  P5 = [[682, 175], [708, 120], [735, 148], [739, 170]]
  POLYGONS = [P1, P2, P3, P4, P5]

  # ------------ main ------------

  # Initalization

  IMG_SIZE = [800, 430]

  glInit() 
  glCreateWindow(*IMG_SIZE)
  glCreateViewPort(*IMG_SIZE)
  glClear()

  # Dibujo de los poligonos

  for fig in POLYGONS:
    if fig == POLYGONS[-1]:
      glColor(0, 0, 0)
      glCLearColor(1, 1, 1)

    perim_fig(fig)
    pintar(fig)

  glFinish('out') # File writting
