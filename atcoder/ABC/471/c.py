from bisect import bisect_left,bisect_right

N = int(input())
A = sorted(list(map(int, input().split()))+[0])

INF = float('inf')

A = [-INF] + A + [INF]

pos = 0

left = bisect_left(A,pos) - 1
right = bisect_right(A,pos)

out = 0
for i in range(N):
  if A[right] - pos < pos - A[left]:
    out += A[right] - pos
    pos = A[right]
    right += 1
  else:
    out += pos - A[left]
    pos = A[left]
    left -= 1

print(out)