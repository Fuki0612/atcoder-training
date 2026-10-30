a, b = map(int, input().split())
MOD = 1000000007

out = 1     
p = a % MOD
while b > 0:
  if b & 1:          # b の一番下の桁が 1 なら掛ける
    out = out * p % MOD
  p = p * p % MOD    # 次の桁用に2乗する
  b >>= 1            # b を1桁右にずらす
print(out)