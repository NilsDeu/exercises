c=1
solution = ""
stack = []
crates = ["",[],[],[],[],[],[],[],[], []] # dummy string for moving the index
#part_two = False # switching between parts
part_two = True 

with open("input.txt") as data:
    for line in data:
        if not line:
            continue
        if c < 10:
            ''' populate the crates list '''
            if len(line) == 36 and line[1] != "1":
                if line[1] != " ":
                    crates[1].insert(0,line[1])
                for i in range(2,10):
                    if line[(i-1)*4+1] != " ":
                        crates[i].insert(0,line[(i-1)*4+1])
            c += 1
        else:
            ''' move the crates '''
            if line == '' or len(line) < 5:
                continue
            line = line.strip()
            line = line.split(" ")
            b = int(line[3])
            d = int(line[5])
            for i in range(0, int(line[1])):
                stack.append(crates[b][-1])
                del(crates[b][-1])
            if part_two:
                stack.reverse()
            crates[d] = crates[d] + stack
            stack = []

for crate in crates:
    if crate != "":
        solution = solution + crate[len(crate)-1]
print(solution)
