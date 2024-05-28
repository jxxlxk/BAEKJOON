a = int(input())

for i in range(a):
  b = int(input())
  u = 1
  if b == 1 or b == 0:
    print(1)
  else:
    q = 1
    w = 1
    for j in range(b-1):
      
      u = q+w
      q = w
      w = u
    
    print(u)