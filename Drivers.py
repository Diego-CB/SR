from src.gl import *

def __paintModel(model, texture, W, transform, scale, v_to_draw, L):
  print('\nRenderizando:', model, '\nCon texturas:', texture)
  __Init(W)

  load_model(
    model, transform, scale, L=L, 
    vertex_to_draw=v_to_draw , texture_path=texture
  )

  # File Writing
  glFinish('./renders/Mario')


def __Init(size):
  # Initalization
  glInit()
  x, y = size if type(size) in [tuple, list] else size, size

  # Viewport and window initialization
  glCreateWindow  (x, y)
  glCreateViewPort(x, y)

def Mario():
  model = './models/Mario/Mario.obj'
  texture = './models/Mario/Mario.bmp'
  print('\nRenderizando:', model, '\nCon texturas:', texture)

  W = 1024
  __Init(W)
  # --- Mario ---

  # Obj Model Drawing
  transform = (
    round(W / 2),
    round(W / 2),
    round(W * 2)
  )

  scale = (
    round(W / 2.8),
    round(W / 2.8), 
    round(W / 4)
  )

  v_to_draw = (2, 0, 1) # z, x, y
  LIGHT = (15, 30, -100)
  LIGHT = (-15, 10, -100)

  load_model(
    model, transform, scale, L=LIGHT, 
    vertex_to_draw=v_to_draw , texture_path=texture
  )

  # File Writing
  glFinish('./renders/Mario')

def Tmap_Mario():
  glInit()
  model = './models/Mario/Mario.obj'
  texture = './models/Mario/Mario.bmp'
  
  render_img(
    texture, model, './renders/Mario_texture', 
    color=(0, 0.6, 0)
  )

def Yoshi():
  model = './models/Yoshi/Yoshi.obj'
  texture = './models/Yoshi/Yoshi.bmp'
  print('\nRenderizando:', model, '\nCon texturas:', texture)
  
  # Initalization
  glInit()

  # Viewport and window initialization
  W = 1024
  glCreateWindow  (W, W)
  glCreateViewPort(W, W)

  # --- Mario ---

  # Obj Model Drawing
  transform = (
    round(W),
    round(W / 2),
    round(W * 2)
  )

  scale = (
    round(W / 2.8),
    round(W / 2.8), 
    round(W / 4)
  )


  v_to_draw = (2, 0, 1) # z, x, y
  LIGHT = (0, 0, -100)

  load_model(
    model, transform, scale, L=LIGHT, 
    vertex_to_draw=v_to_draw , texture_path=texture
  )

  # File Writing
  glFinish('./renders/Yoshi')


def Tmap_Yoshi():
  glInit()

  model = './models/Yoshi/Yoshi.obj'
  texture = './models/Yoshi/Yoshi.bmp'

  render_img(
    texture, model, './renders/Yoshi_texture', 
    color=(0, 0, 0.6)
  )

def Face():
  model = './models/Face/face.obj'
  texture = './models/Face/model.bmp'
  print('\nRenderizando:', model, '\nCon texturas:', texture)
  
  # Initalization
  glInit()

  # Viewport and window initialization
  W = 1024
  glCreateWindow  (W, W)
  glCreateViewPort(W, W)

  # --- Mario ---

  # Obj Model Drawing
  transform = (
    round(W / 2),
    round(W / 2),
    round(W * 2)
  )

  scale = (
    round(W / 2.1),
    round(W / 2.1), 
    round(W / 4)
  )


  v_to_draw = (0, 1, 2) # z, x, y
  LIGHT = (0, 0, -100)

  load_model(
    model, transform, scale, L=LIGHT, 
    vertex_to_draw=v_to_draw , texture_path=texture
  )

  # File Writing
  glFinish('./renders/Face')

def Tmap_Face():
  glInit()

  model = './models/Face/face.obj'
  texture = './models/Face/model.bmp'
  render_img(texture, model, './renders/Face_texture')