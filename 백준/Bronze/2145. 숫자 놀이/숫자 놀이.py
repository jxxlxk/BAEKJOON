while(True):
  
  a = int(input())
  if a == 0:
    break
    
  else:
    b = str(a)
    
    while 1:
      if len(b)  == 1:
        break
        
      else:
        b = str(a)
        a = 0
        for i in range(len(b)):
          
          a += int(b[i])
        b = str(a)
  print(a) 
