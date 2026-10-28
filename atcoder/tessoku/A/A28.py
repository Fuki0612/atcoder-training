N = int(input())

out = 0
ans = []

for i in range(N):
  T,A = input().split()
  if T == '+':
    out += int(A)
  elif T == '-':
    out -= int(A)
  else:
    out *= int(A)
  out %= 10000
  ans.append(out)

print("\n".join(map(str, ans)))