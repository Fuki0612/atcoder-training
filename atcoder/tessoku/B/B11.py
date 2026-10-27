from bisect import bisect_left 

N = int(input())
A = sorted(list(map(int, input().split())))

Q = int(input())

out = []

for i in range(Q):
  X = int(input())
  pos = bisect_left(A,X)
  out.append(pos)

[print(i) for i in out]