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
  W = 1024
  glCreateWindow  (W, W)
  glCreateViewPort(W, W)

  # Obj Model Drawing
  t = round(W / 2)
  s = round(t * 9/10)
  transform = (t, t, t)
  z_scale = round(s * 1.5)
  scale = (s, s, z_scale)

  model = './models/face.obj'
  v_to_draw = (2, 0, 1) # z, x, y
  v_to_draw = (0, 1, 2) # z, x, y
  LIGHT = (0, 0, -100)

  load_model(
    model, transform, scale, L=LIGHT, 
    vertex_to_draw=v_to_draw, texture_path='./models/model.bmp'
  )

  # File Writing
  glFinish('./renders/out')
  #render_img('./models/model.bmp', './renders/model')
