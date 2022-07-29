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

from locale import normalize
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

  global v_width_d
  global v_height_d
  global v_width_u
  global v_height_u
  global x_offset
  global y_offset 
  v_width_d = (SR.viewPort_w - 1) / 2
  v_height_d = (SR.viewPort_h - 1) / 2
  v_width_u = SR.viewPort_w / 2
  v_height_u = SR.viewPort_h / 2
  x_offset = round((SR.window_w - width) / 2)
  y_offset = round((SR.window_h - height) / 2)

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

  actual_w = v_width_d if x <= 0 else v_width_u
  actual_h = v_height_d if y <= 0 else v_height_u

  y_normal = round(actual_h * (y + 1)) + y_offset
  x_normal = round(actual_w * (x + 1)) + x_offset
  return x_normal, y_normal

def glVertex(x, y, normalized:bool=True):
  ''' writes a pixel inside the viewport '''
  sr_isInit()
  if normalized:
    if x < -1 or x > 1: raise Exception('invalid coordinates:', [x, y])
    if y < -1 or y > 1: raise Exception('invalid coordinates:', [x, y])

  points = denormalize(x, y) if normalized else (x, y)
  SR.point(*points)

def glLine(x0, y0, x1, y1, normalized=False):
  '''
    Draws a line of pixels from point
    [x0, y0] to [x1, y1] on the viewport
  '''
  sr_isInit()

  if normalized:
    x0, y0 = denormalize(x0, y0)
    x1, y1 = denormalize(x1, y1)
    
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
    actual_pixel = [y, actual_x] if inverse else [actual_x, y]
    SR.point(*actual_pixel)

    if augment > round_limit:
      y += 1 if y0 < y1 else -1
      round_limit += 2 * dx

# ------------ Funciones para Relleno de Poligonos ------------

def denormalize_poly(p:list[list]) -> list[list]:
  temp_a = []

  for n in range(len(p)):
    temp_a.append([*denormalize(*p[n])])

  return temp_a

def perim_fig(p:list[list], normalized=True):
  ''' Draws the contorn of a polygon based a series of points '''

  if normalized == True:
    p = denormalize_poly(p)

  for n in range(0, len(p)):
    x0 = p[n][0]
    y0 = p[n][1]
    x1 = 0
    y1 = 0

    if n < len(p) - 1:
      x1 = p[n+1][0]
      y1 = p[n+1][1] 

    else:
      x1 = p[0][0]
      y1 = p[0][1]

    glLine(x0, y0, x1, y1)

def Bx(y:int, x0:int, x1:int) -> list:
  '''
    Checks for filling area in a especific y 
    coordinate between x0 and x1 intervals
  '''
  rangos = []
  i = x0

  while i <= x1:
    actual_i = i

    if SR.framebuffer[y][i] == SR.current_color:
      flag = True

      while flag:
        i += 1

        if i == SR.window_w:
          flag = False
          
        elif SR.framebuffer[y][i] != SR.current_color:
          flag = False
          rangos.append([actual_i, i - 1])

    i += 1
  
  return rangos

def By(x: int, y0: int, y1: int) -> list:
  '''
    Checks for filling area in a especific x
    coordinate between y0 and y1 intervals
  '''
  rango = []
  initial = -1

  for y in range(y0, y1 + 1):
    if SR.framebuffer[y][x] == SR.current_color:
      if initial == -1:
        initial = y

      else:
        if SR.framebuffer[y - 1][x] != SR.current_color:
          rango.append([initial, y])
          initial = -1
  
  return rango

def get_poly_area(p:list[list]) -> int:
  ''' Get Area in wich a a polygon is drawed '''
  x_points:list = []
  y_points:list = []

  for n in p:
    x_points.append(n[0])
    y_points.append(n[1])

  return (
    min(x_points), max(x_points), 
    min(y_points), max(y_points)
  )

def pintar(p:list[list], normalized=True):
  ''' Fills the area of a polygon with color '''

  if normalized == True:
    p = denormalize_poly(p)
  
  perim_fig(p, normalized=False)
  min_x, max_x, min_y, max_y = get_poly_area(p)

  for y in range(min_y, max_y + 1):
    rangos_x = Bx(y, min_x, max_x)
        
    for n in range(len(rangos_x) - 1):
      x0 = rangos_x[n][1]
      x1 = rangos_x[n + 1][0]
      x_check = x0 + round((x1 - x0) / 2)
      rangos_y = By(x_check, min_y, max_y)

      for yy in rangos_y:
        if y >= yy[0] and y <= yy[1]:
          glLine(x0, y, x1, y)
          break

# -------- Funciones Extra --------

def square_perim(limit = 1):
  ''' Draws an square perimeter in the viewport '''
  glLine(-limit, limit, limit, limit)
  glLine(-limit, -limit, limit, -limit)
  
  glLine(-limit, -limit, -limit, limit)
  glLine(limit, -limit, limit, limit)

def filled_square(n):
  ''' Draws n sauqre perimeters into the viewport'''
  for i in [x/n for x in range(1, n)]:
    square_perim(i)
