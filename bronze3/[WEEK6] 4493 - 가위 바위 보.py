t = int(input())

for i in range(t):
    winP1 = 0  # Player1 이긴횟수
    winP2 = 0  # Player2 이긴횟수
    n = int(input())
    for j in range(n):
        p1, p2 = map(str, input().split())
        if p1 == 'R':
            if p2 == 'S':
                winP1 += 1
            elif p2 == 'P':
                winP2 += 1
        elif p1 == 'S':
            if p2 == 'P':
                winP1 += 1
            elif p2 == 'R':
                winP2 += 1
        elif p1 == 'P':
            if p2 == 'R':
                winP1 += 1
            elif p2 == 'S':
                winP2 += 1
    if winP1 > winP2:
        print('Player 1')
    elif winP1 < winP2:
        print('Player 2')
    elif winP1 == winP2:
        print('TIE')
