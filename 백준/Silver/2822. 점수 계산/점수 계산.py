b = []
g = 0
f = []

for i in range(8):
  b.append(int(input()))


for i in range(5):
  g+=max(b)
  f.append(b.index(max(b))+1)
  b[b.index(max(b))] = -1982736
f.sort()
print(g)
print(*f)