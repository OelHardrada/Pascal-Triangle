#Pascal Triagle

def pascal(numRows): #Triangle generator
  global triangles
  triangles = []
  for i in range(numRows):
      triangles.append([])
      for j in range(i + 1):
          if j == 0 or j == i:
              triangles[i].append(1)
          else:
              triangles[i].append(triangles[i - 1][j - 1] + triangles[i - 1][j])
      print(triangles[i])
  return triangles

def get_n(): #Row number
  global n
  a = False
  while a == False:
    n = input("Enter row number desire: ")
    if n.isnumeric(): #Check n as natural number
        n = int(n)
        a = True
    else:
      print('n must be a possitive number')

def main():
  get_n()
  pascal(n)

if __name__ == "__main__":
  main()
