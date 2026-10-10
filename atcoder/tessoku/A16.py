N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0,A[0]]

for i in range(3,N+1):
  dp.append(min(dp[-2]+B[i-3], dp[-1]+A[i-2]))

print(dp[-1])