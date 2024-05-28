for i in range(3):
  streak = 1
  mix = 0
  b = input()
  for j in range(1,len(b)):
    if b[j] == b[j-1]:
      streak += 1
      
    else:
      streak = 1
      
    if mix< streak:
      mix = streak
        
  print(mix) 