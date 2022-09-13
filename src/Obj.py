''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  Obj.py (Object)
  - Object used to read .obj models

  Last modified (yy-mm-dd): 2022-07-31
--------------------------------------
'''

class Obj(object):
  '''
  .obj file reader

  Atributes
  ---------
  lines: lines written in the .obj file
  vertices: Vertices of the model
  faces: faces of the model
  '''
  def __init__(self, filename):
    with open(filename) as f:
      self.lines = f.read().splitlines()
    
    self.vertices = []
    self.faces = []
    self.tverctices = []

    for line in self.lines:
      try:
        prefix, value = line.split(' ', 1)
      except:
        continue

      match prefix:
        case 'v':
          temp_vertices = [
            float(n) for n in list(filter(
              lambda v: v != '', value.split(' ')
            ))
          ]
          self.vertices.append(temp_vertices)
        
        case 'f':
          temp_faces = [
            [int(n) for n in face.split('/')]
              for face in list(filter(
              lambda v: v != '', value.split(' ')
            ))
          ]
          self.faces.append(temp_faces)

        case 'vt':
          temp_vertices = [
            float(n) for n in list(filter(
              lambda v: v != '', value.split(' ')
            ))
          ]
          self.tverctices.append(temp_vertices)
