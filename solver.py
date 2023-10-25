def solve(sudo):
    find = find_empty(sudo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(sudo, i, (row, col)):
            sudo[row][col] = i

            if solve(sudo):
                return True

            sudo[row][col] = 0

    return False


def valid(sudo, num, pos):
    # Check row
    for i in range(len(sudo[0])):
        if sudo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(sudo)):
        if sudo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if sudo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(sudo):
    for i in range(len(sudo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -  ")

        for j in range(len(sudo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(sudo[i][j])
            else:
                print(str(sudo[i][j]) + " ", end="")


def find_empty(sudo):
    for i in range(len(sudo)):
        for j in range(len(sudo[0])):
            if sudo[i][j] == 0:
                return (i, j)  # row, col

    return None

sudoku = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

print_board(sudoku)
solve(sudoku)
print("")
print_board(sudoku)
