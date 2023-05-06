prev = 0
asc_count = 0

with open("input.txt") as data:
    for line in data:
        line = int(line)
        if line > prev and prev != 0:
            asc_count +=1
        prev = line
print(asc_count) 
    
