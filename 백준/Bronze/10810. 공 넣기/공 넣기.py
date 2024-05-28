a,b = map(int,input().split()) 
l = []
for i in range(a):
  l.append(0)
for i in range(b):
  s,d,f = map(int,input().split())
  for j in range(s,d+1):
    l[j-1] = f


print(*l)