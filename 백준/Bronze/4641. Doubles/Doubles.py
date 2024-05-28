while 1:
  sam = 0
  a = list(map(int,input().split()))
  if a[0] == -1 and len(a) == 1:
    break

  for i in range(len(a) - 1) :
    if a [i] % 2 == 0 :
      if a[i] // 2 in a :
        sam += 1

  print(sam)