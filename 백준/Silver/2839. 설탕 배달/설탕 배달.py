n = int(input())
ans = 0
s = True
while n >= 0:
  if n % 5 == 0:
    ans += n//5
    print(ans)
    s = False
    break
  n -= 3
  ans+=1
if s:  
  print(-1)  