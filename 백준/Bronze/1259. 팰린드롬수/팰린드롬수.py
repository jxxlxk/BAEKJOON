while 1:
  a = int(input())
  if a == 0:
    break
  else:
    if str(a) == str(a)[::-1]:
      print("yes")
    else:
      print('no')