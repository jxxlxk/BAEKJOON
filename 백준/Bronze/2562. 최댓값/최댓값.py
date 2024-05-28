import sys
input = sys.stdin.readline
max1 = 0
for i in range(9):
    num = int(input())
    if num > max1:
      idx = i + 1
      max1 = num
print(max1)     
print(idx)
    