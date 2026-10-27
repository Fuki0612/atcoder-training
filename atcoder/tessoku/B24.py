from bisect import bisect_left

N = int(input())
boxes = [tuple(map(int, input().split())) for _ in range(N)]
boxes.sort(key = lambda b:(b[0],-b[1]))

L = []

for x,y in boxes:
  k = bisect_left(L,y)
  if k == len(L):
    L.append(y)
  else:
    L[k] = y

print(len(L))