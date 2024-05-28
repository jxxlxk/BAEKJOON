a = int(input())
v = []
total = 0

for i in range(a):
  x, y = map(int, input(). split())
  v.append([x, y])

v.sort()

start = 0
for j in v:
  if j[1] > total :
    total = j[1]
    temp = start
  start += 1

height = v[0][1]

for h in range(temp):
  if height < v[h+1][1] :
    total += height * (v[h+1][0] - v[h][0])
    height = v[h+1][1]

  else :
    total += height * (v[h+1][0] - v[h][0])

height = v[-1][1]

for t in range(a-1, temp, -1):
  if height < v[t-1][1]:
    total += height *(v[t][0] - v[t-1][0])
    height = v[t-1][1]

  else :
    total += height * (v[t][0] - v[t-1][0])

print(total) 