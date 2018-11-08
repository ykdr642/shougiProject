def makeBoard():
    row = ["ロ" for i in range(9)]
    board = [row[:] for i in range(9)]
    row = ['歩' for i in range(9)]
    board[2] = row[:]
    board[6] = row[:]
    board[0][0] = "香"
    board[8][0] = "香"
    board[0][8] = "香"
    board[8][8] = "香"
    board[0][1] = "桂"
    board[0][7] = "桂"
    board[8][1] = "桂"
    board[8][7] = "桂"
    board[0][2] = "銀"
    board[0][6] = "銀"
    board[8][2] = "銀"
    board[8][6] = "銀"
    board[0][3] = "金"
    board[0][5] = "金"
    board[8][3] = "金"
    board[8][5] = "金"
    board[0][4] = "王"
    board[8][4] = "玉"
    board[1][1] = "飛"
    board[7][7] = "飛"
    board[1][7] = "角"
    board[7][1] = "角"
    return board

def look(board:list):
    count = 0
    for i in board:
        for j in i:
            if j is not "ロ" and count > 4:
                print(j,end="")
            elif j is not "ロ":
                print(j ,end="")
            else:
                print(j,end="")
        print("")
        count += 1
    print("")

def change(a,board):
    board[6][2] = "ロ"
    board[5][2] = "歩"
    return board

def main():
    print("")
    print("")
    board = makeBoard()
    look(board)
    print("先手")
    a = input()
    print("")
    print("")
    nextboard = change(a,board)
    look(nextboard)
    print("後手")
    a = input()
    print("そこには動かせません")
    print("")
    look(nextboard)
    print("後手")

main()


