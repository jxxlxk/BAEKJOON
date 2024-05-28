a = []
b = []

g = 0
h = 0
for i in range(10):
  a.append(int(input()))
for i in range(10):
  b.append(int(input()))

a.sort(reverse = 1)
b.sort(reverse = 1)
for i in range(3):
  g+= a[i]
  h+= b[i]

print(g,h)