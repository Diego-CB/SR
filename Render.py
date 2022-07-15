''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Autor: Diego Cordova
  Carne: 20212
  Last modified (yy-mm-dd): 2022-07-14
--------------------------------------
'''

import struct

def char(c):
  return struct.pack('=c', c.encode('ascii'))
  #1 byte

def word(w):
  return struct.pack('=h', w)
  # 2 bytes

def dword(d):
  return struct.pack('=l', d)
  # 4 bytes

def color(r, g, b):
  r *= 255
  g *= 255
  b *= 255
  return bytes([g, r, b])

class Render(object):
  def __init__(self):
    # Atributos
    self.window_w = 0
    self.window_h = 0
    self.viewPort_w = 0
    self.viewPort_h = 0

    self.current_color = color(1, 1, 1)
    self.clear_color = color(0, 0, 0)
    self.framebuffer = []

  def initWindow(self, width, height):
    self.window_w = width
    self.window_h = height

  def initViewPort(self, width, height):
    self.viewPort_w = width
    self.viewPort_h = height

  def clear(self):
    self.framebuffer = [
      [self.clear_color for x in range(self.window_w)]
      for y in range(self.window_h)
    ]

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
        f.write(self.framebuffer[x][y])

    f.close

  def point(self, x, y):
    self.framebuffer[y][x] = self.current_color

# ----- Main

r = Render()
r.initViewPort(10, 10)
r.initWindow(10, 10)
r.current_color = color(0, 1, 0)
r.point(5, 5)

r.current_color = color(0, 0, 1)

for x in range(1, 2):
  for y in range(1, 2):
    r.point(x, y)

r.write('a.bmp')