N, S, L = map(int, input().split())

A = list(map(int, input().split()))

d = [0]
for x in A:
  d.append(d[-1] + x)

dl = [0] * S
dr = [0] * (N - S + 1)

for i in range(S):
  dl[i] = abs(d[S-1] - d[i])

for i in range(S, N):
  dr[i-S+1] = abs(d[S-1] - d[i])

ans = 0
j = 0
for i in range(S): 
  x = dl[i]
  if x > L : continue

  while j + 1 < len(dr) and (x + 2 * dr[j+1] <= L or 2 * x + dr[j+1] <= L): 
    j += 1
    
  ans = max(ans, S - i + j)

print(ans)
