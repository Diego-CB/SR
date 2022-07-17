''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  gl.py
  - Applies the 

  Last modified (yy-mm-dd): 2022-07-17
--------------------------------------
'''

from .Render import Render
from .util import color

def glInit():
  ''' Initialized Internal Render Object '''
  global SR
  SR = Render()

def sr_isInit():
  '''
    Checks if Internal Object is Initialized
    If not, reaises exception
  '''

  try:
    SR.current_color

  except NameError:
    raise Exception('ERROR: Software Renderer not initialized\n\
       execute glInit before any action\n\
    ')

def glCreateWindow(width, height):
  ''' Initialize Window of image '''
  sr_isInit()
  SR.initWindow(width=width, height=height)

def glCreateViewPort(width, height):
  ''' Initialize viewport of image '''
  sr_isInit()
  SR.initViewPort(width=width, height=height)
  global v_width
  global v_height
  global x_offset 
  global y_offset 
  v_width = SR.viewPort_w - 1
  v_height = SR.viewPort_h - 1
  x_offset = SR.x_offset
  y_offset = SR.y_offset

def glClear():
  ''' Fills image with one plain color (clear_color)'''
  sr_isInit()
  SR.clear()

def glCLearColor(r, g, b):
  ''' changes clear_color'''
  sr_isInit()
  SR.set_clear_color(color(r, g, b))

def glColor(r, g, b):
  ''' changes the color for writting pixels '''
  sr_isInit()
  SR.set_current_color(color(r, g, b))

def glFinish(fileName):
  ''' Writes bmp file '''
  sr_isInit()
  try:
    SR.write(fileName + '.bmp')
    print('File', fileName + '.bmp written succesfully!!')
  except:
    print('ERROR during file writting')

def denormalize(x, y):
  ''' 
    Takes normalized coordinates and transforms
    them into coordinates for the framebuffer
    inside the viewport
  '''
  sr_isInit()
  x_normal = int(v_width * (x + 1)/2 + x_offset)
  y_normal = int(v_height * (y + 1)/2 + y_offset)
  return x_normal, y_normal
  
def glVertex(x, y):
  ''' writes a pixel inside the viewport '''
  sr_isInit()
  if x < -1 or x > 1: raise Exception('invalid coordinates:', [x, y])
  if y < -1 or y > 1: raise Exception('invalid coordinates:', [x, y])

  SR.point(*denormalize(x, y))
