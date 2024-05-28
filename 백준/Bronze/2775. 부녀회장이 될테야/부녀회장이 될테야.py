t = int(input())

for i in range(t) :
  floor = int(input())
  ho = int(input())

  young = [x for x in range(1, ho + 1)]
  for j in range(floor) :
    for k in range(1, ho) :
      young[k] += young[k - 1]

  print(young[-1]) 