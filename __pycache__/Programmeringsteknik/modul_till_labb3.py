rader = 9
kolonner = 18

# Skapa en matris med koordinater
matris = [[f'{rad},{kol}' for kol in range(1, kolonner + 1)] for rad in range(1, rader + 1)]

# Skriv ut den skapade matrisen
for rad in matris:
    print(rad)
