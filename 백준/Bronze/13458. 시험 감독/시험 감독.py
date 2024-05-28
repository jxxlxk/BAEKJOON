n = int(input())
list = map(int, input().split())
b, c = map(int, input().split())

total = 0

for i in list :
  total += 1
  i = i - b
  if i > 0 :
    total += i // c
    if i % c != 0:
      total += 1
print(total) 