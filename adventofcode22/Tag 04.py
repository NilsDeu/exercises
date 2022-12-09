
input ="""
"""

counter = 0
counter2 = 0

for line in input.split("\n"):
  list = line.split(",")
  if(len(list) < 2):
    continue
  one = list[0].split("-")
  two = list[1].split("-")
  if (int(one[0]) >= int(two[0]) and int(one[1]) <= int(two[1])) or (int(one[0]) <= int(two[0]) and int(one[1]) >= int(two[1])):
    counter += 1
  if(int(one[1]) >= int(two[0]) >=int(one[0])) or (int(one[1]) >= int(two[1]) >= int(one[0])) or (int(two[1]) >= int(one[1]) >= int(two[0])):
    counter2 += 1
  else:
    print(list)
print(counter2)
