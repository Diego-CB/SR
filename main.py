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

# ----- main

glInit() # Initalization

# Viewport and window initialization
glCreateWindow(1080, 1080)
glCreateViewPort(1000, 1000)

# Clear of the window
glCLearColor(0, 0, 0)
glClear()


# Squares draw
limit = 505
ls = [x/limit for x in range(1, limit)]
for i in ls:
  square_perim(i)

square_perim(1)

glVertex(0, 0)

glColor(0, 0, 1)

  
#glLine(-1, 0, 1, 0)
#glLine(0, -1, 0, 1)
#glLine(-1, -1, 1, 1)
#glLine(-1, 1, 1, -1)

# File writting (rendering)
glFinish('out')
