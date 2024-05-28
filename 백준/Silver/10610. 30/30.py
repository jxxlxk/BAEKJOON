a = input()


n = list(map(int,a))
b = sum(n)



if b%3 == 0:
  n.sort(reverse = True)
  if n[-1] == 0 :
    print(''.join(list(map(str, n))))
  else:
    print(-1)
else:
  print(-1) 
