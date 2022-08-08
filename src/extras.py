# ---------- Drawing of Polygons
from .Render import Render
from .Vector import V3

# Algoritmo a mano
def get_x_DrawRange(SR:Render, y:int, x0:int, x1:int) -> list:
  '''
    Checks for filling area in a especific y 
    coordinate between x0 and x1 intervals
  '''
  rangos = []

  while x0 <= x1:
    actual_x = x0

    if SR.framebuffer[y][x0] == SR.current_color:
      flag = True

      while flag:
        x0 += 1

        if x0 == SR.window_w:
          flag = False
          
        elif SR.framebuffer[y][x0] != SR.current_color:
          flag = False
          rangos.append([actual_x, x0 - 1])

    x0 += 1
  
  return rangos

def get_y_DrawRange(SR:Render, x: int, y0: int, y1: int) -> list:
  '''
    Checks for filling area in a especific x
    coordinate between y0 and y1 intervals
  '''
  rango = []
  initial = -1

  for y in range(y0, y1 + 1):
    if SR.framebuffer[y][x] == SR.current_color:
      if initial == -1:
        initial = y

      else:
        if SR.framebuffer[y - 1][x] != SR.current_color:
          rango.append([initial, y])
          initial = -1
  
  return rango

def get_poly_area(p:list[list]) -> tuple[int]:
  ''' Get Area in wich a a polygon is drawed '''
  x_points:list = []
  y_points:list = []

  for n in p:
    x_points.append(n[0])
    y_points.append(n[1])

  return (
    min(x_points), max(x_points), 
    min(y_points), max(y_points)
  )

def paint_polygon(SR:Render, p:list[list], color):
  ''' Fills the area of a polygon with color '''
  
  SR.current_color = color
  SR.draw_perim_fig(p)
  min_x, max_x, min_y, max_y = get_poly_area(p)

  for y in range(min_y, max_y + 1):
    rangos_x = get_x_DrawRange(SR, y, min_x, max_x)
        
    for n in range(len(rangos_x) - 1):
      x0 = rangos_x[n][1]
      x1 = rangos_x[n + 1][0]
      x_check = x0 + round((x1 - x0) / 2)
      rangos_y = get_y_DrawRange(SR, x_check, min_y, max_y)

      for yy in rangos_y:
        if y >= yy[0] and y <= yy[1]:
          SR.line(V3(x0, y), V3(x1, y))
          break

# Algoritmo de triangulos
def triangle(SR:Render, A: V3, B: V3, C: V3, color):
  if A.y > B.y:
    A, B = B, A
  if A.y > C.y:
    A, C = C, A
  if B.y > C.y:
    B, C = C, B

  SR.current_color = color

  dx_ac = C.x - A.x
  dy_ac = C.y - A.y

  if dy_ac == 0:
    return
  
  m_ac = dx_ac / dy_ac 

  dx_ab = B.x - A.x
  dy_ab = B.y - A.y

  if dy_ab != 0:
    m_ab = dx_ab / dy_ab
    for y in range(A.y, B.y):
      xi = round(A.x - m_ac * (A.y - y))
      xf = round(A.x - m_ab * (A.y - y))

      if xi > xf:
        xi, xf = xf, xi

      for x in range(xi, xf):
        SR.point(x, y)
  
  dx_bc = C.x - B.x
  dy_bc = C.y - B.y

  if dy_bc != 0:
    m_bc = dx_bc / dy_bc

    
    for y in range(B.y, C.y):
      xi = round(A.x - m_ac * (A.y - y))
      xf = round(B.x - m_bc * (B.y - y))

      if xi > xf:
        xi, xf = xf, xi

      for x in range(xi, xf + 1):
        SR.point(x, y)

def paint_face(SR:Render, p:list[list], color, algo):
  if algo == 'triangles':
    triangle(SR, V3(*p[0]), V3(*p[1]), V3(*p[1]), color)
  elif algo == 'polygon':
    paint_polygon(SR, p, color)
  
