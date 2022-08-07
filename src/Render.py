''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  Render.py (Object)
  - Object used to render a bmp image

  Last modified (yy-mm-dd): 2022-07-31
--------------------------------------
'''

from .util import *
from .Obj import Obj
from .Vector import V3

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
    if 0 < x < self.window_w and 0 < y < self.window_h:
      self.framebuffer[y][x] = self.current_color

  def line(self, v1, v2):
    '''
      Draws a line of pixels from point
      [x0, y0] to [x1, y1] on the viewport
    '''
    x0, y0 = v1[0], v1[1]
    x1, y1 = v2[0], v2[1]

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

  # ---------- Drawing of Polygons

  def draw_perim_fig(self, p:list[list]):
    ''' Draws the contorn of a polygon based a series of points '''

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

      self.line(x0, y0, x1, y1)

  def get_x_DrawRange(self, y:int, x0:int, x1:int) -> list:
    '''
      Checks for filling area in a especific y 
      coordinate between x0 and x1 intervals
    '''
    rangos = []

    while x0 <= x1:
      actual_x = x0

      if self.framebuffer[y][x0] == self.current_color:
        flag = True

        while flag:
          x0 += 1

          if x0 == self.window_w:
            flag = False
            
          elif self.framebuffer[y][x0] != self.current_color:
            flag = False
            rangos.append([actual_x, x0 - 1])

      x0 += 1
    
    return rangos

  def get_y_DrawRange(self, x: int, y0: int, y1: int) -> list:
    '''
      Checks for filling area in a especific x
      coordinate between y0 and y1 intervals
    '''
    rango = []
    initial = -1

    for y in range(y0, y1 + 1):
      if self.framebuffer[y][x] == self.current_color:
        if initial == -1:
          initial = y

        else:
          if self.framebuffer[y - 1][x] != self.current_color:
            rango.append([initial, y])
            initial = -1
    
    return rango

  def __get_poly_area(self, p:list[list]) -> int:
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

  def paint_face(self, p:list[list]):
    ''' Fills the area of a polygon with color '''
    
    self.draw_perim_fig(p)
    min_x, max_x, min_y, max_y = self.__get_poly_area(p)

    for y in range(min_y, max_y + 1):
      rangos_x = self.get_x_DrawRange(y, min_x, max_x)
          
      for n in range(len(rangos_x) - 1):
        x0 = rangos_x[n][1]
        x1 = rangos_x[n + 1][0]
        x_check = x0 + round((x1 - x0) / 2)
        rangos_y = self.get_y_DrawRange(x_check, min_y, max_y)

        for yy in rangos_y:
          if y >= yy[0] and y <= yy[1]:
            self.line(x0, y, x1, y)
            break

  # ---------- Drawing of models
  
  def __transform_vertex(self, vertex, translate, scale, vertex_to_draw):
    '''Returns the coordinates of a vertex centered to the screen'''
    return V3(
      round(vertex[0] * scale[0]) + translate[0],
      round(vertex[1] * scale[1]) + translate[1],
      round(vertex[2] * scale[2]) + translate[2]
    )

  def wireframe_model(
    self, model_path, transform, 
    scale, vertex_to_draw, option
  ):
    ''' Reads an obj file and draws a wireframe of it in the viewport '''
    model = Obj(model_path)

    for face in model.faces:
      face_vertex = []

      for actual_v in face:
        temp = model.vertices[actual_v[0] - 1]
        temp = self.__transform_vertex(temp, transform, scale, vertex_to_draw)
        face_vertex.append(temp)

      if option == 'draw':
        self.draw_perim_fig(face_vertex)
      elif option == 'paint':
        self.paint_face(face_vertex)

  # Triangules

  def triangle(self, A: V3, B: V3, C: V3, color):
    if A.y > B.y:
      A, B = B, A
    if A.y > C.y:
      A, C = C, A
    if B.y > C.y:
      B, C = C, B

    self.current_color = color

    dx_ac = C.x - A.x
    dy_ac = C.y - A.y

    if dy_ac == 0:
      return
    
    m_ac = dx_ac / dy_ac 

    dx_ab = B.x - A.x
    dy_ab = B.y - A.y

    if dy_ab != 0:
      m_ab = dx_ab / dy_ab
      for y in range(A.y, B.y):
        xi = round(A.x - m_ac * (A.y - y))
        xf = round(A.x - m_ab * (A.y - y))

        if xi > xf:
          xi, xf = xf, xi

        for x in range(xi, xf):
          self.point(x, y)
    
    dx_bc = C.x - B.x
    dy_bc = C.y - B.y

    if dy_bc != 0:
      m_bc = dx_bc / dy_bc

      
      for y in range(B.y, C.y):
        xi = round(A.x - m_ac * (A.y - y))
        xf = round(A.x - m_bc * (B.y - y))

        if xi > xf:
          xi, xf = xf, xi

        for x in range(xi, xf):
          self.point(x, y)

  def bounding_box(self, A:V3, B:V3, C:V3):
    xs = [A.x, B.x, C.x]
    ys = [A.y, B.y, C.y]
    zs = [A.z, B.z, C.z]

    return (
      V3(min(xs), min(ys), min(zs)),
      V3(max(xs), max(ys), max(zs))
    )
