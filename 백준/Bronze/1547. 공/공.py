a = int(input())
q = 1
for i in range(a):
  v,b = map(int,input().split())
  if v == q:
    q = b
  elif b == q:
    q = v
print(q)   