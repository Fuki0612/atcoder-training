N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (S+1) for i in range(N+1)]


print("\n".join(map(str, dp)))