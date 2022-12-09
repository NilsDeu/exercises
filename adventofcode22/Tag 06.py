buffer = []
BUFFER_SIZE = 4 # part one
BUFFER_SIZE = 14 # part two

with open("input.txt") as data:
    for line in data:
        if not line:
            continue
        line = line.strip()
        for i in range(0, len(line)):
            ''' keep the buffer always at BUFFER_SIZE char '''
            buffer += line[i]
            if len(buffer) > BUFFER_SIZE:
                del(buffer[0])

            ''' check for duplicates '''
            if len(set(buffer)) == BUFFER_SIZE:
                print(i+1)
                print(buffer)
                break
