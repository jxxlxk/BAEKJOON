a = int(input())

for i in range(a):
  t = 0
  l = 0
  
  for j in range(9):
    y,k = map(int,input().split())
    t+= y
    l += k
  if t > l:
    print('Yonsei')
  elif t<l:
    print('Korea')
  else:
    print('Draw')