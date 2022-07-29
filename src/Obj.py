
from fileinput import filename

class Obj(object):
  def __init__(self, filename):
    with open(filename) as f:
      self.lines = f.read().splitlines()
    
    self.vertices = []
    self.faces = []

    for line in self.lines:
      try:
        prefix, value = line.split(' ', 1)
      except:
        continue

      match prefix:
        case 'v':
          self.vertices.append(list(
            map(float, value.split(' '))
          ))
        
        case 'f':
          self.faces.append([
            list(map(int, face.split('/')))
              for face in value.split(' ')
          ])


  