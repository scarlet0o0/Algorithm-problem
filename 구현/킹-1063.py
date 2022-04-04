king, pawn, n = input().split()
command_arr = [input() for _ in range(int(n))]
v = ['0','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
king_xy = [v.index(king[0]), int(king[1])]
pawn_xy = [v.index(pawn[0]), int(pawn[1])]

for command in command_arr:
    if command == 'R':
        x, y = (1,0)
    elif command == 'L':
        x, y = (-1,0)
    elif command == 'B':
        x, y = (0,-1)
    elif command == 'T':
        x, y = (0,1)
    elif command == 'RT':
        x, y = (1,1)
    elif command == 'LT':
        x, y = (-1,1)
    elif command == 'RB':
        x, y = (1,-1)
    elif command == 'LB':
        x, y = (-1,-1)

    if (king_xy[0]+x) == pawn_xy[0] and (king_xy[1]+y) == pawn_xy[1]:
        if 0 < (king_xy[0] + x) < 9 and 0 < (king_xy[1] + y) < 9 \
                and 0 < (pawn_xy[0] + x) < 9 and 0 < (pawn_xy[1] + y) < 9:
            king_xy[0] += x
            king_xy[1] += y
            pawn_xy[0] += x
            pawn_xy[1] += y
    else:
        if 0 < (king_xy[0] + x) < 9 and 0 < (king_xy[1] + y) < 9:
            king_xy[0] += x
            king_xy[1] += y

print(str(v[king_xy[0]])+str(king_xy[1]))
print(str(v[pawn_xy[0]])+str(pawn_xy[1]))
