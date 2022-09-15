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
  
  LIGHT = (-50, 0, -50)
  W = 400
  SIZE = 0.9

  transform = center = rotate = (0, 0, 0)
  scale = (SIZE, SIZE, SIZE)
  eye = (0, 0, 5)
  up = (0, 1, 0)
  coeff = -0.01

  paintModel(
    './models/Shpere/sphere.OBJ', None, W, transform, scale, 
    rotate, eye, center, up, coeff, LIGHT, 'Renders/Moon'
  )

