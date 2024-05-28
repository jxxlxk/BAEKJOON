a = int(input())
num = a
count = 0


while True:
  b = num//10
  c = num%10
  d = (b+c)%10
  num = (c*10) + d
  count += 1
  if num == a:
    break
print(count)