a = int(input())
l = []

for i in range(a):
  l.append(float(input()))
  if len(l) > 7:
    l.remove(max(l))

for j in sorted(l):
  print(f'{j:.3f}')