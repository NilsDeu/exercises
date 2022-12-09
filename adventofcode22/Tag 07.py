dir_sizes = {}
curr_dir = []
dir_total = 0

under_threshold = 0
THRESHOLD = 100_000

DISK_SPACE = 70_000_000
UPDATE_SIZE = 30_000_000
bigger = []

def add_total(total: int, dir_list: list, dir_sizes: dict) -> dict:
    ''' Update each (parent) directory with the total size of current dir'''
    if total != 0:
        for directory in dir_list:
            dir_sizes[directory] += total
    return dir_sizes

def build_key(curr_dir: str, path: list) -> str:
    ''' Build a path from current dir + path of parent dir for using as a dict key.'''
    if len(path) > 1:
        return path[-1]+curr_dir
    else: #we are at the top dir
        return curr_dir

with open("input.txt") as data:
    for line in data:
        if not line:
            continue
        line = line.split()
        match line[0]:
            case "$": #commands
                if  line[1] == "ls":
                    pass
                elif line[2] == "..": # sum up current and delete dir
                    dir_sizes = add_total(dir_total, curr_dir, dir_sizes)
                    dir_total = 0
                    del(curr_dir[-1])
                else: # sum up previous! dir and add the new one
                    dir_sizes = add_total(dir_total, curr_dir, dir_sizes)
                    dir_total = 0
                    path = build_key(line[2], curr_dir)
                    curr_dir.append(path)
                    dir_sizes[path] = 0 #add dir to dict
            case "dir":
                pass
            case _: #not a dir or a cmd, should be a file
                dir_total += int(line[0])
    else:
        add_total(dir_total, curr_dir, dir_sizes)
        dir_total = 0

for size in dir_sizes.values():
    if size < THRESHOLD: #Part one
        under_threshold += size
    bigger.append(size) #Part two
print(f"The sum of the total sizes of those directories under {THRESHOLD} is {under_threshold}")

bigger = sorted(bigger)
FREE_SPACE = DISK_SPACE - bigger[-1]
SPACE_NEEDED = UPDATE_SIZE - FREE_SPACE
for size in bigger:
    if size >= SPACE_NEEDED:
        print(f"Space needed for the update: {SPACE_NEEDED}")
        print(f"Smallest dir for freeing enough: {size}")
        break
