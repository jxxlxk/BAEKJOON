a = int(input())
b = []
c1 = [0]*a

l1 = []
l2 = []
l3 = []


for i in range(a):
  b.append(list(map(int,input().split())))

for i in range(a):
  l1.append(b[i][0])
  l2.append(b[i][1])
  l3.append(b[i][2])


for i in range(a):

  g = l1.count(l1[i])
  if g == 1:
    c1[i] += l1[i]
  else:
    continue

for i in range(a):

  g = l2.count(l2[i])
  if g == 1:
    c1[i] += l2[i]
  else:
    continue

for i in range(a):

  g = l3.count(l3[i])
  if g == 1:
    c1[i] += l3[i]
  else:
    continue
  
for i in range(a):
  print(c1[i])