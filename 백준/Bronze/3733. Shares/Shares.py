while 1:
  try:
    x,y = map(int,input().split())
    x+=1
    print(y//x)
  except EOFError:
    break