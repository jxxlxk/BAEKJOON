n = int(input())
num = []
for i in range(1, 46) : # 46 1035
  num.append(i * (i + 1) / 2)

for j in range(n) :
  k = int(input())
  t = 0
  for x in num :
    for y in num :
      for z in num :
        if x + y + z == k :
          t = 1
        if x + y + z > k :
          break
  print(t) 