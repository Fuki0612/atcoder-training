N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

NEG = -float('inf')
point = [NEG] * (N+1)
point[1] = 0

for i in range(1,N):
  if point[i] == NEG : continue 
  point[A[i]] = max(point[A[i]],point[i]+100)
  point[B[i]] = max(point[B[i]],point[i]+150)

print(point[-1])