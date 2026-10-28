N = int(input())

a = 1
b = 1

for i in range(N-2):
  t = (a+b) % 1000000007
  a = b
  b = t

print(b)