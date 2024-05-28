n = int(input())
a = 665
ans = 0
while True:
  a+=1
  if '666' in str(a):
    ans+=1
  if ans == n:
    print(a)
    break
  