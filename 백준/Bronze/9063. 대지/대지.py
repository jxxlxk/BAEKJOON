a = int(input())
u = []
j = []
f = []
for i in range(a):
  u.append(list(map(int,input().split())))
for i in range(a):
  j.append(u[i][0])
  f.append(u[i][1])

j.sort()
f.sort()

print((j[len(j)-1]-j[0])*(f[len(f)-1]-f[0]))
