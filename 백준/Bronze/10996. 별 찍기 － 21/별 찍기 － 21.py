a = int(input())
if a%2 != 0:  
  for i in range(a):
    print((a//2+1)*('* '))
    print(' '+a//2*('* '))

else:
  for i in range(a):
    print((a//2)*('* '))
    print(' '+a//2*('* '))