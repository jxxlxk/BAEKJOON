a = int(input())

print('Gnomes:')

for i in range(a):
  s = list(map(int,input().split()))

  l = sorted(s)
  k = sorted(s,reverse = 1)
  if  l== s or  k== s:
    print('Ordered')
  else:
    print('Unordered')