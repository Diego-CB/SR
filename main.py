''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  main.py
  - main program to write files
  
  Last modified (yy-mm-dd): 2022-07-24
--------------------------------------
'''

from tkinter import W


if __name__ == '__main__':
  from src.gl import *
  from src.Obj import Obj

  glInit() # Initalization

  # Viewport and window initialization
  WSIZE = [2000, 2000]
  glCreateWindow  (*WSIZE)
  glCreateViewPort(*WSIZE)

  # Clear of the window
  glCLearColor(0, 0, 0)
  glClear()

  car = Obj('./models/Rims&Tires.obj')
  
  def transform_vertex(vertex, translate, scale):
    return [
      round(vertex[0] * scale[0]) + translate[0],
      round(vertex[1] * scale[1]) + translate[1]
    ]


  scale_factor = (50, 50)
  t_factor = (1000, 1000)

  #for face in car.faces:
  #  cube_vertex = []
  #
  #  for actual_f in face:
  #    temp = car.vertices[actual_f[0] - 1]
  #    temp = transform_vertex(temp, t_factor, scale_factor)
  #    cube_vertex.append(temp)
  #
  #  pintar(cube_vertex, normalized=False)
  #
  #  
  #glColor(0, 0, 0)

  for face in car.faces:
    cube_vertex = []

    for actual_f in face:
      temp = car.vertices[actual_f[0] - 1]
      temp = transform_vertex(temp, t_factor, scale_factor)
      cube_vertex.append(temp)
      
    perim_fig(cube_vertex, normalized=False)

  
  #cube_vertex = []
  #for face in cube.faces:
  #  for actual_f in face:
  #    temp = cube.vertices[actual_f[0] - 1]
  #    temp = transform_vertex(temp, t_factor, scale_factor)
  #    cube_vertex.append(temp)
  #
  #pintar(cube_vertex, normalized=False)
  #
  #glColor(0.8, 0.15, 0.1)
  #perim_fig(cube_vertex, normalized=False)

  glFinish('out')
