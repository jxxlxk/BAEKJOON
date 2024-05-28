y = []
while 1:
  a = float(input())
  if a == 999:
    break
  else:
    y.append(a)

for i in range(1,len(y)):
  print("%.2f" %(y[i]-y[i-1]))