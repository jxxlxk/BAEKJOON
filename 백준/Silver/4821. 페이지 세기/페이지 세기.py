while 1 :
  n = int(input())
  if n == 0 :
    break

  joa = input().split(",")
  youngcha = set()

  for i in joa :
    sseo = i.split("-")   
    if len(sseo) == 1 :
      if 1 <= int(sseo[0]) <= n :
        youngcha.add(int(sseo[0]))

    else :
      okji, ppangppang = int(sseo[0]), int(sseo[1])

      for i in range(okji, ppangppang + 1) :
        if 1 <= i <= n :
          youngcha.add(i)

  print(len(youngcha)) 