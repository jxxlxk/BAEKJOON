a = int(input())
l = list(map(int, input().split()))
y = 0
m = 0

for i in l :
  y += i // 30 * 10 + 10
  m += i // 60 * 15 + 15

if y > m :
  print("M", m)
elif y < m :
  print("Y", y)
else :
  print("Y M", m) 