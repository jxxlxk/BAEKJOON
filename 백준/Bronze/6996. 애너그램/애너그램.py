a = int(input())

for i in range(a):
  n,m = map(str,input().split())
  q = sorted(n)
  w= sorted(m)
  if q == w:
    print(n,'&',m,'are anagrams.')
  else:
    print(n,'&',m,'are NOT anagrams.')