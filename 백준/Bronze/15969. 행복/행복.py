a = int(input())
b = list(map(int,input().split()))
b.sort()
print(b[a-1]-b[0])