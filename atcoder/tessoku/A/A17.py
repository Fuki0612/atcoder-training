N = int(input())
A = [0,0] + list(map(int, input().split()))
B = [0,0,0] + list(map(int, input().split()))

dp = [0,0,A[2]]

for i in range(3,N+1):
  dp.append(min(dp[-1]+A[i], dp[-2]+B[i]))

ans = [N]

while ans[-1] > 1:
  if dp[ans[-1]-1] + A[ans[-1]] == dp[ans[-1]]:
    ans.append(ans[-1] - 1)
  else:
    ans.append(ans[-1] - 2)
ans.sort()

print(len(ans))
print(*ans)