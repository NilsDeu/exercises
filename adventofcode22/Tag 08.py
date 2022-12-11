total_trees_visible = 0
scenic_score = 0
forest = []
x = y = 0

def is_visible(tree_X: int, tree_Y: int, height: int, forest: list) -> bool:
    '''Determine if a tree is visible from the outside of the grid.'''
    if tree_X == 0 or tree_Y == 0 or tree_X+1 == len(forest[0]) or tree_Y+1 == len(forest):
        return True #edge cases
    '''from left'''
    for a in range(0, tree_X):
        if not height > int(forest[tree_Y][a]):
            break
    else:
        return True
    '''from right'''
    for b in range(len(forest[tree_X])-1, tree_X, -1):
        if not height > int(forest[tree_Y][b]): 
            break
    else:
        return True
    '''from top'''
    for c in range(0, tree_Y):
        if not height > int(forest[c][tree_X]): 
            break
    else:
        return True
    '''from bottom'''
    for d in range(len(forest)-1, tree_Y, -1):
        if not height > int(forest[d][tree_X]):
            break
    else:
        return True

    return False # should never be reached

def get_scenic_score(tree_X: int, tree_Y: int, height: int, forest: list) -> int:
    ''' Get the scenic score for a tree.'''
    if tree_X == 0 or tree_Y == 0 or tree_X+1 == len(forest[0]) or tree_Y+1 == len(forest):
        return 0 # Edge case have at least one zero multiplier

    '''to left'''
    for a in range(tree_X-1, -1, -1):
        if not height > int(forest[tree_Y][a]):
            a = tree_X - a
            break
        else:
            a = tree_X
    '''to right'''
    for b in range(tree_X+1, len(forest[tree_X])):
        if not height > int(forest[tree_Y][b]):
            b = b - tree_X 
            break
        else:
            b = len(forest[tree_X]) - tree_X - 1
    '''up'''
    for c in range(tree_Y-1, -1, -1):
        if not height > int(forest[c][tree_X]):
            c = tree_Y - c
            break
        else:
            c = tree_Y
    '''down'''
    for d in range(tree_Y+1, len(forest)):
        if not height > int(forest[d][tree_X]):
            d = d- tree_Y
            break
        else:
            d = len(forest) - tree_Y - 1
    return a*b*c*d

''' Get grid data '''
with open("input.txt") as data:
    for tree_line in data:
        if not tree_line:
            continue
        forest.append(list(tree_line.replace("\n","")))

''' Compute '''
for line in forest:
    for tree in line:
        if is_visible(x, y, int(forest[y][x]), forest):
            total_trees_visible += 1
        s = get_scenic_score(x, y, int(forest[y][x]), forest)
        if s > scenic_score:
            scenic_score = s
        x += 1
    y += 1
    x = 0

print(f"{total_trees_visible} trees are visible from outside the grid.")
print(f"{scenic_score} is the highest scenic score possible for any tree.")
