''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  Render.py (Object)
  - Object used to render a bmp image

  Last modified (yy-mm-dd): 2022-08-08
--------------------------------------
'''

# TODO: quitar

from numpy import *

# TODO: quitar


from math import cos, sin
from .Texture import Texture
from .util import *
from .Obj import Obj
from .Vector import *
from .Matrix import *

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
    self.Model = None

  # Matrix transformaions

  def __transform_vertex(self, vertex):
    '''Returns the coordinates of a vertex centered to the screen'''
    augmented_vertex = V4([*vertex, 1])

    transformed_vertex = (
      self.viewport
      @ self.projection
      @ self.Model
      @ augmented_vertex
      @ self.viewMatrix
    )
    
    transformed_vertex = transformed_vertex.matrix[0]

    return V3(
      transformed_vertex[0] / transformed_vertex[3],
      transformed_vertex[1] / transformed_vertex[3],
      transformed_vertex[2] / transformed_vertex[3]
    )

  def loadModelMatrix(self, translate, scale, rotate):
    translate=V3(*translate)
    scale=V3(*scale)
    rotate=V3(*rotate)

    translation_matrix = M4([
      [1, 0, 0, translate.x],
      [0, 1, 0, translate.y],
      [0, 0, 1, translate.z],
      [0, 0, 0, 1],
    ])

    scale_matrix = M4([
      [scale.x, 0, 0, 0],
      [0, scale.y, 0, 0],
      [0, 0, scale.z, 0],
      [0, 0, 0, 1],
    ])

    a = rotate.x
    rotation_x = M4([
      [1,      0,       0, 0],
      [0, cos(a), -sin(a), 0],
      [0, sin(a),  cos(a), 0],
      [0,      0,       0, 1],
    ])

    a = rotate.y
    rotation_y = M4([
      [cos(a) , 0, sin(a), 0],
      [0      ,      1, 0, 0],
      [-sin(a), 0, cos(a), 0],
      [0      ,      0, 0, 1],
    ])

    a = rotate.z
    rotation_z = M4([
      [cos(a), -sin(a), 0, 0],
      [sin(a), cos(a) , 0, 0],
      [0     , 0      , 1, 0],
      [0     , 0      , 0, 1],
    ])

    rotation_matrix = rotation_x @ rotation_y @ rotation_z
    self.Model = translation_matrix @ rotation_matrix @ scale_matrix

  def loadViewMatrix(self, x:V3, y:V3, z:V3, center:V3):
    # (x, y, z) = eye
    Mi = M4([
      [x.x, x.y, x.z, 0],
      [y.x, y.y, y.z, 0],
      [z.x, z.y, z.z, 0],
      [0  ,   0,   0, 1],
    ])

    Op = M4([
      [1, 0, 0, -center.x],
      [0, 1, 0, -center.y],
      [0, 0, 1, -center.z],
      [0, 0, 0,         1],
    ])

    self.viewMatrix = Mi @ Op
  
  def loadProjectionMatrix(self, coeff):
    # (x, y, z) = eye
    c = coeff
    self.projection = M4([
      [1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, c, 1]
    ])
  
  def loadViewportMatrix(self):
    x = 0
    y = 0
    w = self.window_w / 2
    h = self.window_h / 2

    self.viewport = M4([
      [w, 0, 0, x + w],
      [0, h, 0, y + h],
      [0, 0, 128, 128],
      [0, 0, 0, 1]
    ])

  def lookAt(self, eye: V3, center:V3, up:V3, coeff):
    z = (eye - center).normalize()
    x = (up @ z).normalize()
    y = (z @ x).normalize()

    self.loadProjectionMatrix(coeff)
    self.loadViewMatrix(x, y, z, center)
    self.loadViewportMatrix()
    
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

  # Functionality
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

  def load_model(
    self, model_path, 
    draw, L,
    translate=(0, 0, 0),
    scale    =(1, 1, 1),
    rotate   =(0, 0, 0),
    texture_path = None
  ):
    self.loadModelMatrix(translate, scale, rotate)
    model = Obj(model_path)
    ''' Reads an obj file and draws a wireframe of it in the viewport '''

    if texture_path: self.texture = Texture(texture_path)

    for face in model.faces:
      face_vertex = []
      text_vertex = []

      for actual_v in face:
        temp = model.vertices[actual_v[0] - 1]
        temp = self.__transform_vertex(temp)
        face_vertex.append(temp)

        if isinstance(self.texture, Texture):
          temp_texture = V3(*model.tverctices[actual_v[1] - 1])
          text_vertex.append(temp_texture)

      if draw:
        self.draw_perim_fig(face_vertex)
      else:
        self.poly_triangle(face_vertex, text_vertex, L)

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
    
    if abs(cz) <= 0: return -1, -1, -1
    
    v = cy / cz
    u = cx / cz
    w = 1 - (cx + cy) / cz
    
    return w, v, u
    
  def triangle(
    self, vertices:list[V3], L:tuple, t_vertices:list[V3] = (),
    paint_color = [255, 255, 255]
  ):
    A, B, C = vertices
    L = V3(*L)
    N = (C - A) @ (B - A)
    i = L.normalize() * N.normalize()
    i = round(i, 6)

    if i < 0: return

    if self.texture:
      tA, tB, tC = t_vertices

    else:
      self.current_color = color(
        round(paint_color[0] * i),
        round(paint_color[1] * i),
        round(paint_color[2] * i),
        normalized=False
      )

    Min, Max = self.bounding_box(A, B, C)

    for x in range(Min.x, Max.x + 1):
      for y in range(Min.y, Max.y + 1):
        if x > len(self.zBuffer[0]) - 1 or y > len(self.zBuffer) - 1: continue
        if x < 0 or y < 0: continue

        w, v, u = self.barycentric(A, B, C, V3(x, y))
        if w < 0 or v < 0 or u < 0: continue
        z = A.z * w + B.z * v + C.z * u

        if self.zBuffer[y][x] < z:
          self.zBuffer[y][x] = z

          if self.texture:
            tx = tA.x * w + tB.x * u + tC.x * v
            ty = tA.y * w + tB.y * u + tC.y * v
            self.current_color = self.texture.get_color(tx, ty, i)
            
          self.point(x, y)

  def poly_triangle(self, face:list[V3], text:list[V3], L:tuple):
    if len(face) < 3: raise Exception('Invalid Polygon:', face)

    for v in range(len(face) - 2):
      vertex = (face[0], face[v+1], face[v+2])

      if not self.texture:
        self.triangle(vertex, L)
      else:
        textures = (text[0], text[v+1], text[v+2])
        self.triangle(vertex, L, textures)
