import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
final = []
for i in range(a,b+1):
  count = 0
  for j in range(1,i+1):
    if i%j == 0:
      count += 1
  if count == 2:
    final.append(i)
if len(final) == 0:
  print(-1)
else:  
  print(sum(final),final[0])    
      