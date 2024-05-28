x,y,w,h = map(int,input().split())  
p = w-x
a = []
o = h-y

a.append(p)
a.append(o)
a.append(x)
a.append(y)

a.sort()
print(a[0])