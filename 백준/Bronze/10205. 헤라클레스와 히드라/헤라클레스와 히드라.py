a = int(input())

for i in range(a):

  b = int(input())
  l = list(input())

  for j in range(len(l)):
    if b == 0 : 
      
      break
    else:
      if l[j] == 'c':
        b += 1
      else:
        b-=1
  print("Data Set %d:" % int(i+1))
  print(b)
  print()