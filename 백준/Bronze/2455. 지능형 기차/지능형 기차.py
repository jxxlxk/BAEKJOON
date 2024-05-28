
count = 0
max =0
l = []

for i in range(4):
  g,h = map(int,input().split())
  count -= g
  count+= h
  l.append(count)


l.sort()








print(l[3])