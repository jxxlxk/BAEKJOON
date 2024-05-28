b = []
for i in range(100):
  b.append([0]*100) 
a = int(input())
for i in range(a): 
  x,y = map(int,input().split())
  for r in range(x-1, x+9 ): 
    for c in range(y-1,y+9):
      b[r][c] = 1
count = 0 
for i in range(100):
  for j in range(100):
    count += b[i][j]
print(count)