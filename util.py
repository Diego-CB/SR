''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Autor: Diego Cordova
  Carne: 20212
  Last modified (yy-mm-dd): 2022-07-15
--------------------------------------
'''

import struct

def char(c):
  return struct.pack('=c', c.encode('ascii'))
  #1 byte

def word(w):
  return struct.pack('=h', w)
  # 2 bytes

def dword(d):
  return struct.pack('=l', d)
  # 4 bytes

def color(r, g, b):
  if r < 0 or r > 1: return print('invalid color:', [r, g, b])
  if g < 0 or b > 1: return print('invalid color:', [r, g, b])
  if g < 0 or b > 1: return print('invalid color:', [r, g, b])

  r = int(255 * r)
  g = int(255 * g)
  b = int(255 * b)
  return bytes([g, r, b])
