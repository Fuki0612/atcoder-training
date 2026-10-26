N = int(input())
L = list(map(int, input().split()))

INF = float('inf')
S = sum(L)
left = 0
right = S
ans = S

for i in range(0, N): 
  left  += L[i]
  right -= L[i]
  ans = min(ans, abs(left - right))

print(ans)