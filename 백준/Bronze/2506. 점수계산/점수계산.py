a = int(input())
c = 0 
streak = 0
l = list(map(int,input().split()))

for i in range(a):
  if l[i] == 1:
    streak += 1
    c+=streak
  else:
    streak = 0
print(c)    