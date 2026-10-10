N = int(input())
P = list(map(int, input().split()))

count = N // 10

for i in range(count):
  if max(P[10*i:10*(i+1)]) != 10*(i+1) or min(P[10*i:10*(i+1)]) != 10*i+1:
    print('No')
    exit()

if N % 10 != 0:
  if max(P[10*(N//10):]) != N or min(P[10*(N//10):]) != 10*(N//10)+1:
    print('No')
    exit()

print('Yes')