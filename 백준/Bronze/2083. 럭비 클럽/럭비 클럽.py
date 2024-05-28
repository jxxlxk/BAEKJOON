while 1:
  a = input()
  if a == '# 0 0':
    break
  else:
    y,u,i = a.split()
    u = int(u)
    i = int(i)
    if u > 17 or  i>= 80:
      print(y,'Senior')
    else:
      print(y,'Junior')