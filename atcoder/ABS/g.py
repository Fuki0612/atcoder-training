N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

out = 0

for i in range(N):
  if i % 2 == 0:
    out += a[i]
  else:
    out -= a[i]

print(out)