u =0

while 1:
  
  u+=1
  a = input()
  b = input()
  if a == 'END' and b == "END":
    break

  else :
    a_n = sorted(list(a))
    b_n = sorted(list(b))

    if a_n == b_n:
      print("Case", str(u) + ": same") 

    else:
      print("Case", str(u) + ": different") 