priority_sum=0
badge_sum = 0

counter = 1
group=[]
with open("input.txt") as input:
    for line in input:
        
        ''' Part 1 '''
        half = len(line)//2
        diff_set = set(line[:half]).intersection(line[half:])
        for diff in diff_set:
            diff = ord(diff)
            priority_sum += diff - 96 if diff >= 97 else diff - 38

        ''' All below is Part 2 '''
        if counter == 4:
            badge_set = set(group[0]).intersection(set(group[1]).intersection(group[2]))
            for badge in badge_set:
                badge = ord(badge)
                badge_sum += badge - 96 if badge >= 97 else badge - 38 
            group = []
            counter = 1
        group.append(line.replace("\n",""))
        counter +=1
    else:
        badge_set = set(group[0]).intersection(set(group[1]).intersection(group[2]))
        for badge in badge_set:
            badge = ord(badge)
            badge_sum += badge - 96 if badge >= 97 else badge - 38
            
print(f"1: What is the sum of the priorities of those item types? {priority_sum}")
print(f"2: What is the sum of the priorities of (the badges) item types? {badge_sum}")      
