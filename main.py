''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  main.py
  - main program to write files
  
  Last modified (yy-mm-dd): 2022-09-12
--------------------------------------
'''

if __name__ == '__main__':
  from Drivers import *

  print('\n----- Initializing moon Rendering with shaders -----')
  model = './models/Face/face.obj'
  texture = './models/Face/model.bmp'
  LIGHT = (0, 0, -1)
  W = 800
  SIZE = 1

  transform = (0, 0, 0)
  scale = (SIZE, SIZE, SIZE)
  rotate = (0, pi * 1/5, 0)

  eye = (0, 0, 5)
  center = (0, 0, 0)
  up = (0, 1, 0)
  coeff = -0.0001

  paintModel(
    model, texture, W, transform, scale, rotate, 
    eye, center, up, coeff, LIGHT, 'Renders/Moon'
  )

