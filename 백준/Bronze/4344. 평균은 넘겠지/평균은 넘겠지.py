c = int(input())
for i in range(c):
  a = list(map(int,input().split()))
  b = a[0]
  a.remove(a[0])
  h = 0
  s = 0
  for j in range(b):
    s += a[j]
  p = s/b
  for i in a:
    if i>p:
      h += 100/b
  print('%.3f'%h+"%")