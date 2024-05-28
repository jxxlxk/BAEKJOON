a,b,c = map(int,input().split())
n = b-a-1
m = c-b-1
if n >= m:
    print(n)
else:
    print(m)