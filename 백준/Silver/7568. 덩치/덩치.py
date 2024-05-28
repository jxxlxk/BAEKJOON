num = int(input())
l = []
for i in range(num):
  l.append(list(map(int,input().split())))
  
for i in range(num):
  n = 1
  for j in range(num):
    if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
      n += 1
  print(n,end=' ')