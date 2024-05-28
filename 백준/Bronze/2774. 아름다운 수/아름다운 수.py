a = int(input())


for i in range(a):
  num = input()
  temp = 0
  if len(num) == 1:
    print(1)
  else:
    list = []
    
    for j in range(len(num)):
      if list.count(num[j]) == 0:
        temp += 1
        list.append(num[j])  

    print(temp)