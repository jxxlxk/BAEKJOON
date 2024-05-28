a,b = map(int,input().split())
s =[]

for i in range(a):
    s.append(list(map(int,input().split())))
s.sort(key = lambda x:(x[1],x[2],x[3]), reverse = True)

for i in range(a):
    if s[i][0] == b:
        index = i
        
for i in range(a):
    if s[index][1:] == s[i][1:]:
        print(i+1)
        break