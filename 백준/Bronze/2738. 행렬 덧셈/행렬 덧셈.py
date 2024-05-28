N,M = map(int,input().split())
l = []
ll = []
for i in range(N):
  a = list(input().split())
  l.append(a)         
for i in range(N):
  b = list(input().split())
  ll.append(b)
for i in range(N):
  h = []
  for j in range(M):
    h.append(int(ll[i][j])+int(l[i][j]))
  print(*h)