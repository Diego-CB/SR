''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Autor: Diego Cordova
  Carne: 20212
  Last modified (yy-mm-dd): 2022-07-15
--------------------------------------
'''

from util import *

class Render(object):
  def __init__(self):
    # Atributos
    self.window_w = 0
    self.window_h = 0
    self.viewPort_w = 0
    self.viewPort_h = 0
    self.framebuffer = []

    self.current_color = color(1, 1, 1)
    self.clear_color = color(0, 0, 0)

  def initWindow(self, width, height):
    self.window_w = width
    self.window_h = height

    self.framebuffer = [
      [self.clear_color for x in range(self.window_w)]
      for y in range(self.window_h)
    ]

  def initViewPort(self, width, height):
    self.viewPort_w = width
    self.viewPort_h = height
    self.x_offset = (self.window_w - width) / 2
    self.y_offset = (self.window_h - height) / 2

  def clear(self):
    self.framebuffer = [
      [self.clear_color for x in range(self.window_w)]
      for y in range(self.window_h)
    ]

  def set_clear_color(self, clear_color):
    self.clear_color = clear_color
  
  def set_current_color(self, current_color):
    self.current_color = current_color

  def __pixel_header(self, f):

    # pixel Header
    f.write(char('B'))
    f.write(char('M'))

    # File size (4 bytes)
    f.write(dword(
      14 + 40 + self.window_w * self.window_h * 3
    ))

    # 2 words de 2 bytes
    f.write(word(0))
    f.write(word(0))

    f.write(dword(14 + 40))

    f.write(dword(40))
    f.write(dword(self.window_w))
    f.write(dword(self.window_h))
    f.write(word(1))
    f.write(word(24))
    f.write(dword(0))
    f.write(dword(self.window_w * self.window_h * 3))
    
    f.write(word(0))
    f.write(word(0))
    f.write(word(0))
    f.write(word(0))

  def write(self, filename):
    f = open(filename, 'bw')
    self.__pixel_header(f)

    for x in range(self.window_w):
      for y in range(self.window_h):
        f.write(self.framebuffer[y][x])

    f.close

  def point(self, x, y):
    self.framebuffer[y][x] = self.current_color
