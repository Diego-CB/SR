

from .util import *
import struct

class Texture:
  def __init__(self, path):
    self.path = path
    self.read()

  def read(self):
    img = open(self.path, 'rb')
    img.seek(2 + 4 + 4)
    header_size = struct.unpack('=l', img.read(4))[0]
    
    img.seek(2 + 4 + 4 + 4 + 4)
    self.width = struct.unpack('=l', img.read(4))[0]
    self.height = struct.unpack('=l', img.read(4))[0]

    img.seek(header_size)

    self.pixels = []

    for y in range(self.height):
      self.pixels.append([])
      for x in range(self.width):
        b = ord(img.read(1))
        g = ord(img.read(1))
        r = ord(img.read(1))
        
        actual_color = color(r, g, b, normalized=False)
        self.pixels[y].append(actual_color)

    img.close()
      
  def get_color(self, tx, ty, intensity=1):
    x = round(tx * self.width) - 1
    y = round(ty * self.height) - 1

    try:
      p = self.pixels[y][x]
      b = round(p[0] * intensity)
      g = round(p[1] * intensity)
      r = round(p[2] * intensity)

      return color(r, g, b, normalized=False)
    except:
      print('x, y = ',[x, y])
