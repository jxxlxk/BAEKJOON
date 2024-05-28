t  = int(input())
for q in range(t):
  count = 0
  n,m = map(int,input().split())
  for i in range(2,n):
    for j in range(1,i):
      if (i**2+j**2+m)/(i*j) ==(i**2+j**2+m)//(i*j):
        count += 1
  print(count)      