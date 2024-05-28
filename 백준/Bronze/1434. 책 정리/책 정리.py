a,b = map(int,input().split())
h,y =0,0
g = list(map(int,input().split()))

for i in range(a):
  h += g[i]
q = list(map(int,input().split()))
for i in range(b):
  y += q[i]

print(h-y)