
# ----- Operaciones algebraicas

def transpos(M):
  matrix = []

  for n in M.matrix:
    matrix.append(n[0])

  return M4([ matrix ])

def matrixMul(M1, M2):
  M1, M2 = M1.matrix, M2.matrix
  n1 = len(M1[0])
  n2 = len(M2)

  if n1 != n2:
    raise Exception('Invalid Sizes of matrixes', n1, n2)

  m = len(M1)
  n = len(M2[0])
  resultMatrix = []

  for i in range(m):
    temp_array:list = []

    for j in range(n):
      temp_value = 0

      for k in range(n1):
        a = M1[i][k]
        b = M2[k][j]
        temp_value += a * b

      temp_array.append(temp_value)
    
    resultMatrix.append(temp_array)
  
  return M4(resultMatrix)

# ----- Objetos

class V4:
  def __init__(self, array:list):
    self.matrix = array
  
  def __repr__(self) -> str:
    return f'V4:\n{self.matrix}\n'

  def __matmul__(self, other):
    if type(other) == M4:
      return matrixMul(
        M4([[ x for x in self.matrix ]]),
        other
      )

class M4:
  def __init__(self, array:list):
    self.matrix = array
  
  def __repr__(self) -> str:
    return f'M4:\n{self.matrix}\n'\
    
  def __matmul__(self, other):
    if type(other) == M4:
      return matrixMul(self, other)
    
    if type(other) == V4:
      return transpos(
        matrixMul(
          self, 
          M4([ [x] for x in other.matrix ])
        )
      )
