while 1 :
  s = input()
  if s == '*':
    break

  else :
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = []

    for i in a :
      if i not in s :
        b.append(i)

    if not b :
      print("Y")

    else :
      print("N") 