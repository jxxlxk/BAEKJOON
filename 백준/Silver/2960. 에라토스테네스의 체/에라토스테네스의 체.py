a, b = map(int, input().split())
list = [False] * (a + 1)

count = 0
for i in range(2, a + 1) :
  for j in range(i, a + 1, i):
    if list[j] == False :
      list[j] = True
      count += 1

      if count == b :
        print(j)
        break
        