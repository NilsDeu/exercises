"""""""""""""""""""""""""""""""""""""""""""""
 Day  9: Rope Bridge // Advent of Code 2022
"""""""""""""""""""""""""""""""""""""""""""""

tail_position = (0,0)
all_tail_positions = {(0, 0)}
head_positions = [[0,0]]

long_rope = [[[0,0], [0,0]], [[0,0], [0,0]], [[0,0], [0,0]], [[0,0], [0,0]], [[0,0], [0,0]], [[0,0], [0,0]], [[0,0], [0,0]], [[0,0], [0,0]], [[0,0], [0,0]], [[0,0], [0,0]]]
all_long_positions = {(0, 0)}


def move_head(direction: str, head_positions: list[list]) -> list[list]:
    '''Move the head of the rope, return current and last position.'''
    match direction:
        case "L":
            head_positions.append([head_positions[-1][0]-1, head_positions[-1][1]])
        case "R":
            head_positions.append([head_positions[-1][0]+1, head_positions[-1][1]])
        case "U":
            head_positions.append([head_positions[-1][0], head_positions[-1][1]+1])
        case "D":
            head_positions.append([head_positions[-1][0], head_positions[-1][1]-1])
    return head_positions[-2:]


def move_tail(head_positions: list[list], tail_position: list) -> tuple:
    ''' Move the tail of the rope.'''
    if tail_position == head_positions[1]:
        #print("o")
        return tail_position
    elif abs(head_positions[1][0] - tail_position[0]) <= 1 and abs(head_positions[1][1] - tail_position[1]) <= 1:
        #print("p")
        return tail_position
    else:
        #print("m")
        return tuple(head_positions[0])


def print_rope(line: str, head_pos: list, tail_pos: list, all_tail_pos: dict[tuple], whole_grid: bool = False) -> None:
    ''' Print the grid and all tail movement '''   
    grid_x_max = grid_y_max = grid_x_min = grid_y_min = 0
    if whole_grid:
        for i in range(0, len(all_tail_pos)):
            if all_tail_pos[i][0] == grid_x_max:
                grid_x_max = all_tail_pos[i][0] + 1
            elif all_tail_pos[i][0] < grid_x_min:
                grid_x_min = all_tail_pos[i][0]
            if all_tail_pos[i][1] > grid_y_max:
                grid_y_max = all_tail_pos[i][1] 
            elif all_tail_pos[i][1] == grid_y_min:
                grid_y_min = all_tail_pos[i][1] - 1
    else: # only print between start and current
        grid_x_min = min(grid_x_min, tail_pos[1][0])
        grid_x_max = max(grid_x_max, tail_pos[1][0]) + 1
        grid_y_min = min(grid_y_min, tail_pos[1][1]) - 1
        grid_y_max = max(grid_y_max, tail_pos[1][1])

    grid_x_max = max(grid_x_max, head_pos[1][0]) + 1
    grid_x_min = min(grid_x_min, head_pos[1][0])
    grid_y_max = max(grid_y_max, head_pos[1][1])
    grid_y_min = min(grid_y_min, head_pos[1][1]) - 1

    print(f"###{line}###")
    for col in range(grid_y_max, grid_y_min, -1):
        for row in range(grid_x_min, grid_x_max):
            token = "."
            if [row, col] in all_tail_pos:
                token = "#"
            if [row, col] == [0, 0]:
                token = "s"
            if [row, col] == tail_pos:
                token = "t"
            if [row, col] == head_pos[-1]:
                token = "h"

            print(token, end="")
        print()


def move_long_rope(direction: str, rope: dict) -> dict[tuple]:
    '''Move a rope longer then only head/tail one field in a given direction.'''
    rope[0] = move_head(direction, rope[0])
    for j in range(1,9):
        rope[j][0] = rope[j][1] 
        rope[j][1] = list(move_tail(rope[j-1], rope[j][0]))
        if rope[j][0] == rope[j][1]:
            break
    print(rope)
    return rope

with open("test.txt") as data:
    for line in data:
        if not line:
            continue
        else:
            line = line.replace("\n","")
            direction, length = line.split(" ")
        print(line)
        for i in range(0, int(length)):
            # part 1
            head_positions = move_head(direction, head_positions)
            tail_position = move_tail(head_positions, tail_position)
            all_tail_positions.add(tail_position)
            # part 2
            long_rope = move_long_rope(direction, long_rope)
            all_long_positions.add(tuple(long_rope[9][1]))

            #print_rope(line, head_positions, tail_position, all_tail_positions, True)
            
print(f"The tail of the rope visits {len(all_tail_positions)} positions at least once.")
print(f"The tail of the rope with 10 knots visits {len(all_long_positions)} positions at least once.")
