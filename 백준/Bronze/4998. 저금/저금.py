while 1:
  year = 0
  try:
    m,b,n = map(float,input().split())
    while m<n:
      m+= b/100*m
      year += 1

    print(year)
      
        
  except:
    break