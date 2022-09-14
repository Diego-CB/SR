from .util import color
from .Render import Render

def shader(render:Render, **kwargs):
  w, u, v = kwargs['bari']
  L = kwargs['light']
  tA, tB, tC = kwargs['texture_coords']
  nA, nB, nC = kwargs['normals']

  iA = nA.normalize() * L.normalize()
  iB = nB.normalize() * L.normalize()
  iC = nC.normalize() * L.normalize()
  i = iA * w + iB * u + iC * v
  i = iA
  if i < 0: return color(1, 0, 0)

  if render.texture:
    tx = tA.x * w + tB.x * u + tC.x * v
    ty = tA.y * w + tB.y * u + tC.y * v

    return render.texture.get_color(tx, ty, i)