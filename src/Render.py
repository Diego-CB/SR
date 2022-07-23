''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  Render.py (Object)
  - Object used to render a bmp image

  Last modified (yy-mm-dd): 2022-07-17
--------------------------------------
'''

from .util import *

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
    self.x_offset = (self.window_w - width) / 2
    self.y_offset = (self.window_h - height) / 2

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
    self.framebuffer[y][x] = self.current_color

  def line(self, x1, y1, x2, y2):

    dy = abs(y2 - y1)
    dx = abs(x2 - x1)
 
    steep = dy > dx
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dy = abs(y2 - y1)
    dx = abs(x2 - x1)

    offset = 0 * 2 * dx
    threshold = 0.5 * 2 * dx

    y = y1
    points = []

    for x in range(x1, x2 + 1):
        if steep:
            points.append((y, x))
        else:
            points.append((x, y))
        
        offset += dy * 2
        if offset >= threshold:
            y += 1 if y1 < y2 else -1
            threshold += 1 * 2 * dx

    for point in points:
        self.point(*point)
