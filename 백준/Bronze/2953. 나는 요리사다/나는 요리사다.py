o = list(input().split())
t = list(input().split())
th = list(input().split())
f = list(input().split())
fi = list(input().split())
a = 0
b = 0
c = 0
d = 0
e = 0
mix = 0
li = []
for i in o:
  a += int(i)
for i in t:
  b += int(i)
for i in th:
  c += int(i)
for i in f:
  d += int(i)
for i in fi:
  e += int(i)
li.append(a)  
li.append(b)  
li.append(c)  
li.append(d)  
li.append(e)  
for i in range(5):
  if li[i] > mix:
    mix = li[i]
if mix == a:
  print(1,mix)
if mix == b:
  print(2,mix)
if mix == c:
  print(3,mix)
if mix == d:
  print(4,mix)  
if mix == e:
  print(5,mix)    