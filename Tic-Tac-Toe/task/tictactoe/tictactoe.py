# write your code here
current_player = "X"


def print_grid(grid: str):
    for i in range(0, 3):
        if i == 0:
            print("---------")
        for j in range(0, 3):
            if j == 0:
                print("| ", end="")
            print(f"{grid[i * 3 + j]} ", end="")
            if j == 2:
                print("|")
        if i == 2:
            print("---------")


def analyse_result(grid):
    grid_ = list(grid)
    grid = [grid_[0:3], grid_[3:6], grid_[6:]]

    # Check winner in rows
    winners = []
    for row in grid:
        if row[0] == row[1] and row[0] == row[2] and "_" not in row:
            winners.append(row[0])

    # Check winner in columns
    for col in range(0, 3):
        if all([grid[row][col] == "X" for row in range(0, 3)]):
            winners.append(grid[0][col])
        if all([grid[row][col] == "O" for row in range(0, 3)]):
            winners.append(grid[0][col])

    # Check winner in diagonals
    if (grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2]) or \
            (grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0]):
        if grid[1][1] != "_":
            winners.append(grid[1][1])

    # Check for impossible state
    if 1 < len(winners) != winners.count("X") or abs(grid_.count("X") - grid_.count("O")) >= 2:
        print(winners.count("X"))
        print("Impossible")
        return 1
    elif len(winners) == 1:
        print(f"{winners[0]} wins")
        return 1

    if any(["_" in row for row in grid]):
        print("Game not finished")
        return 0
    else:
        print("Draw")
        return 1


def player_makes_move(grid):
    global current_player
    grid = str_to_mat(grid)
    while True:
        move = input("Enter the coordinates:").split()
        for coord in move:
            if not coord.isnumeric():
                print_grid("You should enter numbers!")
                continue
        row, col = int(move[0]) - 1, int(move[1]) - 1

        if row not in range(0, 3) or col not in range(0, 3):
            print("Coordinates should be from 1 to 3!")
            continue

        if grid[row][col] != "_":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            grid[row][col] = current_player
            current_player = "X" if current_player == "O" else "O"
            break

    return mat_to_str(grid)


def str_to_mat(grid: str) -> list:
    grid = list(grid)
    return [grid[0:3], grid[3:6], grid[6:]]


def mat_to_str(grid: list) -> str:
    return "".join([str(cell) for row in grid for cell in row])


def main():
    grid = "_________"
    while True:
        print_grid(grid)
        if analyse_result(grid) == 1:
            break
        grid = player_makes_move(grid)


main()
