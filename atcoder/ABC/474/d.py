N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = [1] * (N)

deficit = sum(max(0, B[j] - A[j]) for j in range(N))   

for i in range(N):
  if A[i] > B[i]:
    ans[i] += deficit
    print('Yes')
    print(*ans)
    exit()

print('No')