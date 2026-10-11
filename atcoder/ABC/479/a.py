N = int(input())
A = list(map(int, input().split()))

out = 0
for i in range(N):
  if i % 2 == 0:
    out += A[i]

print(out)