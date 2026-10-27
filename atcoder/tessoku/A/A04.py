N = int(input())

ans = [0] * 10

n = N
for i in range(10):
  if n == 0 : break
  if n % 2 == 1:
    ans[-1-i] = 1
  n = n // 2

print(''.join(map(str, ans)))
