''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  Shaders.py
  - implementation of shaders

  Last modified (yy-mm-dd): 2022-09-17
--------------------------------------
'''

from .MStructs.Vector import V3
from .util import color
from .Render import Render
from math import sqrt

def __getIntensity(L:V3, baricentric:tuple, normals:tuple):
  '''Intensity of light (for gouraud algorithm)'''
  w, u, v = baricentric
  nA, nB, nC = normals
  L = L.normalize()

  iA = nA.normalize() * L
  iB = nB.normalize() * L
  iC = nC.normalize() * L
  return iA * w + iB * u + iC * v

def gouraud(render:Render, **kwargs):
  '''Implementation of gouraud algorithm (shader)'''
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
      max(min(round(255 * i), 255), 0),
      max(min(round(255 * i), 255), 0),
      max(min(round(255 * i), 255), 0),
      normalized=False
    )

def astronaut(render:Render, **kwargs):
  w, u, v = kwargs['bari']
  i = __getIntensity(kwargs['light'], (w, u, v), kwargs['normals'])

  tA, tB, tC = kwargs['texture_coords']
  tx = tA.x * w + tB.x * u + tC.x * v
  ty = tA.y * w + tB.y * u + tC.y * v

  r, g, b = render.texture.get_color_astronaut(tx, ty, i)

  return color(
    r if r > 0 else 200,
    g if g > 0 else 200,
    b if b > 0 else 200,
    normalized=False
  )
  
def satelite(render:Render, **kwargs):
  x, y = kwargs['coords']
  if x % 3 == 0 and y % 3 == 0: return color(1, 1, 1)

  i = __getIntensity(kwargs['light'], kwargs['bari'], kwargs['normals'])
  r = max(min(round(255 * i), 255), 0)
  g = max(min(round(255 * i), 255), 0)
  b = max(min(round(255 * i), 255), 0)

  r += 100 if r < 155 else 0
  g += 50 if g < 150 else -25
  b = 180 if b < 50 else b

  return color(r, g, b, normalized=False)

def isPrime(x):
  return (
    (x % 5 == 0)
    or (x % 7 == 0)
    or (x % 11 == 0)
  )
def starship(render:Render, **kwargs):
  x, y = kwargs['coords']
  w, u, v = kwargs['bari']
  nA, nB, nC = kwargs['normals']
  i = nA.normalize() * kwargs['light'].normalize()

  r = max(min(round(255 * i), 255), 0)
  g = max(min(round(255 * i), 255), 0)
  b = max(min(round(255 * i), 255), 0)

  b += 100 if b < 155 else 0
  g += 50 if g < 150 else -25
  r = 180 if r < 50 else r

  return color(r, g, b, normalized=False)

def moon_shader(render:Render, **kwargs):
  x, y = kwargs['coords']

  w, u, v = kwargs['bari']
  i = 1 - (__getIntensity(kwargs['light'], (w, u, v), kwargs['normals']))

  tA, tB, tC = kwargs['texture_coords']
  tx = tA.x * w + tB.x * u + tC.x * v
  ty = tA.y * w + tB.y * u + tC.y * v

  r, g, b = render.texture.get_color_astronaut(tx, ty, i)

  return color(
    r,
    g,
    b,
    normalized=False
  )

def earth_shader(render:Render, **kwargs):
  x, y = kwargs['coords']
  if x % 7 == 0 and y % 7 == 0: return color(0, 0, .7)

  w, u, v = kwargs['bari']
  i = __getIntensity(kwargs['light'], (w, u, v), kwargs['normals'])

  tA, tB, tC = kwargs['texture_coords']
  tx = tA.x * w + tB.x * u + tC.x * v
  ty = tA.y * w + tB.y * u + tC.y * v
  if 0 <= tx < render.window_w and 0 <= ty < render.window_h:
    return render.texture.get_color(tx, ty, i)
  return color(0, 0, .7)
