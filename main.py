import random



def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def color_grid(rows, col):
    rows, cols = (rows, col)
    grid = [[random_color() for i in range(cols)] for j in range(rows)]

    return grid



rows = 5
columns = 3

input = color_grid(rows,columns)

print('Color Grid ------ \n')
for r in input:
    print(r)
print('-----------------------\n')

visited = [[0 for j in range(columns)] for i in range(rows)]
result = [[0 for j in range(columns)] for i in range(rows)]
COUNT = 0


def is_valid(new_row_cell, new_col_cell, key, input):
    try:
        if (new_row_cell < rows and new_col_cell < columns and new_row_cell >= 0 and new_col_cell >= 0):
            v = visited[new_row_cell][new_col_cell]
            k = input[new_row_cell][new_col_cell]
            if (v == 0 and k == key):
                return True;
            else:
                return False;
        else:
            return False;
    except Exception as e:
        raise e



def search(rc, rc_n, i, j, input):
    global COUNT

    if (rc != rc_n):
        return

    visited[i][j] = 1;
    COUNT += 1

    cel_mov_in_row = [0, 0, 1, -1]
    cel_mov_in_col = [1, -1, 0, 0]

    for u in range(4):
        if (is_valid(i + cel_mov_in_col[u], j + cel_mov_in_row[u], rc, input)):
            search(rc, rc_n, i + cel_mov_in_col[u], j + cel_mov_in_row[u], input)

def reset_visited():
    for i in range(rows):
        for j in range(columns):
            visited[i][j] = 0

def reset_result(key, input):
    for i in range(rows):
        for j in range(columns):
            if (visited[i][j] != 0 and input[i][j] == key):
                result[i][j] = visited[i][j]
            else:
                result[i][j] = 0


def print_result(res):
    print(f'The largest connected component of the grid is : {res}');
    for i in range(rows):
        for j in range(columns):
            if (result[i][j] != 0):
                print('x', end=' ')
            else:
                print('. ', end='')
        print()


def computeLargestConnectedGrid(input):
    global COUNT
    current_max = 0

    for i in range(rows):
        for j in range(columns):
            reset_visited()
            COUNT = 0

            if (j + 1 < columns):
                search(input[i][j], input[i][j + 1], i, j, input)

            if (COUNT >= current_max):
                current_max = COUNT
                reset_result(input[i][j], input)

            reset_visited()
            COUNT = 0

            if (i + 1 < rows):
                search(input[i][j], input[i + 1][j], i, j, input)

            if (COUNT >= current_max):
                current_max = COUNT
                reset_result(input[i][j], input)

    print_result(current_max)


computeLargestConnectedGrid(input)