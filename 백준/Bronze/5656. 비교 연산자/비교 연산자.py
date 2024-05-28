i = 1
while 1:

  a,b,c = input().split()
  a = int(a)
  c = int(c)
  if b =='E':
    break
 
  else:
    if b == '>':
      if a > c:
        print('Case',str(i)+':','true')
      else:
         print('Case',str(i)+':','false')
    elif b == '>=':
      if a >= c:
        print('Case',str(i)+':','true')
      else:
          print('Case',str(i)+':','false')
    elif b == '<':
      if a < c:
        print('Case',str(i)+':','true')
      else:
          print('Case',str(i)+':','false')
    elif b == '<=':
      if a <= c:
        print('Case',str(i)+':','true')
      else:
          print('Case',str(i)+':','false')
      
    elif b == '==':
      if a == c:
        print('Case',str(i)+':','true')
      else:
        print('Case',str(i)+':','false')
    else:
      if a != c:
        print('Case',str(i)+':','true')
      else:
        print('Case',str(i)+':','false')
  i+=1
        