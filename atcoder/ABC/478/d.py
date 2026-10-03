from collections import defaultdict

N, Q = map(int, input().split())

diff = [[] for i in range(N+1)]

def merge(intervals):
  intervals.sort()
  res = []
  cl, cr = intervals[0]
  for l, r in intervals[1:]:
    if l <= cr:
      cr = max(cr, r)
    else:
      res.append((cl, cr))
      cl, cr = l, r
  res.append((cl, cr))
  return res   


groups = defaultdict(list)
for _ in range(Q):
  l, r, x = map(int, input().split())
  groups[x].append((l, r))  

s = [0] * (N+2)
for intervals in groups.values():
  for l, r in merge(intervals):
    s[l] += 1
    s[r+1] -= 1  
dp = [0]
for x in s[1:-1]:
  dp.append(dp[-1] + x)

print(*dp[1:])


