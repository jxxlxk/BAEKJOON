a,b = map(int,input().split())
l = []
hap = 0
for i in range(1,b+1,1):
  for j in range(i):
    l.append(i)

print(sum(l[a-1:b]))