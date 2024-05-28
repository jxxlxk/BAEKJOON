a,b= map(int,input().split())
i = 0
final = 0

while True:
  if i == a:
    break
  else:
    i+=1
    while True: 
      final+=1
      
      if str(b) not in str(final):
        break

print(final)