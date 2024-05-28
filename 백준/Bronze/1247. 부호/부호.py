for i in range(3):
  b = 0
  a = int(input())
  for j in range(a):
    b+=int(input())
  if b == 0:
    print(0)
  elif b > 0:
    print('+')
  else:
    print('-')