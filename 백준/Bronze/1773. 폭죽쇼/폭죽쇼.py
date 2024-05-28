import sys
input = sys.stdin.readline

ppl,sec = map(int,input().split())
tot = []
for i in range(ppl):
  tot.append(int(input()))

check = [0] * (sec + 1)

for i in tot :
  time = 0
  if not check[i]:
    while 1 :
      time += i
      if time > sec :
        break
      check[time] = 1

print(check.count(1)) 