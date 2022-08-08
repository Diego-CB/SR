''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  main.py
  - main program to write files
  
  Last modified (yy-mm-dd): 2022-08-07
--------------------------------------
'''

if __name__ == '__main__':
  from src.gl import *

  # Initalization
  glInit()

  # Viewport and window initialization
  W = 1200
  glCreateWindow  (W, W)
  glCreateViewPort(W, W)

  # Clear of the window
  glCLearColor(0, 0, 0)
  glClear()

  # Obj Model Drawing
  t = round(W / 2)
  s = round(9/10 * t)
  s = round(t / 2.5)
  transform = (t, t, t)
  scale = (s, s, s)
  model = './models/Rims&Tires.obj'
  model = './models/face.obj'
  model = './models/cube.obj'

  load_model(model, transform, scale)

  glColor(.7, 0, 0)
  #wireframe_model(model, transform, scale)

  # File Writing
  glFinish('out')
  gl_zBuffer('z_out', s)
