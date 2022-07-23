''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  gl.py
  - Uses de Renderer Object to
    write bmp files

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
  if x < -1 or x > 1: raise Exception('invalid coordinates:', [x, y])
  if y < -1 or y > 1: raise Exception('invalid coordinates:', [x, y])

  SR.point(x, y)

def glLine(x0, y0, x1, y1):
  sr_isInit()
  SR.line(x0, y0, x1, y1)

def square_perim(limit = 1):
  ''' Draws an square perimeter in the viewport '''
  limit_d = limit * -1

  for i in range(2):
    x = limit_d

    while x <= limit:
      y = limit_d

      while y <= limit:
        if i == 0:
          glVertex(x, y)
        else:
          glVertex(y, x)

        y += 0.001
      
      x += limit * 2

def square_perim(limit = 1):
  ''' Draws an square perimeter in the viewport '''
  glLine(-limit, limit, limit, limit)
  glLine(-limit, -limit, limit, -limit)
  
  glLine(-limit, -limit, -limit, limit)
  glLine(limit, -limit, limit, limit)


def filled_square():
  limit = round(max([SR.viewPort_h, SR.viewPort_w]) / 2)
  ls = [x/limit for x in range(1, limit)]
  for i in ls:
    square_perim(i)

  glVertex(0, 0)
  glVertex(0.001, 0)
  glVertex(0, 0.001)
  glVertex(0.001, 0.001)


def Bx(y):
  rangos = []
  i = 0

  while i < len(SR.framebuffer[y]):
    actual_i = i
    
    if SR.framebuffer[y][i] != SR.clear_color:
      flag = True
      rango = [actual_i, 0]

      while flag:
        rango[1] = i

        if SR.framebuffer[y][i] == SR.clear_color:
          flag = False
          rango[1] = i - 1
          rangos.append(rango)
          break
        
        i += 1
    i += 1
  
  return rangos

def By(x):
  pass

def pintar():
  pass

