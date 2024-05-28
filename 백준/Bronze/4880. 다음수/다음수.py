while 1:
  h = []
  a,b,c = map(int,input().split())
  if a == 0 and b == 0 and c == 0:
    break
  else:
    h.append(b-a)
    h.append(c-b)

    if h[0] == h[1]:
      print('AP',c+h[0])
    else:
      p = b//a
      print('GP',c*p)
      
