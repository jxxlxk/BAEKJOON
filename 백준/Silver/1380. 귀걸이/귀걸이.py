final = []
num = 0
while True :
  n = int(input())

  if n == 0 :
    break
  else :
    num += 1
  student =[]
  for i in range(n) :
    student.append(input())

  temp = []
  for i in range(2 * n - 1) :
    a, b = input().split()
    temp.append(int(a))

  index = 0
  for j in range(1, n + 1) :
    if temp.count(j) == 1:
      index = j
      break
  print(num, student[index - 1]) 