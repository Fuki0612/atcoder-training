N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))

l = 0
r = A[0] * K
pos = (l + r) // 2

def cul_sum(t):
  out = 0
  for a in A:
    out += t // a
  return out

while l != r:
  s = cul_sum(pos)
  if K <= s:
    r = pos
  else:
    l = pos + 1
  pos = (l + r) // 2

print(l)