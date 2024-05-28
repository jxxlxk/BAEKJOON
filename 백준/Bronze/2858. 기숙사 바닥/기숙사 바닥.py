a,b = map(int,input().split())
for i in range(3,2000):
  for j in range(3,i+1):
    k = (i*2)+((j-2)*2)
    if k == a and (i*j) -k == b:
      print(i,j)