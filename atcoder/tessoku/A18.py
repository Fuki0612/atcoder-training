N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (S+1) for i in range(N+1)]
dp[0][0] = 1

for i in range(N):
  for j in range(S+1):
    if dp[i][j] == 0 : continue
    dp[i+1][j] = 1
    if j + A[i] <= S:
      dp[i+1][j + A[i]] = 1

if dp[-1][-1] == 1:
  print('Yes')
else:
  print('No')