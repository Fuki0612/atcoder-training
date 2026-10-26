from collections import deque

N, M, K = map(int, input().split())
A = list(map(int, input().split()))

dp = deque([])
S = 0

ans = []

for i in range(N):
  if i-M+1 < 0:
    if S + A[i] <= K:
      dp.append(A[i])
      S += A[i]
      ans.append('Yes')
    else:
      dp.append(0)
      ans.append('No')
  else:
    if S + A[i] <= K:
      dp.append(A[i])
      ans.append('Yes')
      S += A[i]
    else:
      dp.append(0)
      ans.append('No')
    u = dp.popleft()
    S -= u

print("\n".join(map(str, ans)))