a = int(input())
for i in range(a):
  t = 0
  a,b = map(int,input().split())
  for j in range(a,b+1):
    t +=str(j).count('0')
  print(t)