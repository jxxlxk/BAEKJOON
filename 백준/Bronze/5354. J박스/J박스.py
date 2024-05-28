a = int(input())
l = []

for i in range(a):
  l.append(int(input()))

for i in l:
  if i == 1:
    print('#','\n')
  elif i==2:
    print('##')
    print('##','\n')
    
  else:
    print(i*'#')
    
    for j in range(i-2):
      print('#'+'J'*(i-2)+'#')
    print(i*'#','\n')