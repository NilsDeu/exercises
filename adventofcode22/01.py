
score = 0
score2 = 0
tmp=''
ersatz = tmp.maketrans("ABCXYZ", "123123", "\n")

with open("02.data.txt") as daten:
    for zeile in daten:
        zeile = zeile.translate(ersatz)

        # 1 for Rock, 2 for Paper, and 3 for Scissors
        score += int(zeile[2])  

        # 0 if you lost, 3 if the round was a draw, and 6 if you won
        if zeile[0] == zeile[2]:
            score += 3
        elif int(zeile[0]) % 2 == int(zeile[2]) % 2:
            if int(zeile[2]) < int(zeile[0]):
                score +=6
        else:
            if int(zeile[2]) > int(zeile[0]):
                score +=6


print(f"Die Highscore für Teil Eins: {score}")
print(f"Die Highscore für Teil Zwei: {score2}")
