while 1:
  sam= 0
  a = input()
  if a == '#':
    break
  else:
    for i in range(len(a)):
      if a[i] == ' ':
        continue
      else:  
        sam += (ord(a[i])-64)*(i+1)
    print(sam) 