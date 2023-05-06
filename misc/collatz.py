def collatz(current: int) -> int:
    """Berechnet die nächste Zahl der Collatzfolge"""
    return (current // 2, 3 * current + 1)[current % 2]


print("Das Collatz-Problem...")

zahl = 0
while zahl <= 0:
    eingabe = input("Bitte geben Sie eine positive Ganzzahl ein: ")
    try:
        zahl = int(eingabe)
    except ValueError:
        print("Das sieht nicht wie eine positive Ganzzahl aus")

folge = []
while True:
    folge.append(zahl)
    if zahl == 1 and len(folge) > 1:
        break
    zahl = collatz(zahl)

print(f"Ihre Collatz-Folge: {folge}")
