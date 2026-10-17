N, M = map(int, input().split())
NEG = -float('inf')
dp = [[NEG] * (2**N) for _ in range(M+1)]
dp[0][0] = 0

def calcIndex(A):
  ret = 0
  for i in range(len(A)):
    ret += 2**i * A[i]
  return ret

for i in range(M):
  A = list(map(int, input().split()))
  index = calcIndex(A)

print("\n".join(map(str, dp)))