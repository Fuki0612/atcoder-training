N = int(input())
S = input()

dp = [[0] * N for _ in range(N)]

for i in range(N):
  dp[i][i] = 1

for i in range(N-2, -1, -1):
  for j in range(i+1, N):
    if S[i] == S[j]:
      dp[i][j] = dp[i+1][j-1] + 2
    else:
      dp[i][j] = max(dp[i][j-1], dp[i+1][j])

print(dp[0][N-1])