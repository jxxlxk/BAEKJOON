a,b,c = map(int,input().split())
n = 0
if c-b > 0:
  print(a//(c-b)+1)
else:
  print(-1)
  
    