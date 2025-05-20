import random


def print_board(board):
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


def checkWin(board, player):
    # 승리 조건을 좌표 리스트로 정의
    winConditions = [
        # 가로 승리 조건
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        # 세로 승리 조건
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        # 대각 승리 조건
        [0, 4, 8],
        [2, 4, 6],
    ]

    # 숭라 조건 체크
    for condition in winConditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False


board = [" "] * 9

while True:
    print_board(board)
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

    if checkWin(board, "o"):
        print_board(board)
        print("플레이어 승리")
        break
    elif checkWin(board, "x"):
        print_board(board)
        print("컴퓨터 승리")
        break
    else:
        print_board(board)
        print("무승부")
