N, K = map(int, input().split())
A = list(map(int, input().split()))

num = [0] * (K)

for a in A:
  num[a-1] += 1

num.sort(reverse=True)
MAX = num[0]
ans = 0

for a in num:
  if MAX - a <= 1:
    ans += 1
  else:
    break

print(ans)