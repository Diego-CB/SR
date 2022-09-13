''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  Drivers.py
  - Have the instructions to render 
    models using gl.py functions
  
  Last modified (yy-mm-dd): 2022-09-12 
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
  L, filename
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
  glFinish(filename)

# ------ Modelos ------

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

def Mario_normal():
  model = './models/Mario/Mario.obj'
  texture = './models/Mario/Mario.bmp'
  LIGHT = (0, 0, -1)
  W = 1000

  transform = (
    0,
    0,
    0
  )
  scale = (
    0.7,
    0.7, 
    0.7,
  )
  rotate = (
    pi/2,
    pi,
    0,
  )

  eye = (0, 0, 5)
  center = (0, 0, 0)
  up = (0, 1, 0)
  coeff = -0.01

  __paintModel(
    model, texture, W, transform, scale, rotate, 
    eye, center, up, coeff, LIGHT, 'mario_medium'
  )

def Mario_medium():
  model = './models/Mario/Mario.obj'
  texture = './models/Mario/Mario.bmp'
  LIGHT = (0, 0, -1)
  W = 1000

  transform = (
    0,
    -0.5,
    0
  )
  scale = (
    0.76,
    0.76, 
    0.76,
  )
  rotate = (
    pi/2,
    pi,
    0,
  )

  eye = (0, 0, 5)
  center = (0, 0, 0)
  up = (0, 1, 0)
  coeff = -0.0001

  __paintModel(
    model, texture, W, transform, scale, rotate, 
    eye, center, up, coeff, LIGHT, './Renders/mario_medium'
  )

def Mario_lowangle():
  model = './models/Mario/Mario.obj'
  texture = './models/Mario/Mario.bmp'
  LIGHT = (0, -0.3, -0.7)
  W = 1000

  transform = (
    0,
    0,
    -0.5
  )
  scale = (
    0.8,
    0.8,
    0.88
  )
  rotate = (
    pi * 0.98/2,
    pi,
    pi * 1/30
  )

  eye = (0, 65, 35)
  center = (0, 0, 0)
  up = (0, 1, 0)
  coeff = 0.3

  __paintModel(
    model, texture, W, transform, scale, rotate, 
    eye, center, up, coeff, LIGHT, './Renders/Mario_low'
  )

def Mario_highangle():
  model = './models/Mario/Mario.obj'
  texture = './models/Mario/Mario.bmp'
  LIGHT = (0, 0, -1)
  W = 600

  transform = (
    0,
    1,
    -1.2
  )
  scale = (
    0.75,
    0.75, 
    0.80
  )
  rotate = (
    pi * 1/2,
    pi * 86/85,
    pi * 1/10
  )

  eye = (0, -200, 80)
  center = (0, 0, 0)
  up = (0, 1, 0)
  coeff = 0.2

  __paintModel(
    model, texture, W, transform, scale, rotate, 
    eye, center, up, coeff, LIGHT, './Renders/mario_high'
  )

def Mario_dutch():
  model = './models/Mario/Mario.obj'
  texture = './models/Mario/Mario.bmp'
  LIGHT = (0, 0, -1)
  W = 1000

  transform = (
    -0.25,
    0,
    -2.5
  )
  scale = (
    0.7,
    0.7, 
    0.7
  )
  rotate = (
    pi * 1/2,
    pi,
    -pi * 0.75/2
  )

  eye = (0, 30, 70)
  center = (0, 0, 0)
  up = (30, 70, 0)
  coeff = 0.15

  __paintModel(
    model, texture, W, transform, scale, rotate, 
    eye, center, up, coeff, LIGHT, './Renders/Mario_dutch'
  )

