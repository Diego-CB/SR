''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  Drivers.py
  - Have the instructions to render 
    models using gl.py functions
  
  Last modified (yy-mm-dd): 2022-08-17 
--------------------------------------
'''

from src.gl import *

def __Init(size):
  # Initalization
  glInit()
  x, y = size if type(size) in [tuple, list] else size, size

  # Viewport and window initialization
  glCreateWindow  (x, y)
  glCreateViewPort(x, y)

def __paintModel(model, texture, W, transform, scale, v_to_draw, L):
  print('\nRenderizando:', model, '\nCon texturas:', texture)
  __Init(W)

  load_model(
    model, transform, scale, L=L, 
    vertex_to_draw=v_to_draw , texture_path=texture
  )

  # File Writing
  glFinish('./renders/' + model.split('/')[-1].split('.')[0])


# ------ Modelos ------

def Mario():
  model = './models/Mario/Mario.obj'
  texture = './models/Mario/Mario.bmp'
  v_to_draw = (2, 0, 1) # z, x, y
  LIGHT = (-15, 10, -100)
  W = 1024

  transform = (
    round(W / 2),
    round(W / 2),
    round(W * 2)
  )
  scale = (
    round(W / 2.8),
    round(W / 2.8), 
    round(W / 4)
  )

  __paintModel(
    model, texture, W, transform, 
    scale, v_to_draw, LIGHT
  )
  

def Tmap_Mario():
  glInit()
  model = './models/Mario/Mario.obj'
  texture = './models/Mario/Mario.bmp'
  
  render_img(
    texture, model, './renders/Mario_texture', 
    color=(0, 0.6, 0)
  )

def Yoshi():
  model = './models/Yoshi/Yoshi.obj'
  texture = './models/Yoshi/Yoshi.bmp'
  v_to_draw = (2, 0, 1) # z, x, y
  LIGHT = (0, 0, -100)
  W = 1024

  transform = (
    round(W),
    round(W / 2),
    round(W * 2)
  )
  scale = (
    round(W / 2.8),
    round(W / 2.8), 
    round(W / 4)
  )

  __paintModel(
    model, texture, W, transform, 
    scale, v_to_draw, LIGHT
  )


def Tmap_Yoshi():
  glInit()
  model = './models/Yoshi/Yoshi.obj'
  texture = './models/Yoshi/Yoshi.bmp'

  render_img(
    texture, model, './renders/Yoshi_texture', 
    color=(0, 0, 0.6)
  )

def Face():
  model = './models/Face/face.obj'
  texture = './models/Face/model.bmp'
  v_to_draw = (0, 1, 2) # z, x, y
  LIGHT = (0, 0, -100)
  W = 1024

  transform = (
    round(W / 2),
    round(W / 2),
    round(W * 2)
  )
  scale = (
    round(W / 2.1),
    round(W / 2.1), 
    round(W / 4)
  )

  __paintModel(
    model, texture, W, transform, 
    scale, v_to_draw, LIGHT
  )

def Tmap_Face():
  glInit()
  model = './models/Face/face.obj'
  texture = './models/Face/model.bmp'
  render_img(texture, model, './renders/Face_texture')