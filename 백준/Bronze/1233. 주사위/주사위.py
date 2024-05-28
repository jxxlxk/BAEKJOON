a,b,c = map(int,input().split())
g = []
h = []
q = []
mox = 98765456789765456890



for i in range(1,a+1):
  for j in range(1,b+1):
    for k in range(1,c+1):
      g.append(i+j+k)


for i in range(len(g)):

  if len(g) == 0:
    break
  else:
    t = g[0]
    h.append(t)
    q.append(g.count(t))
    for j in range(g.count(t)):
      g.remove(t)
  

f = max(q)

if q.count(f) > 1:
  for i in range(q.count(f)):
    if mox > h[q.index(f)]:
      mox = h[q.index(f)]
      h.remove(h[q.index(f)])

  print(mox)   
else:
  print(h[q.index(f)])


