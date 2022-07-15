''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Autor: Diego Cordova
  Carne: 20212
  Last modified (yy-mm-dd): 2022-07-15
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
  if r < 0 or r > 1: return print('invalid color:', [r, g, b])
  if g < 0 or b > 1: return print('invalid color:', [r, g, b])
  if g < 0 or b > 1: return print('invalid color:', [r, g, b])

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
    self.x_offset = (SR.window_w - SR.viewPort_w) / 2
    self.y_offset = (SR.window_h - SR.viewPort_h) / 2

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

# ----- Funciones

def glInit():
  global SR
  SR = Render()

def sr():
  try:
    SR.current_color
    return False

  except NameError:
    print('ERROR: Software Renderer not initialized\n\
       execute glInit before any action\n\
    ')
    return True

def glCreateWindow(width, height):
  if sr(): return
  SR.initWindow(width=width, height=height)

def glCreateViewPort(width, height):
  if sr(): return
  SR.initViewPort(width=width, height=height)

def glClear():
  if sr(): return
  SR.clear()

def glCLearColor(r, g, b):
  if sr(): return
  SR.set_clear_color(color(r, g, b))

def glColor(r, g, b):
  if sr(): return
  SR.set_current_color(color(r, g, b))

def glFinish(fileName):
  if sr(): return
  try:
    SR.write(fileName + '.bmp')
    print('File', fileName + '.bmp', 'written succesfully!!')
  except:
    print('ERROR during file writting')
  
def glVertex(x, y):
  if sr(): return
  if x < -1 or x > 1: return print('invalid coordinates:', [x, y])
  if y < -1 or y > 1: return print('invalid coordinates:', [x, y])

  v_width = SR.viewPort_w - 1
  v_height = SR.viewPort_h - 1
  x_offset = SR.x_offset
  y_offset = SR.y_offset

  x_normal = int(v_width * (x + 1)/2 + x_offset)
  y_normal = int(v_height * (y + 1)/2 + y_offset)
  
  #print([x, y])
  #print(x_normal, y_normal)
  SR.point(x_normal, y_normal)

def vfb():
  fb:list[list] = SR.framebuffer
  for row in fb:
    rep = []
    for e in row:
      color = 'x' if e == b'\xff\xff\xff' else 'p'
      rep.append(color)
    print(rep)

# ----- main

glInit()

glCreateWindow(1000, 1000)
glCreateViewPort(100, 100)

glCLearColor(0, 0, 0)
glClear()

glColor(0, 1, 1)

x, y = -1, -1
while y <= 1:
  x = -1
  while x <= 1:
    glVertex(x, y)
    x += .004008

  y += .004008

glColor(1, 0, 0)
glVertex(0, 0)
glVertex(1, 1)
glVertex(-1, -1)


glFinish('out')
