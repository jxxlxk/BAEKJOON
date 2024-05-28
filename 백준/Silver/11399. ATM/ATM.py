a = int(input())
huh = 0
b = list(map(int, input().split()))
b.sort()
time = 0
for i in b:
  huh += i
  time += huh
print(time)