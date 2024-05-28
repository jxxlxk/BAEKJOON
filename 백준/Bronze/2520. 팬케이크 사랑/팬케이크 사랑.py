a = int(input())
for i in range(a):
  oeihefr = input()
  m,y,su,sa,f = map(int,input().split())
  b,s,c,w = map(int,input().split())
  banjuk = [int(m /8 * 16),  int(y /8 * 16), int(su /4 * 16), int(sa /1 * 16), int(f /9 * 16)]
  banjuk = min((banjuk))
  top = sum([b //1, s // 30, c // 25, w // 10])
  if banjuk > top:
    print(top)
  elif banjuk <= top:
    print(banjuk) 