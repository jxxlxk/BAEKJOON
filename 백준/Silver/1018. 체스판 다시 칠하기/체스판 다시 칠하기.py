N,M = map(int,input().split())
board = []
ans = []
mini=10000000000000000000000000000000000000000000000000
for n in range(N):
  board.append(input())
  
for x in range(N-7):
  for y in range(M-7):
    black,white = 0,0
    for i in range(x,x+8):
      for j in range(y,y+8):
        if (i+j) % 2 == 0:
          if board[i][j] != 'B':
            black += 1
          if board[i][j] != 'W':
            white +=1
        else:
          if board[i][j] != 'W':
              black += 1
          if board[i][j] != 'B':
              white +=1
    ans.append(black)
    ans.append(white)
x = len(ans)
for i in range(x):
  if mini>ans[i]:
    mini = ans[i]
    
print(mini)   