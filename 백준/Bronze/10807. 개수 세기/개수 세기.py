import sys
input = sys.stdin.readline
a = int(input())
c = 0
b = input().split()
n = input().rstrip()
for i in b:
    if i == n:
        c +=1
print(c)    