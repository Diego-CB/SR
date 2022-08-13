''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  gl.py
  - Uses de Renderer Object to
    write bmp files

  Last modified (yy-mm-dd): 2022-08-08
--------------------------------------
'''

from re import T
from .Render import Render
from .util import color as color_b
from .Vector import V3
from .extras import paint_face
from .IO_bmp import *
from .Texture import Texture
from .Obj import Obj

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
  SR.clear()

def glCLearColor(r, g, b):
  ''' changes clear_color'''
  SR.set_clear_color(color_b(r, g, b))

def glColor(r, g, b):
  ''' changes the color for writting pixels '''
  SR.set_current_color(color_b(r, g, b))

def denormalize(x, y):
  ''' 
    Takes normalized coordinates and transforms
    them into coordinates for the framebuffer
    inside the viewport
  '''
  actual_w = v_width_d if x <= 0 else v_width_u
  actual_h = v_height_d if y <= 0 else v_height_u

  y_normal = round(actual_h * (y + 1)) + y_offset
  x_normal = round(actual_w * (x + 1)) + x_offset
  return x_normal, y_normal

def glVertex(x, y, normalized:bool=True):
  ''' writes a pixel inside the viewport '''
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
    
  SR.line(V3(x0, y0), V3(y0, y1))

# ------------ Funciones para Relleno de Poligonos ------------

def denormalize_poly(p:list[list]) -> list[list]:
  '''Denormalizes the coordinates of a polygon (array of coordinates)'''
  return [ [ *denormalize(*p[n]) ] for n in range(len(p)) ]

def perim_fig(normalized=True, *p:V3):
  ''' Draws the contorn of a polygon based a series of points '''
  if normalized: p = denormalize_poly(p)
  SR.draw_perim_fig(p)

def pintar(*p, color=[1, 1, 1], algo='triangles', normalized=True):
  ''' Fills the area of a polygon with color '''
  if normalized: p = denormalize_poly(p)
  if isinstance(color, list): color = color_b(*color)
  paint_face(SR, p, color, algo)

# ------------ Carga de modelos ------------

def wireframe_model(model_path, transform, scale, vertex_to_draw=(0, 1, 2)):
  SR.load_model(model_path, transform, scale, L=None, draw=True, vertex_to_draw=vertex_to_draw)

def load_model(model_path, transform, scale, L=(0, 0, -1), vertex_to_draw=(0, 1, 2), texture_path=0):
  SR.load_model(model_path, transform, scale, L=L, draw=False, vertex_to_draw=vertex_to_draw, texture_path=texture_path)

# ------------ Escritura de Archivos ------------

def gl_zBuffer(fileName, scale):
  ''' Writes the Z-Buffer to a bmp file '''
  z_write(fileName + '.bmp', SR.zBuffer, scale)
  print(f'-> Z-Buffer written succesfully to: {fileName}.bmp')

def glFinish(fileName):
  ''' Writes the FrameBuffer to a bmp file '''
  write_bmp(fileName + '.bmp', SR.framebuffer)
  print(f'-> FrameBuffer written succesfully to: {fileName}.bmp')

def render_img(texture, model, filename, color=(1, 1, 1)):
  T = Texture(texture)
  SR.initWindow(T.width, T.height)
  SR.initViewPort(T.width, T.height)
  SR.framebuffer = T.pixels

  cube = Obj(model)

  SR.current_color = color_b(*color)
  for face in cube.faces:
    if len(face)== 3:
      f1 = face[0][1] - 1
      f2 = face[1][1] - 1
      f3 = face[2][1] - 1

      vt1 = V3(
        cube.tverctices[f1][0] * T.width,
        cube.tverctices[f1][1] * T.height
      )
      vt2 = V3(
        cube.tverctices[f2][0] * T.width,
        cube.tverctices[f2][1] * T.height
      )
      vt3 = V3(
        cube.tverctices[f3][0] * T.width,
        cube.tverctices[f3][1] * T.height
      )

      vt1.round()
      vt2.round()
      vt3.round()

      SR.line(vt1, vt2)
      SR.line(vt2, vt3)
      SR.line(vt3, vt1)
    
    if len(face)== 4:
      f1 = face[0][1] - 1
      f2 = face[1][1] - 1
      f3 = face[2][1] - 1
      f4 = face[3][1] - 1

      vt1 = V3(
        cube.tverctices[f1][0] * T.width,
        cube.tverctices[f1][1] * T.height
      )
      vt2 = V3(
        cube.tverctices[f2][0] * T.width,
        cube.tverctices[f2][1] * T.height
      )
      vt3 = V3(
        cube.tverctices[f3][0] * T.width,
        cube.tverctices[f3][1] * T.height
      )
      vt4 = V3(
        cube.tverctices[f4][0] * T.width,
        cube.tverctices[f4][1] * T.height
      )

      vt1.round()
      vt2.round()
      vt3.round()
      vt4.round()

      SR.line(vt1, vt2)
      SR.line(vt2, vt3)
      SR.line(vt3, vt4)
      SR.line(vt4, vt1)
    
    if len(face)== 5:
      f1 = face[0][1] - 1
      f2 = face[1][1] - 1
      f3 = face[2][1] - 1
      f4 = face[3][1] - 1
      f5 = face[4][1] - 1

      vt1 = V3(
        cube.tverctices[f1][0] * T.width,
        cube.tverctices[f1][1] * T.height
      )
      vt2 = V3(
        cube.tverctices[f2][0] * T.width,
        cube.tverctices[f2][1] * T.height
      )
      vt3 = V3(
        cube.tverctices[f3][0] * T.width,
        cube.tverctices[f3][1] * T.height
      )
      vt4 = V3(
        cube.tverctices[f4][0] * T.width,
        cube.tverctices[f4][1] * T.height
      )
      vt5 = V3(
        cube.tverctices[f5][0] * T.width,
        cube.tverctices[f5][1] * T.height
      )

      vt1.round()
      vt2.round()
      vt3.round()
      vt4.round()
      vt5.round()

      SR.line(vt1, vt2)
      SR.line(vt2, vt3)
      SR.line(vt3, vt4)
      SR.line(vt4, vt5)
      SR.line(vt5, vt1)
  
  glFinish(filename)

def setBG(img_path):
  img = Texture(img_path)
  SR.framebuffer = img.pixels