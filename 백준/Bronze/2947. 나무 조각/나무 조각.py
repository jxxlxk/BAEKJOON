a = list(map(int,input().split()))
b = 0



while 1:
  if a == [1,2,3,4,5]:
    break

  else:
    
    if a[0]>a[1]:
      b = 0
      b = a[0]
      a[0] = a[1]
      a[1] = b
      print(*a)
      
    if a[1]>a[2]:
      b = 0
      b = a[1]
      a[1] = a[2]
      a[2] = b
      print(*a)
      
    if a[2]>a[3]:
      b = 0
      b = a[2]
      a[2] = a[3]
      a[3] = b
      print(*a)  

    if a[3]>a[4]:
      b = 0
      b = a[3]
      a[3] = a[4]
      a[4] = b
      print(*a)
    
      