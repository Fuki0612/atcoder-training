N = int(input())
A = list(map(int, input().split()))

out = 0

for i in range(N//2,N):
  out += A[i]

print(out)