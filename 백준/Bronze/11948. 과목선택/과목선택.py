a = []
for i in range(4):
  a.append(int(input()))

b = []
for i in range(2):
  b.append(int(input()))

sa = a.sort()
sb = b.sort()

print(a[1]+a[2]+a[3]+b[1])