a = int(input())
c = 0
if 99 + 99 < a:
  print(0)
else:
  for i in range(1,100):
    for j in range(1,100):
      if i+j == a:
        c+=1

  print(c)