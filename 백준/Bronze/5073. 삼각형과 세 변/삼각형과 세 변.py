while 1:
  a = sorted(list(map(int,input().split())))
  
  if a[0] == 0 and a[1] == 0 and a[2]==0:
    break
    
  if a[2] >=a[0]+a[1]:
    print('Invalid')
  else:  
    if a[0]==a[1]==a[2]:
        print('Equilateral')
    elif a[0]==a[1] or a[0]==a[2] or a[1]==a[2]:
        print('Isosceles ')
    else:
        print('Scalene')