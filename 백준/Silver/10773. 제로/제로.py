a = int(input())
tot = []
for i in range(a):
  y = int(input())
  if y == 0:
    del tot[len(tot)-1]
  else:
    tot.append(y)

print(sum(tot))