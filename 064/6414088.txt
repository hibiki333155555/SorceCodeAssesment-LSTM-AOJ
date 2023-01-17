dice = list(map(int, input().split()))
cmd = input()
for i in range(len(cmd)):
  if cmd[i] == 'N':
    dice[0], dice[1] = dice[1], dice[0]
    dice[1], dice[5] = dice[5], dice[1]
    dice[5], dice[4] = dice[4], dice[5]
  elif cmd[i] == 'E':
    dice[0], dice[3] = dice[3], dice[0]
    dice[3], dice[5] = dice[5], dice[3]
    dice[5], dice[2] = dice[2], dice[5]
  elif cmd[i] == 'W':
    dice[0], dice[2] = dice[2], dice[0]
    dice[2], dice[5] = dice[5], dice[2]
    dice[5], dice[3] = dice[3], dice[5]
  else:
    dice[0], dice[4] = dice[4], dice[0]
    dice[4], dice[5] = dice[5], dice[4]
    dice[5], dice[1] = dice[1], dice[5]
print(dice[0])
