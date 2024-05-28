a = int(input())
h = -2
for i in range(a):
  h += 2
  if a == i+1:    
    print('*'*(i*2+1))
  elif i == 0:
    print((a-1)*' '+ '*')
  else:
    print(' '*(a-i-1)+'*'+' '*(h-1)+'*')
  