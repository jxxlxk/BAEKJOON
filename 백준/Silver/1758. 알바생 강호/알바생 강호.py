a = int(input())
t = []
tot = 0
for i in range(a):
    t.append(int(input()))

t.sort(reverse = True)

for i in range(len(t)):
  if t[i]-(i+1-1) >= 0:
    
    tot +=t[i]-(i+1-1)
  else:
    continue

print(tot)
