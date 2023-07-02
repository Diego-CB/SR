''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  Drivers.py
  - Have the instructions to render 
    models using gl.py functions
  
  Last modified (yy-mm-dd): 2022-09-17
--------------------------------------
'''

from src.gl import *
from src.Shaders import *

def __Init(size, shader):
  glInit(shader)
  x, y = size if type(size) in [tuple, list] else size, size
  glCreateWindow (x, y) # Viewport and window initialization

def paintModel(
  model, texture,
  transform, scale, rotate, 
  eye, center, up, coeff,
  L, SR, shader=gouraud
):
  print('\nRenderizando:', model)
  if texture is not None: print('Con texturas:', texture)

  SR.current_shader = shader
  SR.lookAt(V3(*eye), V3(*center), V3(*up), coeff)
  SR.load_model(
    model, 
    L,
    transform,
    scale    ,
    rotate   ,
    texture
  )
