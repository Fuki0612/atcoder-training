from bisect import bisect_left

Q = int(input())
S = input()
T = input()

def kmp(s, t):
  m = len(t)
  fail = [0]*(m+1)
  fail[0] = -1
  k = -1
  for i in range(m):
    while k >= 0 and t[k] != t[i]:
      k = fail[k]
    k += 1
    fail[i+1] = k

  res = []
  r = 0        
  for i in range(len(s)):
    while r >= 0 and (r == m or t[r] != s[i]):
      r = fail[r]
    r += 1
    if r == m:
      res.append(i - m + 1)
  return res

m = len(T)
kmp_res = kmp(S, T)
ans = []
for _ in range(Q):
  l, r = map(int, input().split())
  j = bisect_left(kmp_res, l-1)
  if j < len(kmp_res) and kmp_res[j] <= r - m:
    ans.append("Yes")
  else:
    ans.append("No")

print("\n".join(ans))