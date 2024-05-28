n,m = map(int,input().split())
a = int(input())
if n+m >= a*2:
  print(n+m-a*2)
else:
  print(n+m)