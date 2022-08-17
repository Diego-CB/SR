''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  Render.py (Object)
  - Object used to render a bmp image

  Last modified (yy-mm-dd): 2022-08-08
--------------------------------------
'''

from .util import *
from .Obj import Obj
from .Vector import *
import copy

from random import randint

class Render(object):
  '''
    Renderer for BMP images

    Atributes
    ---------
    window_w: width of window (file)
    window_h: height of window (file)
    viewPort_w: width of viewport
    viewPort_h: height of viewport
    framebuffer: pixel framebuffer
    current_color: Selected color to print pixels
    clear_color: color to clear image
  '''
  def __init__(self):
    self.current_color = color(1, 1, 1)
    self.clear_color = color(0, 0, 0)
    self.texture = None

  def initWindow(self, width, height):
    '''
      Initialize window and framebuffer 
      with specified dimensions
    '''
    self.window_w = width
    self.window_h = height

    self.framebuffer = [
      [self.clear_color for y in range(self.window_h)]
      for x in range(self.window_w)
    ]
    
    self.zBuffer = [
      [-9999 for y in range(self.window_h)]
      for x in range(self.window_w)
    ]

  def initViewPort(self, width, height):
    '''
      Initialize viewport and
      calculate x and y offsets
    '''

    self.viewPort_w = width
    self.viewPort_h = height

  def clear(self):
    ''' Fills framebuffer with the actual clear_color'''

    self.framebuffer = [
      [self.clear_color for x in range(self.window_w)]
      for y in range(self.window_h)
    ]

  def set_clear_color(self, clear_color):
    ''' Sets clear_color '''
    self.clear_color = clear_color
  
  def set_current_color(self, current_color):
    ''' Sets current_color '''
    self.current_color = current_color

  def __pixel_header(self, f):
    ''' Writes Pixel Header for the file f'''

    # -------- File header --------
    
    # BM
    f.write(char('B'))
    f.write(char('M'))

    # Tamano del file Header + Tamano del Image Header + tamano de la imagen
    f.write(dword(14 + 40 + self.window_w * self.window_h * 3))
    
    f.write(dword(0)) # 4 bytes vacios (dword)
    f.write(dword(14 + 40)) # Tamano del file Header + Tamano del Image Header

    # -------- Image header --------
    
    f.write(dword(40)) # Tamano del Image Header
    f.write(dword(self.window_w)) # Ancho de la imagen
    f.write(dword(self.window_h)) # Largo de la imagen
    f.write(word(1)) # un word con un 1 (2 bytes)
    f.write(word(24)) # un word con un 24 (2 bytes)
    f.write(dword(0)) # 4 bytes vacios (dword)
    f.write(dword(self.window_w * self.window_h * 3)) # tamano de la imagen
    
    # 4 dwords vacios: 4*4 bytes
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))

  def write(self, filename):
    '''
      Writes a bmp file with the 
      color information contained
      in the framebuffer
    '''
    f = open(filename, 'bw')
    self.__pixel_header(f)

    for y in range(self.window_h):
      for x in range(self.window_w):
        f.write(self.framebuffer[y][x])

    f.close

  def point(self, x, y):
    ''' Change the color of a pixel in the framebuffer '''
    if 0 <= x < self.window_w and 0 <= y < self.window_h:
      self.framebuffer[y][x] = self.current_color

  def line(self, v1:V3, v2:V3):
    '''
      Draws a line of pixels from point
      [x0, y0] to [x1, y1] on the viewport
    '''
    x0, y0 = v1.x, v1.y
    x1, y1 = v2.x, v2.y

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
      self.point(*actual_pixel)

      if augment > round_limit:
        y += 1 if y0 < y1 else -1
        round_limit += 2 * dx

  # ---------- Drawing of models
  
  def draw_perim_fig(self, p:list[V3]):
    for n in range(0, len(p)):
      x0 = p[n].x
      y0 = p[n].y
      x1, y1 = 0, 0

      if n < len(p) - 1:
        x1 = p[n+1].x
        y1 = p[n+1].y

      else:
        x1 = p[0].x
        y1 = p[0].y

      self.line(V3(x0, y0), V3(x1, y1))

  def __transform_vertex(self, vertex, translate, scale, vertex_to_draw=(0, 1, 2)):
    '''Returns the coordinates of a vertex centered to the screen'''
    return V3(
      round(vertex[vertex_to_draw[0]] * scale[0]) + translate[0],
      round(vertex[vertex_to_draw[1]] * scale[1]) + translate[1],
      round(vertex[vertex_to_draw[2]] * scale[2]) + translate[2]
    )

  def load_model(
    self, model_path, transform, 
    scale, draw, L, vertex_to_draw
  ):
    ''' Reads an obj file and draws a wireframe of it in the viewport '''
    model = Obj(model_path)

    for face in model.faces:
      face_vertex = []

      for actual_v in face:
        temp = model.vertices[actual_v[0] - 1]
        temp = self.__transform_vertex(temp, transform, scale, vertex_to_draw)
        face_vertex.append(temp)

      if draw:
        self.draw_perim_fig(face_vertex)
      else:
        self.poly_triangle(face_vertex, L)

  # Triangles

  def bounding_box(self, *polygon:V3) -> tuple[V3]:
    x = [ vertex.x for vertex in polygon ]
    y = [ vertex.y for vertex in polygon ]
    z = [ vertex.z for vertex in polygon ]

    Min = V3(min(x), min(y), min(z))
    Max = V3(max(x), max(y), max(z))
    Min.round()
    Max.round()

    return Min, Max

  def barycentric(self, A:V3, B:V3, C:V3, P:V3):
    cx, cy, cz = cross(
      V3(B.x - A.x, C.x - A.x, A.x - P.x),
      V3(B.y - A.y, C.y - A.y, A.y - P.y)
    )
    
    if abs(cz) < 1: return -1, -1, -1
    
    w = 1 - (cx + cy) / cz
    v = cy / cz
    u = cx / cz
    
    return w, v, u
    
  def triangle(self, A:V3, B:V3, C:V3, L:tuple, paint_color=[255, 255, 255]):
    L = V3(*L)
    N = (C - A) @ (B - A)
    i = L.normalize() * N.normalize()
    i = round(i, 6)

    if i < 0: return

    self.current_color = color(
      round(paint_color[0] * i),
      round(paint_color[1] * i),
      round(paint_color[2] * i),
      normalized=False
    )

    Min, Max = self.bounding_box(A, B, C)

    for x in range(Min.x, Max.x + 1):
      for y in range(Min.y, Max.y + 1):
        w, v, u = self.barycentric(A, B, C, V3(x, y))

        if w < 0 or v < 0 or u < 0: continue
        z = A.z * w + B.z * v + C.z * u

        if self.zBuffer[y][x] < z:
          self.zBuffer[y][x] = z
          self.point(x, y)

  def poly_triangle(self, face:list[V3], L:tuple):
    if len(face) < 3: raise Exception('Invalid Polygon:', face)
    if len(face) == 3: return self.triangle(*face, L)
    
    if len(face) > 4: return

    A, B, C, D = face
    self.triangle(A, B, C, L)
    self.triangle(A, C, D, L)


  def z_write(self, filename, scale):
    '''
      Writes a bmp file with the 
      color information contained
      in the zBuffer
    '''
    f = open(filename, 'bw')
    self.__pixel_header(f)

    for y in range(self.window_h):
      for x in range(self.window_w):
        z = self.zBuffer[y][x]
        z = 0 if z < 0 else z
        z = z / (scale * 3)
        z = 1 if z > 1 else z
        z_color = color(z, z, z)
        f.write(z_color)

    f.close
