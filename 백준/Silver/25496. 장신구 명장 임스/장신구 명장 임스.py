piro,job = map(int,input().split())
work = list(map(int,input().split()))
work.sort()

w = 0

for i in range(job):
  if piro >= 200:
    break
  else:
    piro += work[w]
    w+=1

print(w)