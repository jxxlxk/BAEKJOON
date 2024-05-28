a = []

for i in range(3):
  a.append(list(input().split()))

p,o = [],[]

for i in range(3):
  p.append(a[i][0])
  o.append(a[i][1])

for i in range(3):
  if p.count(p[i]) == 1:
    h = p[i]
  if o.count(o[i]) == 1:
    e = o[i]

print(h,e)