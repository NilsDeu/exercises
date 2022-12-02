punkte = 0
tmp=''
# X lose, Y  draw, and Z win.
ersatz = tmp.maketrans("ABCXYZ", "123123", "\n")

with open("02.data.txt") as daten:
    for zeile in daten:
        zeile = zeile.translate(ersatz)

        # 1 for Rock, 2 for Paper, and 3 for Scissors
        punkte += int(zeile[2])  

        # 0 if you lost, 3 if the round was a draw, and 6 if you won
        if zeile[0] == zeile[2]:
            punkte += 3
        elif int(zeile[0]) % 2 == int(zeile[2]) % 2:
            if int(zeile[2]) < int(zeile[0]):
                punkte +=6
        else:
            if int(zeile[2]) > int(zeile[0]):
                punkte +=6

print(f"Die Highscore für Teil Eins: {punkte}")
