n, m = map(int, input().split())
numbers = list(map(int, input().split()))
l = set()
p = []
for x in numbers :
  for y in numbers[1:] :
    if x == y :
      break
    for z in numbers[2:] :
      if z == x or z == y :
        break
      l.add(x + y + z)
for i in l :
  if i <= m :
    p.append(i)
print(max(p)) 