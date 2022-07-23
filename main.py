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
glCreateWindow(800, 1000)
glCreateViewPort(650, 850)

# Clear of the window
glCLearColor(0, 0, 0)
glClear()

glColor(1, 0, 0)

# Squares draw
limit = 121
ls = [x/limit for x in range(1, limit)]
for i in ls:
  square_perim(i)

# File writting (rendering)
glFinish('out')
