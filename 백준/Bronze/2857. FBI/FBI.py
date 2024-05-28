count = 0
a = input()
b = input()
c = input()
d = input()
e = input()
if 'FBI' in a:
  print('1')
  count += 1
if 'FBI' in b:
  print('2')
  count += 1
if 'FBI' in c:
  count += 1
  print('3')
if 'FBI' in d:
  count += 1
  print('4')
if 'FBI' in e:
  count += 1
  print('5')
if count == 0:
  print('HE GOT AWAY!')
  