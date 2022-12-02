kalorien = 0
elfen = []

with open("input.txt") as data:
    for line in data:
        if line == "\n":
            elfen.append(kalorien)
            kalorien = 0
        else:
            kalorien += int(line)
# vergessen! Durch die Leerzeile am Ende beim Kopieren aber
# trotzdem das richtige Ergebnis
elfen.append(kalorien)

top3 = 0
elfen_sortiert = sorted(elfen, key=int, reverse=True)
for i in range (0,3):
    top3 += elfen_sortiert[i]

print (f"Maximale Kalorien: {max(elfen)}")
print (f"Die Top 3 tragen : {top3} Kalorien")

# viel elegantere Lösungen:
# https://github.com/aspittel/advent-of-code/blob/main/2022/01/script.py
# https://luisnatera.com/posts/2022/12/advent-of-code-day-1/
