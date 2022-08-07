''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  main.py
  - main program to write files
  
  Last modified (yy-mm-dd): 2022-07-31
--------------------------------------
'''

if __name__ == '__main__':
  from src.gl import *

  # Initalization
  glInit()

  # Viewport and window initialization
  W = 2000
  glCreateWindow  (W, W)
  glCreateViewPort(W, W)

  # Clear of the window
  glCLearColor(0, 0, 0)
  glClear()

  # Obj Model Drawing
  t = round(W / 2)
  s = round(t / 20)
  transform = (t, t)
  scale = (s, s)
  vertex_to_draw = (0, 1) # y, z
  model = './models/Rims&Tires.obj'

  glColor(0.9, 0.6, 0.28)
  wireframe_model(model, transform, scale, vertex_to_draw, 'paint')

  glColor(0, 0, 0)
  wireframe_model(model, transform, scale, vertex_to_draw)

  # File Writing
  glFinish('out')
