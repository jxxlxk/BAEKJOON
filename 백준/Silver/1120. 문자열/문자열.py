a, b = input().split()
case = []
for i in range(len(b)-len(a)+1):
  count = 0
  for j in range(len(a)):
    if a[j] != b[i+j]:
      count +=1
  case.append(count) 


print(min(case))