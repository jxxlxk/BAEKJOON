a = int(input())

if a == 1:
  print('*')
  
else:
  print(" "*(a-2),'*')
  b = 0
  for i in range(a-1):
    print(" " * (a-2) + "*" + " " * (b + 1) + "*")
    a -= 1
    b += 2 