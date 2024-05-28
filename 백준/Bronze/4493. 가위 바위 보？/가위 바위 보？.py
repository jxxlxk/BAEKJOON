a = int(input())
pla = 0
pl = 0
for i in range(a):
  n = int(input())
  for i in range(n):
    b,c = input().split()
    if b == c:
      pla += 1
      pl += 1
    elif (b == 'R' and c == 'S') or (b == 'S'and c == 'P')or (b == 'P' and c == 'R'):
      pla += 1
    else:
      pl += 1
  if pl == pla:
    print('TIE')
  elif pl > pla:
    print('Player 2')
  else:
    print('Player 1')
  pl = 0
  pla = 0  
      