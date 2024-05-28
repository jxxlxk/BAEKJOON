a,b = map(int,input().split())
c = []
d = []
g = []
column = []
row = []
h = 0
for i in range(a):
  c.append(list(input().split()))
  
for i in range(a):
  for j in range(b):
    d.append(c[i][j].count('9'))
  g.append(d)
  d = []

for i in range(a):
  for j in range(b):
    h+=g[i][j]
  row.append(h)  
  h = 0


for j in range(b):
  for i in range(a):
    h+=g[i][j]
  column.append(h)
  h = 0

mox = max(row+column)


if mox in row:
  print(sum(row)-mox)
else:
  print(sum(column)-mox)

