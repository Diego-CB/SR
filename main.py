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
  W = 4000
  glCreateWindow  (W, W)
  glCreateViewPort(W, W)

  # Obj Model Drawing
  t = round(W / 2)
  s = round(t / 6)
  transform = (t, round(t * 8.1/10), t)
  z_scale = round(6.5 * s)
  scale = (s, s, z_scale)

  model = './models/GUITAR.obj'
  v_to_draw = (2, 0, 1) # z, x, y
  LIGHT = (-10, 40, -100)

  load_model(model, transform, scale, L=LIGHT, vertex_to_draw=v_to_draw)

  # File Writing
  glFinish('out')
  gl_zBuffer('z_out', z_scale)
