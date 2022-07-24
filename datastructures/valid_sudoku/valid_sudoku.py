def is_valid_sudoku(board) -> bool:
    mini_sections = [[] for x in range(9)]
    counter = 0
    padding = 0
    for i in range(9):
        j = 0
        if (i != 0) and (i % 3 == 0):
            counter = 0
            padding += 3
        else:
            counter = 0
        while j < 9 and counter < 9:
            if board[i][j] == '.' or (-1 < int(board[i][j]) < 10):
                mini_sections[counter+padding].append(board[i][j:j+3])
                counter += 1
                j += 3
            else:
                return False

    for i in range(9):
        vals = []
        for j in range(3):
            for k in range(3):
                if mini_sections[i][j][k].strip() == '.':
                    pass
                elif mini_sections[i][j][k].strip() in vals:
                    return False
                else:
                    vals.append(mini_sections[i][j][k])
    return True


#
# if __name__ == '__main__':
#     board = [(input("Please enter board "))]
#     print(board)
#     print(is_valid_sudoku(board))



