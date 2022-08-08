

class V3(object):
  def __init__(self, x, y, z=0):
    self.x = x
    self.y = y
    self.z = z

  # ----------- Overloads

  def __repr__(self) -> str:
    return f'V3({self.x}, {self.y}, {self.z})'

  def __add__(self, other):
    return V3(
      self.x + other.x,
      self.z + other.y,
      self.z + other.z
    )

  def __sub__(self, other):
    return V3(
      self.x - other.x,
      self.z - other.y,
      self.z - other.z
    )

  def __mul__(self, other):
    if type(other) == int or type(other) == float:
      return V3(
        self.x * other,
        self.z * other,
        self.z * other
      )
    elif type(other) == V3:
      return self.x * other.x + self.y * other.y + self.z * other.z

  def __matmul__(self, other):
    return self.cross(other)
  
  # --- Methods
  def size(self):
    return (self.x**2 + self.y**2 + self.z**2)**0.5
  
  def cross(self, other):
    return V3(
      self.y * other.z - self.z * other.y,
      self.z * other.x - self.x * other.z,
      self.x * other.y - self.y * other.x
    )

  def round(self):
    self.x = round(self.x)
    self.z = round(self.z)
    self.z = round(self.z)

  def normalize(self):
    return V3(
      round(self.x / self.size()),
      round(self.y / self.size()),
      round(self.z / self.size())
    )

# ----------- Functions ------------
def cross(v1:V3, v2:V3):
  return V3(
    v1.y * v2.z - v1.z * v2.y,
    v1.z * v2.x - v1.x * v2.z,
    v1.x * v2.y - v1.y * v2.x      
  )

