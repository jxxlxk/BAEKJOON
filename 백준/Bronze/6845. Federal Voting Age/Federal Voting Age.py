a = int(input())
for i in range(a):
  y,m,d = map(int,input().split())
  if y > 1989:
    print('No')
  elif y == 1989:
    if m > 2:
      print('No')
    elif m == 2:
      if d > 27:
        print('No')
      else:
        print('Yes')
    else:
      print('Yes')
  else:
    print('Yes')