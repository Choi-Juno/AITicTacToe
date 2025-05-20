import random

board = [" "] * 9

while True:
    print(
        f"""
    |---|---|---|
    | {board[0]} | {board[1]} | {board[2]} |
    |---|---|---|
    | {board[3]} | {board[4]} | {board[5]} |
    |---|---|---|
    | {board[6]} | {board[7]} | {board[8]} |
    |---|---|---|
"""
    )
    position = int(input("위치를 입력하세요 (1 - 9) 종료는 0 입력: "))

    if board[position - 1] == "o" or board[position - 1] == "x":
        print("해당 위치에는 둘 수 없습니다.")
        continue

    if position == 0:
        print("게임을 종료합니다.")
        break

    board[position - 1] = "o"

    while True:
        computerPosition = random.randint(0, 8)
        if board[computerPosition] == " ":
            board[computerPosition] = "x"
            break

    # 승리 조건 체크 전에 보드판 출력
    print(
        f"""
    |---|---|---|
    | {board[0]} | {board[1]} | {board[2]} |
    |---|---|---|
    | {board[3]} | {board[4]} | {board[5]} |
    |---|---|---|
    | {board[6]} | {board[7]} | {board[8]} |
    |---|---|---|
"""
    )

    if board[0] == "o" and board[1] == "o" and board[2] == "o":
        print("플레이어 승리")
        break
    elif board[3] == "o" and board[4] == "o" and board[5] == "o":
        print("플레이어 승리")
        break
    elif board[6] == "o" and board[7] == "o" and board[8] == "o":
        print("플레이어 승리")
        break
    elif board[0] == "o" and board[3] == "o" and board[6] == "o":
        print("플레이어 승리")
        break
    elif board[1] == "o" and board[4] == "o" and board[7] == "o":
        print("플레이어 승리")
        break
    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        print("플레이어 승리")
        break
