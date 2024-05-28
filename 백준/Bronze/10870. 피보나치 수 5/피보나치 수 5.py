a = int(input())
b = [0,1]
for i in range(2,a+1):
  b.append(b[-1]+b[-2])
if a == 0:
  print(0)
else:
  print(b[-1])