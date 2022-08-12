

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
        self.pixels[y].append(
          color(r, g, b, normalized=False)
        )

    img.close()
      
  
  def get_color(self, tx, ty, intensity=1):
    x = round(tx * self.width)
    y = round(ty * self.height)

    if y > 0: y = y - 1
    if x > 0: x = x - 1

    py = self.pixels[y]
    px = py[x]
    intensity = 1

    b = round(px[0] * intensity)
    g = round(px[1] * intensity)
    r = round(px[2] * intensity)

    return color(r, g, b, normalized=False)
