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

from cmath import pi
from src.gl import *

def __Init(size):
  # Initalization
  glInit()
  x, y = size if type(size) in [tuple, list] else size, size

  # Viewport and window initialization
  glCreateWindow  (x, y)
  glCreateViewPort(x, y)


def __paintModel(
  model, texture, W, 
  transform, scale, rotate, 
  eye, center, up, coeff,
  L
):
  print('\nRenderizando:', model, '\nCon texturas:', texture)
  __Init(W)
  lookAt(eye, center, up, coeff)

  load_model(
    model, 
    L,
    transform,
    scale    ,
    rotate   ,
    texture
  )

  # File Writing
  glFinish('./renders/' + model.split('/')[-1].split('.')[0])

# ------ Modelos ------

def Mario():
  model = './models/Mario/Mario.obj'
  texture = './models/Mario/Mario.bmp'
  LIGHT = (-15, 10, -100)
  W = 1024

  transform = (
    round(W / 2),
    round(W / 2),
    0
  )
  scale = (
    round(W / 6),
    round(W / 6), 
    round(W / 6), 
  )
  rotate = (
    0,
    pi * 2/3,
    pi * 2/3
  )

  __paintModel(
    model, texture, W, transform, scale, rotate, LIGHT
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

def Face():
  model = './models/Face/face.obj'
  texture = './models/Face/model.bmp'
  LIGHT = (0, 0, -1)
  W = 1000

  transform = (
    0,
    0,
    0
  )
  scale = (
    1,
    1, 
    1,
  )
  rotate = (
    0,
    pi/2,
    0
  )

  eye = (0, 0, 5)
  center = (0, 0, 0)
  up = (0, 1, 0)
  coeff = -0.001

  __paintModel(
    model, texture, W, transform, scale, rotate, 
    eye, center, up, coeff, LIGHT
  )
