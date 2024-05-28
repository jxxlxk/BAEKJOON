a = int(input())
l = list(map(int,input().split()))
l.append(0)
mox = 0
s = 0
for i in range(len(l)-1):

  if l[i] < l[i+1]:
    s += l[i+1] - l[i]
  else:  
      if mox < s:
        mox = s
      s = 0   
      



print(mox)