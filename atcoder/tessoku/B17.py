N = int(input())
h = [0] + list(map(int, input().split()))

INF = float('inf')
dp = [INF] * (N+1)
dp[1] = 0

for i in range(2,N+1):
  if i==2:
    dp[i] = dp[i-1] + abs(h[i] - h[i-1])
  else:
    dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]),dp[i-2] + abs(h[i] - h[i-2]))

ans = [N]

while ans[-1] > 1:
  pos = ans[-1]
  if abs(h[pos]-h[pos-1]) + dp[pos-1] == dp[pos]:
    ans.append(pos-1)
  else:
    ans.append(pos-2)
ans.sort()

print(len(ans))
print(*ans)