from bisect import bisect_right 

N, M, K = map(int, input().split())
X, Y = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

bills = [0]
prices = [0]

for b in B:
  price = prices[-1] + b
  bill = -(-b // K) + bills[-1]
  if bill > Y or price > K * Y:
    break
  prices.append(price)
  bills.append(bill)

desert = [0]
for i in range(N):
  desert.append(desert[-1] + A[i])

ans = 0
for i in range(len(prices)):
  R = X + K * Y - prices[i]
  index = bisect_right(desert,R)
  ans = max(index - 1 + i, ans)

print(ans)