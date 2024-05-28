n = int(input())
ans = n
for i in range(n):
  b = input()
  for i in range(len(b)-1):
    if b[i] != b[i+1]:
      if b[i] in b[i+1:]:
        ans -= 1
        break
print(ans)        