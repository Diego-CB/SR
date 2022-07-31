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

  glInit() # Initalization

  # Viewport and window initialization
  W = 4000
  WSIZE = [W, W]
  glCreateWindow  (*WSIZE)
  glCreateViewPort(*WSIZE)

  # Clear of the window
  glCLearColor(0, 0, 0)
  glClear()

  glColor(0.9, 0.6, 0.28)
  glColor(1, 1, 1)
  t = round(W / 2)
  s = round(t / 20)
  transform = (t, t)
  scale = (s, s)
  scale = (1000, 1000)
  vertex_to_draw = (1, 2) # y, z
  model = './models/Rims&Tires.obj'
  model = './models/cube.obj'

  wireframe_model(model, transform, scale, vertex_to_draw)

  glFinish('out')
