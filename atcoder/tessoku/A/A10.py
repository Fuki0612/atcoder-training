N = int(input())
A = list(map(int, input().split()))

leftA = [0]
rightA = [0]

for i in range(0,N):
  leftA.append(max(A[i],leftA[-1]))

for i in range(N-1,-1,-1):
  rightA.append(max(A[i],rightA[-1]))

leftA = leftA[1:]
rightA = list(reversed(rightA[1:]))

D = int(input())

out = []

for i in range(D):
  l, r = map(int, input().split())
  out.append(max(leftA[l-2],rightA[r]))

[print(i) for i in out]