''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  gl.py
  - Uses de Renderer Object to
    write bmp files

  Last modified (yy-mm-dd): 2022-07-24
--------------------------------------
'''

from operator import index
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

def glCreateWindow(width: int, height: int):
  ''' Initialize Window of image '''
  sr_isInit()
  SR.initWindow(width=width, height=height)

def glCreateViewPort(width: int, height: int):
  ''' Initialize viewport of image '''
  sr_isInit()
  SR.initViewPort(width=width, height=height)

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

def glVertex(x, y):
  ''' writes a pixel inside the viewport '''
  sr_isInit()
  SR.point(x, y)

def glLine(x0, y0, x1, y1):
  '''
    Draws a line of pixels from point
    [x0, y0] to [x1, y1] on the viewport
  '''
  sr_isInit()
    
  dy = abs(y1 - y0)
  dx = abs(x1 - x0)
  inverse = dy > dx

  if inverse:
    x0, y0 = y0, x0
    x1, y1 = y1, x1
    dx, dy = dy, dx

  if x0 > x1:
    x0, x1 = x1, x0
    y0, y1 = y1, y0

  round_limit = dx
  y = y0

  for x in range(dx + 1):
    augment = dy * x * 2
    actual_x = x0 + x

    if augment > round_limit:
      y += 1 if y0 < y1 else -1
      round_limit += 2 * dx

    actual_pixel = [y, actual_x] if inverse else [actual_x, y]
    SR.point(*actual_pixel)

# -------- Funciones para Relleno de Poligonos --------

def Bx(y):
  rangos = []
  i = 0

  while i < len(SR.framebuffer[y]):
    actual_i = i

    if SR.framebuffer[y][i] != SR.clear_color:
      flag = True

      while flag:
        i += 1

        if SR.framebuffer[y][i] == SR.clear_color:
          flag = False
          rangos.append([actual_i, i - 1])

    i += 1
  
  return rangos

def By():
  rangos_y = [[] for x in range(SR.window_w)]

  for x in range(SR.window_w):
    initial = -1

    for y in range(SR.window_h):

      if SR.framebuffer[y][x] != SR.clear_color:
        if initial == -1:
          initial = y

        else:
          if SR.framebuffer[y - 1][x] == SR.clear_color:
            rangos_y[x].append([initial, y])
            initial = -1
  
  return rangos_y

#def By(x):
#  rango = []
#  initial = -1
#
#  for y in range(SR.window_h):
#
#    if SR.framebuffer[y][x] != SR.clear_color:
#      if initial == -1:
#        initial = y
#
#      else:
#        if SR.framebuffer[y - 1][x] == SR.clear_color:
#          rango.append([initial, y])
#          initial = -1
#  
#  return rango

def pintar():
  rangos_y = By()

  for y in range(SR.window_h):
    rangos_x = Bx(y)
        
    for n in range(len(rangos_x) - 1):
      x0 = rangos_x[n][1]
      x1 = rangos_x[n+1][0]
      x_check = x0 + round((x1 - x0) / 2)

      for yy in rangos_y[x_check]:
        if y >= yy[0] and y <= yy[1]:
          glLine(x0, y, x1, y)
          break
        
