a = int(input())
bf = a*2-1
bs = a-1
if a == 1:
  print('*')
else:  
  print((a*2-1)*("*"))
  for i in range(a-1):
    bf -= 2
    print((((a*2-1)-bf)//2)*(' ')+bf*('*'))
  bf = 1
  for i in range(a-2):
    bs-=1
    bf+=2
    print((bs)*(' ')+bf*("*"))
  
  print((a*2-1)*("*"))
