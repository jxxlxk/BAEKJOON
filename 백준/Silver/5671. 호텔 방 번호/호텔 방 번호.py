while 1 :
  try :
    a, b = map(int ,input().split())
  except :
    break
  tot = 0
  for i in range(a, b + 1) :
    k = set()
    number = str(i)
    for j in number :
      k.add(j)
    if len(number) == len(k) :
      tot += 1
  print(tot) 