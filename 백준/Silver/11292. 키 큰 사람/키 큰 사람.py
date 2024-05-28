while 1:
  a = int(input())
  if a == 0:
    break
  else:
    q,p = [],[]
    hax = 0
    u = []
    for i in range(a):
      
      g,h = input().split()
      h = float(h)
      q.append(g)
      p.append(h)
      
    hax = max(p)
    for i in range(a):
      if p[i] == hax:
        u.append(q[i])
    print(*u)    
        