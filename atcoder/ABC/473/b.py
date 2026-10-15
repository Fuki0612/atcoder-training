N = int(input())
A = list(map(int, input().split()))

dic = {}

for a in A:
  if a in dic:
    dic[a] += 1
  else:
    dic[a] = 1

ans = 0

for k,v in dic.items():
  if v%2 == 1:
    ans += k

print(ans)