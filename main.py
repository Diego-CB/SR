''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Autor: Diego Cordova
  Carne: 20212
  Last modified (yy-mm-dd): 2022-07-14
--------------------------------------
'''

from Render import Render
from util import color

# ----- Funciones

def glInit():
  global SR
  SR = Render()

def sr_isInit():
  try:
    SR.current_color
    return False

  except NameError:
    print('ERROR: Software Renderer not initialized\n\
       execute glInit before any action\n\
    ')
    return True

def glCreateWindow(width, height):
  if sr_isInit(): return
  SR.initWindow(width=width, height=height)

def glCreateViewPort(width, height):
  if sr_isInit(): return
  SR.initViewPort(width=width, height=height)

def glClear():
  if sr_isInit(): return
  SR.clear()

def glCLearColor(r, g, b):
  if sr_isInit(): return
  SR.set_clear_color(color(r, g, b))

def glColor(r, g, b):
  if sr_isInit(): return
  SR.set_current_color(color(r, g, b))

def glFinish(fileName):
  if sr_isInit(): return
  try:
    SR.write(fileName + '.bmp')
    print('File', fileName + '.bmp', 'written succesfully!!')
  except:
    print('ERROR during file writting')
  
def glVertex(x, y):
  if sr_isInit(): return
  if x < -1 or x > 1: return print('invalid coordinates:', [x, y])
  if y < -1 or y > 1: return print('invalid coordinates:', [x, y])

  v_width = SR.viewPort_w - 1
  v_height = SR.viewPort_h - 1
  x_offset = SR.x_offset
  y_offset = SR.y_offset

  x_normal = int(v_width * (x + 1)/2 + x_offset)
  y_normal = int(v_height * (y + 1)/2 + y_offset)
  
  SR.point(x_normal, y_normal)

# ----- main

glInit()

glCreateWindow(200, 200)
glCreateViewPort(180, 180)
print([SR.x_offset, SR.y_offset])

glCLearColor(0, 0, 0)
glClear()

glColor(0, 0.5, 1)

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
glVertex(-1, 1)
glVertex(1, -1)


glFinish('out')
