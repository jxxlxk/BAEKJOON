a = int(input())

for i in range(a, 3, -1) :
  z = str(i)
  temp = 0
  for j in z:
    if  j == '4':
      temp += 1

    elif j == '7':
      temp += 1
  if temp == len(z) :
    print(z)
    break 