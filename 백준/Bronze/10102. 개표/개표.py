a = int(input())
b = input()
n = b.count('A')
m = b.count('B')
if n > m:
    print('A')
elif m > n:
    print('B')
else:
    print('Tie')
    