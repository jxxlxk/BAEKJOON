a = int(input())
rb = set()
rb.add('ChongChong')
for i in range(a):
  a,b = input().split()
  if a in rb:rb.add(b)
  if b in rb:rb.add(a)
print(len(rb))    