N, K = map(int, input().split())
A = [0] * N
out = []

def dfs(i, rem): # i: 今決める位置、rem: 残りの和
  if i == N:
    if rem == 0:
      out.append(' '.join(map(str, A)))
    return
  w = i + 1
  for a in range(rem // w + 1):
    A[i] = a
    dfs(i + 1, rem - w * a)
  A[i] = 0

dfs(0, K) 
print('\n'.join(out))