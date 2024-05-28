r,c,zr,zc = map(int,input().split())
b = []
finfin = []

for i in range(r):
  b.append(input())


for i in range(r):
  row = []
  for j in range(c):
    row.append(b[i][j] * zc)
  for k in range(zr):
    finfin.append(row)

for i in finfin :
  print(''.join(i)) 