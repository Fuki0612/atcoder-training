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

pos = S
ans = []
for i in range(N,0,-1):
  if dp[i][S] > 0 and dp[i-1][S] == 0:
    ans.append(i)
    S -= A[i-1]

if len(ans) > 0:
  print(len(ans))
  print(*sorted(ans))
else:
  print(-1)