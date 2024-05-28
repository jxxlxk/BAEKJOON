l = int(input())
for i in range(l):
    a,b =(input().split())
    a=int(a)
    print(str(b[:a-1])+str(b[a:]))
