''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  main.py
  - main program to write files
  
  Last modified (yy-mm-dd): 2022-09-17
--------------------------------------
'''

if __name__ == '__main__':
  from Drivers import *
  from src.Shaders import *
  from cmath import pi
  import src.gl as gl

  # Setting Background Image
  gl.glInit()
  gl.glCreateWindow(1500, 1500)
  SR = gl.setBG('./models/bg.bmp')

  # Earth - model
  model = './models/E/Globe.obj'
  texture = './models/E/Albedo-diffuse_Low-end.bmp'

  LIGHT = (0, 0, 50) # x y z
  SIZE = 0.06
  rotate = (
    0,
    0,
    0
  )
  transform = (
    -0.6,
    0.6,
    0
  )
  scale = (SIZE, SIZE, SIZE)

  center = (0, 0, 0)
  eye = (0, 0, 1)
  up = (0, 1, 0)
  coeff = 0.001

  paintModel(
    model, texture, transform, scale, 
    rotate, eye, center, up, coeff, 
    LIGHT, SR, gouraud
  )
  gl.glFinish('./Renders/scene')


  # moon - model
  model = './models/Moon/Moon.obj'
  texture = './models/Moon/moon2.bmp'

  LIGHT = (0, 0, 1) # x y z
  SIZE = 0.35
  rotate = (
    0,
    0,
    0
  )
  transform = (
    0.58,
    -0.6,
    0
  )
  scale = (SIZE, SIZE, SIZE)

  paintModel(
    model, texture, transform, scale, 
    rotate, eye, center, up, coeff, 
    LIGHT, SR, moon_shader
  )
  gl.glFinish('./Renders/scene')


  # Atronaut - model
  model = './models/Astronaut/astronaut.obj'
  texture = './models/Astronaut/texture.bmp'

  LIGHT = (-1, 0, 1) # x y z
  W = 200
  SIZE = 0.14
  rotate = (
    pi * 1/7,
    pi * 1/8,
    0
  )
  transform = (
    0.65,
    0.2,
    0
  )
  scale = (SIZE, SIZE, SIZE)
  
  paintModel(
    model, texture, transform, scale, 
    rotate, eye, center, up, coeff, 
    LIGHT, SR, astronaut
  )
  gl.glFinish('./Renders/scene')

  # Satelite - model
  model = './models/NoText/Satellite.obj'
  texture = None
  SR.texture = None

  LIGHT = (0, 0, 1) # x y z
  SIZE = 0.6
  rotate = (
    pi * 1/8,
    pi * 1/3,
    -pi * 1/9
  )
  transform = (
    -0.45,
    -0.6,
    0
  )
  scale = (SIZE, SIZE, SIZE)

  paintModel(
    model, texture, transform, scale, 
    rotate, eye, center, up, coeff, 
    LIGHT, SR, satelite
  )
  gl.glFinish('./Renders/scene')


  # Ship - model
  model = './models/SpaceX/f.obj'
  texture = './models/SpaceX/mat.bmp'

  LIGHT = (0, 1, 0) # y z x
  SIZE = 0.075
  rotate = (
    pi * 1/7,
    -pi * 1/6,
    0
  )
  transform = (
    0.2,
    -0.1,
    0
  )
  scale = (SIZE, SIZE, SIZE)

  paintModel(
    model, texture, transform, scale, 
    rotate, eye, center, up, coeff, 
    LIGHT, SR, starship
  )
  gl.glFinish('./Renders/scene')

