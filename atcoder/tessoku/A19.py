N, W = map(int, input().split())
item = [tuple(map(int, input().split())) for i in range(N)]

INF = -float('inf')
dp = [[INF] * (W+1) for i in range(N+1)]

dp[0][0] = 0

for i in range(N):
  for j in range(W):
    if dp[i][j] == INF : continue
    dp[i+1][j] = max(dp[i][j],dp[i+1][j])
    if W < j+item[i][0] : continue
    dp[i+1][j+item[i][0]] = max(dp[i][j+item[i][0]], dp[i][j] + item[i][1])

print(max(dp[-1]))
