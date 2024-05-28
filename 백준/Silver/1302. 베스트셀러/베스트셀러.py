a = int(input())
u = []
for i in range(a):
  u.append(input())
count = []
t = []
for i in range(a):
  if u[i] not in t:
    t.append(u[i])
    count.append(u.count(u[i]))

if count.count(max(count)) > 1:
  t = []
  for i in range(a):
    if u.count(u[i]) == max(count):
      t.append(u[i])
  t.sort()
  print(t[0])

    
else:
  print(t[count.index(max(count))])
    
    