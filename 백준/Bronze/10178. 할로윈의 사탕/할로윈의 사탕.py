a = int(input())
for i in range(a):
  b,c = map(int,input().split())
  print('You get', b//c, 'piece(s) and your dad gets', b%c, 'piece(s).')
    