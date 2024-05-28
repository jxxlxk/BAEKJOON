for i in range(int(input())) :
  w = input()
  if w == "P=NP" :
    print("skipped")
  else :
    a, b = map(int, w.split("+"))
    print(a + b)