from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

L = []
for a in A:
  k = bisect_left(L, a)
  if k == len(L):
    L.append(a)
  else:
    L[k] = a
print(len(L))