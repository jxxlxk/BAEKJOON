n,m = map(int,input().split())
w = 0
y = 1

if n == 0:
  print(0)
else:  
  l = list(map(int,input().split()))
  for i in range (n-1,-1,-1):
    w+=l[i]
    if w > m:
      y+=1
      w = l[i]


  print(y)

