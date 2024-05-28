croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()

for i in croatia :
  a = a.replace(i, '_')
print(len(a))