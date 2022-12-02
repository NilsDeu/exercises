# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won
punkte = 0

# X lose, Y  draw, and Z win.
ersatz=''
ersatz = ersatz.maketrans("ABCXYZ", "123VUG", "\n")

with open("input.txt") as daten:
    for zeile in daten:
        zeile = zeile.translate(ersatz)

        if zeile[2] == "U":
            punkte += 3 + int(zeile[0])
        elif zeile[2] == "V":
            print(punkte)
            punkte += (3 if int(zeile[0])-1 == 0 else int(zeile[0])-1)
            print(zeile, punkte)
        else:
            punkte += 6 + (1 if int(zeile[0])+1 == 4 else int(zeile[0])+1)

print(f"Die Highscore für Teil Zwei: {punkte}")
