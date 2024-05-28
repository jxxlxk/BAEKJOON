a = int(input())
for i in range(a):
  b = input().split()
  for i in range(2):
    g= b[0]
    b.remove(b[0])
    b.append(g)
  print(*b)  
  