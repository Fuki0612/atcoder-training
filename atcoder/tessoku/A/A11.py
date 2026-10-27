N, X = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = N-1

pos = (l+r) // 2
v = A[pos]

while v != X:
  if v < X:
    l = pos + 1
  if v > X:
    r = pos - 1
  pos = (l+r) // 2
  v = A[pos]

print(pos+1)