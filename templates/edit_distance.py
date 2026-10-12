"""
  編集距離（レーベンシュタイン距離）
  https://qiita.com/ktamido/items/d29362cf33dba0df6cb0

  文字列Sを文字列Tに変えるのに必要な最小操作回数を返す．
  操作は 挿入・削除・置換 の3種類（各コスト1）．
  dp[i][j] = Sの先頭i文字をTの先頭j文字に変える最小操作回数
  計算量: O(|S| * |T|)

  注意: 置換なし（挿入・削除のみ）なら |S| + |T| - 2 * LCS(S, T) になる
  使用例: 鉄則本 B20
"""

def edit_distance(s, t):
  n, m = len(s), len(t)
  dp = [[0] * (m+1) for _ in range(n+1)]
  for i in range(n+1):
    dp[i][0] = i          # i文字を全部削除
  for j in range(m+1):
    dp[0][j] = j          # j文字を全部挿入

  for i in range(1, n+1):
    for j in range(1, m+1):
      cost = 0 if s[i-1] == t[j-1] else 1
      dp[i][j] = min(
        dp[i-1][j] + 1,         # 削除
        dp[i][j-1] + 1,         # 挿入
        dp[i-1][j-1] + cost,    # 一致 or 置換
      )
  return dp[n][m]
