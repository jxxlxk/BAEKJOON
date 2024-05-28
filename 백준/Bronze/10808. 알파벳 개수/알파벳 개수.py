a = [0]*26
al = input()

for i in al:
  a[ord(i)-ord('a')] += 1

print(*a)