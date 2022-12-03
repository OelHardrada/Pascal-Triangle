#Pascal triangle and number divisible by d

def pascal(numRows): #Generates triangle
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

def div(d,triangle): #Check divisiblity
    st = f'0 means it is divisible by {d}, 1 means it is not'
    print(st)
    divtriangle = []
    for i, tri in enumerate(triangle):
        divtriangle.append([])
        for j, num in enumerate(triangle[i]):
            if num % d == 0:
                divtriangle[i].append(0)
            else:
                divtriangle[i].append(1)
        print(divtriangle[i])
    return divtriangle

def get_n(): #Gets row number
    global n
    a = True
    while a:
        n = input('Insert row number: ')
        if n.isnumeric():
            n = int(n)
            a = False
        else:
            print('Invalid value for n, it must be a possitive number')
            
def get_d(): #Gets divisor
    global d
    a = True
    while a:
        d = input(('Insert divisor number: '))
        try:
            d = int(d)
            a = False
            break
        except ValueError():
            print('Invalid input')
    

def main():
    get_n()
    get_d()
    pascal(n)
    print()
    div(d,triangles)

if __name__ == "__main__":
  main()