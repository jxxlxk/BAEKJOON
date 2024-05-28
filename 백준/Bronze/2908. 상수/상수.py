a,b = map(int, input().split())
a = str(a)
b = str(b)
f = 0
j = 0

f += int(a[2])*100
f += int(a[1])*10
f += int(a[0])
j += int(b[2])*100
j += int(b[1])*10
j += int(b[0])

if f > j:
    print(f)
else:
    print(j)