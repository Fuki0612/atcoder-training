N, W = map(int, input().split())
item = [tuple(map(int, input().split())) for i in range(N)]

INF = float('inf')
dp = [[INF] * (100001) for i in range(N+1)]
dp[0][0] = 0

for i in range(N):
  for j in range(100001):
    if dp[i][j] == INF : continue
    dp[i+1][j] = min(dp[i][j], dp[i+1][j])
    if 100001 < j+item[i][1] : continue
    dp[i+1][j+item[i][1]] = min(dp[i][j+item[i][1]], dp[i][j] + item[i][0])

out = 0
for i in range(100001):
  if dp[-1][i] <= W:
    out = i

print(out)