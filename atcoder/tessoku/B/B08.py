N = int(input())

max_X = 0
max_Y = 0
XY = []

for i in range(N):
  x, y = map(int, input().split())
  max_X = max(x, max_X)
  max_Y = max(y, max_Y)
  XY.append([x,y])

S = [[0] * (max_X+1) for i in range(max_Y+1)]

for x,y in XY:
  S[y][x] += 1

for y in range(1,max_Y+1):
  for x in range(1,max_X+1):
    S[y][x] += S[y][x-1]

for x in range(1,max_X+1):
  for y in range(1,max_Y+1):
    S[y][x] += S[y-1][x]

Q = int(input())

out = []

for i in range(Q):
  a,b,c,d = map(int, input().split())
  out.append(S[d][c] - S[d][a-1] - S[b-1][c] + S[b-1][a-1]) 

[print(i) for i in out ]