N = list(reversed(list(map(int, input()))))

ans = 0
for i,n in enumerate(N):
  if n == 1:
    ans += n * 2**i

print(ans)