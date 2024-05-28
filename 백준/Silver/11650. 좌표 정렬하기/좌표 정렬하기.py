n = []

for i in range(int(input())):
  x,y = map(int,input().split())
  n.append((x,y))
n.sort()
for x,y in n:
  print(x,y)