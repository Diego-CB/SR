
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

  def __matmul__(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z
  
  # --- Methods
  def size(self):
    return (self.x**2 + self.y**2 + self.z**2)**0.5
  
  def mul_cruz(self, other):
    return V3(
      self.y * other.z - self.z * other.y,
      self.z * other.x - self.x * other.z,
      self.x * other.y - self.y * other.x
    )

  def normalize(self):
    return self * 1 / self.size()
