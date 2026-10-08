H, W, N = map(int, input().split())

S = [[0] *(W+2) for i in range(H+2)]

for i in range(N):
  a,b,c,d = map(int, input().split())
  S[a][b] += 1
  S[a][d+1] -= 1
  S[c+1][b] -= 1
  S[c+1][d+1] += 1

for h in range(1,H+1):
  for w in range(1,W+1):
    S[h][w] += S[h][w-1]

for w in range(1,W+1):
  for h in range(1,H+1):
    S[h][w] += S[h-1][w]

for h in range(1,H+1):
  print(*S[h][1:W+1])