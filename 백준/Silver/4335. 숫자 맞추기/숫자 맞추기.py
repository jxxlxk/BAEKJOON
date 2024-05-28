mon,mox = 0,11
while 1:
  a = int(input())
  if a == 0:
    break
  b = input()
  if b == "right on" :
    if mon < a and a < mox :
      print("Stan may be honest")
    else :
      print("Stan is dishonest")
    mon, mox = 0, 11
  elif b == "too low" :
    mon = max(mon, a)
  else :
    mox = min(mox, a) 