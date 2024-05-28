n,x = map(int,input().split())
a = list(map(int,input().split()))
b = list()
for i in range(n):
  if a[i] < x:
    b.append(a[i])
for i in b:
  print(i,end = ' ')
    