mo = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
a = input()
for i in range(len(a)):
  if  mo[ord(a[i])-ord('a')] == -1:
    mo[ord(a[i])-ord('a')] = i
print(*mo)  