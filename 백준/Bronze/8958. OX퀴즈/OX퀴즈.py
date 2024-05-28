num = int(input())


for i in range(num):
  ox = input()
  score = 0
  count = 0

  for i in ox:
    if i == 'O':
      count += 1
      score += count 
    else:
      count = 0
  print(score)      
      