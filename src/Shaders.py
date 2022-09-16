from .MStructs.Vector import V3
from .util import color
from .Render import Render

def __getIntensity(L:V3, baricentric:tuple, normals:tuple):
  w, u, v = baricentric
  nA, nB, nC = normals
  L = L.normalize()

  iA = nA.normalize() * L
  iB = nB.normalize() * L
  iC = nC.normalize() * L
  return abs(iA * w + iB * u + iC * v)
  
def gouraud(render:Render, **kwargs):
  w, u, v = kwargs['bari']
  i = __getIntensity(kwargs['light'], (w, u, v), kwargs['normals'])

  try:
    tA, tB, tC = kwargs['texture_coords']
    if render.texture:
      tx = tA.x * w + tB.x * u + tC.x * v
      ty = tA.y * w + tB.y * u + tC.y * v

      return render.texture.get_color(tx, ty, i)

  except:
    return color(
      round(255 * i),
      round(255 * i),
      round(255 * i),
      normalized=False
    )

def moon_shader(render:Render, **kwargs):
  i = __getIntensity(kwargs['light'], kwargs['bari'], kwargs['normals'])
  x, y = kwargs['coords']

  if x > 100: 
    r = 170
    g = 50
  else:
    r = 50
    g = 170
  
  if y > 100:
    b = 255
  else:
    b = 100

  return color(
    round(r * i),
    round(g * i),
    round(b * i),
    normalized=False
  )

  