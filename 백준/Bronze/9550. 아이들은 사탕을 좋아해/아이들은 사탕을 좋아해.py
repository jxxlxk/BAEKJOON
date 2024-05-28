a = int(input())

for i in range(a):
  k = 0
  n,m = map(int,input().split())
  l = list(map(int,input().split()))
  for i in range(n):
    k+= l[i]//m
  print(k)  