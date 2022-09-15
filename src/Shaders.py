from .util import color
from .Render import Render

def gouraud(render:Render, **kwargs):
  w, u, v = kwargs['bari']
  L = kwargs['light'].normalize()  
  nA, nB, nC = kwargs['normals']
  
  iA = nA.normalize() * L
  iB = nB.normalize() * L
  iC = nC.normalize() * L
  i = abs(iA * w + iB * u + iC * v)
  
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
