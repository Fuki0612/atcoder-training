S = input()
T = input()

if S[0] in ('A','D') and T[1] in ('A','D'):
  print('No')
elif S[1] in ('A','D') and T[0] in ('A','D'):
  print('No')
else:
  print('Yes')