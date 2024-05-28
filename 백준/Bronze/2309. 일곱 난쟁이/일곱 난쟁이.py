sum = 0
len = []

for i in range(9) :
  dwarf = int(input())
  sum += dwarf
  len.append(dwarf)

total_sum = sum - 100
ans = 0
for j in range(8) :
  if ans == 1 :
    break
  for k in range(j + 1, 9):
    if len[j] + len[k] == total_sum :
      a = len[j]
      b = len[k]
      len.remove(a)
      len.remove(b)
      ans = 1
      break
len.sort()
for l in len :
  print(l) 
