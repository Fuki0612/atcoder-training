N, D = map(int, input().split())

X = list(map(int, input().split()))

sorted_X = sorted(enumerate(X), key=lambda x: x[1])

count = 0
ans_list = []

for i in range(N):
  if i == 0:
    if sorted_X[i+1][1] - sorted_X[i][1] >= D:
      count += 1
      ans_list.append(sorted_X[i][0]+1)
      continue
  elif i == N-1:
    if sorted_X[i][1] - sorted_X[i-1][1] >= D:
      count += 1
      ans_list.append(sorted_X[i][0]+1)
      continue
  else: 
    if sorted_X[i][1] - sorted_X[i-1][1] >= D and sorted_X[i+1][1] - sorted_X[i][1] >= D:
      count += 1
      ans_list.append(sorted_X[i][0]+1)
      continue

print(count)
print(*sorted(ans_list)) 