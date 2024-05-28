a,b = map(int,input().split())

u = []

for i in range(a):
  u.append(i + 1)

for i in range(b):
  x,y = map(int,input().split())
  p = []
  for j in range(x-1,y):
    p.append(u[j])
  p.reverse()

  for j in range(x-1,y):
    u[j] = p[j-x+1]

print(*u)
  