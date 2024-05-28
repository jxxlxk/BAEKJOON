a = 1
for i in range(3):
  a*=int(input())

a = str(a)

g = [0]*10

for i in range(len(a)):
  g[int(a[i])] += 1
for i in range(10):
  print(g[i])