u = 0

while 1:
  u += 1
  x = input()
  if x == '0':
    break
  else:
    a,b,c = map(int,x.split(' '))
    
    if a*2 >= (b**2+c**2)**0.5:
      print('Pizza', u, 'fits on the table.')
    else:
      print('Pizza', u, 'does not fit on the table.')
      