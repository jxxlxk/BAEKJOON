a = int(input())

for i in range(a):
  x = 0
  n =[]
  f,j = map(int,input().split())
  for q in range(j):
    t,g = map(int,input().split())
    n.append(t*g)
  n.sort(reverse=True)
  x = 0
  m = 0 
  
  while 1:
    m += n[x]
    if m >= f:
      break
    else:
      x+= 1
  print(x+1)