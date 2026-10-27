import bisect

N = int(input())
A = list(map(int, input().split()))
S = sorted(set(A))
B = []

for a in A:
  t = bisect.bisect_left(S,a)
  B.append(t+1)

print(*B)