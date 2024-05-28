a, b, c = map(int, input().split(":"))
answer = 0
if 0 < a < 13:
    answer += 2
if 0 < b < 13:
    answer += 2
if 0 < c < 13:
    answer += 2
if 59 < a or 59 < b or 59 < c:
    answer = 0
print(answer) 