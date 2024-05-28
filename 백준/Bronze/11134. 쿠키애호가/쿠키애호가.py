a = int(input())
n = []
for i in range(a):
    n.append(list(map(int,input().split())))
    
    
for i in range(a):
    if n[i][0] % n[i][1] == 0:
        print(n[i][0]//n[i][1])
    else:
        print(n[i][0]//n[i][1]+1)