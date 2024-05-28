p = int(input())
a = list(map(int,input().split()))
t,l = [],[]
for i in range(p):
  if a[i] != -1:
    l.append(a[i])
  else:
    t.append(l)
    l = []
t.append(l)    
print(min(t[0])+min(t[1]))