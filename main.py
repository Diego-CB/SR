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
  coeff = 0.0001

  paintModel(
    model, texture, transform, scale, 
    rotate, eye, center, up, coeff, 
    LIGHT, SR
  )
  gl.glFinish('./Renders/Jupiter')


  # moon - model
  model = './models/Moon/Moon.obj'
  texture = './models/Moon/moon2.bmp'

  LIGHT = (0, 0, 1) # x y z
  SIZE = 0.25
  rotate = (
    0,
    0,
    0
  )
  transform = (
    0.8,
    -0.8,
    0
  )
  scale = (SIZE, SIZE, SIZE)

  paintModel(
    model, texture, transform, scale, 
    rotate, eye, center, up, coeff, 
    LIGHT, SR
  )
  gl.glFinish('./Renders/Jupiter')


  # Atronaut - model
  model = './models/Astronaut/astronaut.obj'
  texture = './models/Astronaut/texture.bmp'

  LIGHT = (-1, 0, 1) # x y z
  W = 200
  SIZE = 0.17
  rotate = (
    pi * 1/7,
    pi * 1/8,
    0
  )
  transform = (
    0.60,
    0.15,
    0
  )
  scale = (SIZE, SIZE, SIZE)
  
  paintModel(
    model, texture, transform, scale, 
    rotate, eye, center, up, coeff, 
    LIGHT, SR
  )
  gl.glFinish('./Renders/Jupiter')

else:

  # Satelite
  model = './models/NoText/Satellite.obj'
  texture = None

  LIGHT = (0, 0, 1) # x y z
  W = 400
  SIZE = 1
  rotate = (
    pi * 1/8,
    pi * 1/3,
    0
  )
  transform = (
    0,
    0,
    0
  )
  scale = (SIZE, SIZE, SIZE)

  center = (0, 0, 0)
  eye = (0, 0, 1)
  up = (0, 1, 0)
  coeff = 0.0001

  paintModel(
    model, texture, W, transform, scale, 
    rotate, eye, center, up, coeff, LIGHT, 'Renders/Jupiter'
  )

  # Ship
  model = './models/SpaceX/f.obj'
  texture = './models/SpaceX/mat.bmp'

  LIGHT = (0, 1, 0) # y z x
  W = 200
  SIZE = 0.2
  rotate = (
    pi * 1/8,
    pi * 1/6,
    0
  )
  transform = (
    0,
    0,
    0
  )
  scale = (SIZE, SIZE, SIZE)

  center = (0, 0, 0)
  eye = (0, 0, 1)
  up = (0, 1, 0)
  coeff = 0.0001

  paintModel(
    model, texture, W, transform, scale, 
    rotate, eye, center, up, coeff, LIGHT, 'Renders/Jupiter'
  )

