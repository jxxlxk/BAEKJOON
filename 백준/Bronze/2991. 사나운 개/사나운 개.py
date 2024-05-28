a, b, c, d = map(int, input().split())
delivery_time = list(map(int, input().split()))

for i in delivery_time:
  dog = 0

  if 0 < i % (a + b) <= a :
    dog += 1
  if 0 < i % (c + d) <= c :
    dog += 1

  print(dog) 