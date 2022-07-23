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
glCreateWindow(1200, 1200)
glCreateViewPort(600, 600)

# Clear of the window
glCLearColor(0, 0, 0)
glClear()

filled_square()

# File writting (rendering)
glFinish('out')
