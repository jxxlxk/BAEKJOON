a = []
while 1:
  try:
    a.append(input())
  except EOFError:
    break  

print(len(a))