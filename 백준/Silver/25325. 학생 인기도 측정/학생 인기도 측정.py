a = int(input())
list1 = []
cnt = []
cnt = [0]*a

l = list(input().split())
l.sort()

for i in range(a):
  vote = list(input().split())
  for j in range(a) :
    cnt[j] += vote.count(l[j])

for i in range(a):
  list1.append([cnt[i], a - i, l[i]])
list1.sort(reverse = True)

for i in range(a):
  print(list1[i][2], list1[i][0]) 