''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  main.py
  - main program to write files
  
  Last modified (yy-mm-dd): 2022-08-08
--------------------------------------
'''

if __name__ == '__main__':
  from src.gl import *

  # Initalization
  glInit()

  # Viewport and window initialization
  W = 800
  glCreateWindow  (W, W)
  glCreateViewPort(W, W)

  # Obj Model Drawing
  t = round(W / 2)
  s = round(9.6/10 * t)
  transform = (t, t, t)
  z_scale = round(1.2 * s)
  scale = (s, s, z_scale)
  model = './models/Rims&Tires.obj'
  model = './models/cube.obj'
  model = './models/face.obj'

  load_model(model, transform, scale, L=(-0.3,  0.4, -1))

  # File Writing
  glFinish('out')
  gl_zBuffer('z_out', z_scale)
