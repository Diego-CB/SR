''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  main.py
  - main program to write files
  
  Last modified (yy-mm-dd): 2022-07-17
--------------------------------------
'''

from src.gl import *

def square_param(limit = 1):
  ''' Draws an squere parameter in the viewport '''
  limit_d = limit * -1

  for i in range(2):
    x = limit_d

    while x <= limit:
      y = limit_d

      while y <= limit:
        if i == 0:
          glVertex(x, y)
        else:
          glVertex(y, x)

        y += 0.001
      
      x += limit * 2

# ----- main

glInit() # Initalization

# Viewport and window initialization
glCreateWindow(1700, 2000)
glCreateViewPort(900, 1500)

# Clear of the window
glCLearColor(0, 0, 0)
glClear()

# Squares draw
glColor(1, 0, 0)
limit = 501
ls = [x/limit for x in range(1, limit)]
for i in ls:
  square_param(i)

# File writting (rendering)
glFinish('out')
