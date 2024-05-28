a,b = map(int,input().split())

u = []

for i in range(a):
  u.append(i + 1)

for i in range(b):
  x,y = map(int,input().split())
  o,p = u[x - 1],u[y - 1]
  u[x - 1] = p
  u[y-1] = o

print(*u)