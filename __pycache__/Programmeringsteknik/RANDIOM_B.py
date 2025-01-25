import random

class Atom:
    def __init__(self, atombeteckning, atomvikt, rad, kolonn):
        self.atombeteckning = atombeteckning
        self.atomvikt = atomvikt
        self.atomnummer = None 
        self.rad = rad
        self.kolonn = kolonn
    
    def __str__(self):
        return f"{self.atomnummer} {self.atombeteckning} {self.atomvikt} || Kolonn: {self.kolonn} Rad: {self.rad}"

class Atomlista:
    def __init__(self):
        self.atomlista = []

    def skriv_ut_atomerna(self, filnamn='Atomer_UppgB.txt'):
        with open(filnamn, 'r') as fil:
            for line in fil:
                data = line.strip().split()
                if len(data) == 4:
                    atom = Atom(data[0], float(data[1]), int(data[2]), int(data[3])) 
                    self.atomlista.append(atom)

        self.atomlista = sorted(self.atomlista, key=lambda x: x.atomvikt)
        for i, atom in enumerate(self.atomlista, start=1):
            atom.atomnummer = i  
            print(f"{atom}")

    def spel_1(self):
        slumpens_atom = random.choice(self.atomlista)
        i = 0
        while True:
            try:
                guessed_atomnummer = int(input(f"Gissa atomnumret för {slumpens_atom.atombeteckning}: "))
                if guessed_atomnummer == slumpens_atom.atomnummer:
                    print("Rätt gissat!")
                    break
                elif i == 2:
                    print(f"Du har inga försök kvar, rätt svar var {slumpens_atom.atomnummer}")
                    break
                elif not 1 <= guessed_atomnummer <= 103:
                    print("Endast tal mellan 1 och 103, pröva igen.")
                else:
                    i += 1
                    print(f"Fel, du har {3-i} försök kvar.\n")
            except ValueError:
                print("Du måste skriva siffror")

    def spel_2(self):
        slumpens_atombeteckning = random.choice(self.atomlista)
        i = 0
    
        while True:
            try:
                guessed_atombeteckning = str(input(f"Gissa atombeteckningen för {slumpens_atombeteckning.atomnummer}: "))
                if guessed_atombeteckning.lower() == slumpens_atombeteckning.atombeteckning.lower():
                    print("Rätt gissat!")
                    break
                elif i == 2:
                    print(f"Du har inga försök kvar, rätt svar var {slumpens_atombeteckning.atombeteckning}")
                    break
                else:
                    i += 1
                    print(f"Fel, du har {3-i} försök kvar.\n")
            except ValueError:
                print("Du måste skriva bokstäver")

    def spel_3(self):
        en_slumpvald_atom_A = random.choice(self.atomlista)
        self.atomlista.remove(en_slumpvald_atom_A)
        en_slumpvald_atom_B = random.choice(self.atomlista)
        self.atomlista.remove(en_slumpvald_atom_B)
        en_slumpvald_atom_C = random.choice(self.atomlista)

        slumpmässiga_atomer = [en_slumpvald_atom_A, en_slumpvald_atom_B, en_slumpvald_atom_C]
        slumpad_atom = random.choice(slumpmässiga_atomer)

        while True:
            try:
                print(f"Vad har atomen {slumpad_atom.atombeteckning} för atomvikt?")
                print("Välj mellan dessa tre alternativ:")
                svar = input(f"A. {en_slumpvald_atom_A.atomvikt}   B. {en_slumpvald_atom_B.atomvikt}   C. {en_slumpvald_atom_C.atomvikt}\nSvar: ")
                if svar.upper() == 'A':
                    vald_vikt = en_slumpvald_atom_A.atomvikt
                elif svar.upper() == 'B':
                    vald_vikt = en_slumpvald_atom_B.atomvikt
                elif svar.upper() == 'C':
                    vald_vikt = en_slumpvald_atom_C.atomvikt
        
                if vald_vikt == slumpad_atom.atomvikt:
                    print("Rätt gissat!")
                    break
                else:
                    print(f"Fel, rätt svar var {slumpad_atom.atomvikt}")
                    break
            except UnboundLocalError:
                print()
                print("Ogiltigt val. Du måste välja A, B eller C.")
                print()

    def spel_4(self):
        periodiska_systemet = Atomlista()
        periodiska_systemet.skriv_ut_atomerna('Atomer_UppgB.txt')

        matris = [['' for _ in range(18)] for _ in range(9)]
        rader = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        kolonner = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

        for i, rad in enumerate(rader):
            for j, kol in enumerate(kolonner):
                matris[i][j] = f'{rad},{kol}'

        for rad in matris:
            print(rad)

        while True:
            atom = random.choice(periodiska_systemet.atomlista)
            periodiska_systemet.atomlista.remove(atom)

            while True:
                print(f"\nVart i det periodiska systemet ligger: {atom.atombeteckning}")
                atomrad = input("\nVilken rad ligger atomen på?")
                atomkolonn = input("Vilken kolonn?")

                if not atomrad.isdigit() or not atomkolonn.isdigit():
                    print("Det var inget alternativ, försök igen!")
                    continue
                elif not 0 < int(atomrad) <= 9 or not 0 < int(atomkolonn) <= 18:
                    print("\nFelaktigt intervall, rad mellan 1-9 och kolonn mellan 1-18. Försök igen!\n")
                    continue
                elif int(atomrad) == atom.rad and int(atomkolonn.strip()) == atom.kolonn:
                    print("\nRätt!!")

                    tillägg_i_systemet = [['' for _ in range(18)] for _ in range(9)]
                    for i, rad in enumerate(rader):
                        for j, kol in enumerate(kolonner):
                            if int(atomrad) == i + 1 and int(atomkolonn) == j + 1:
                                tillägg_i_systemet[i][j] = atom.atombeteckning

                    for i, rad in enumerate(tillägg_i_systemet, start=1):
                        rad_str = [f'{i},{kol}' if not cell else cell for kol, cell in enumerate(rad, start=1)]
                        print(rad_str)
                    break
                else:
                    print("\nFel!")
                    True

atom_lista_objekt = Atomlista()

print("-------------- MENY ---------------")
print("1. Visa alla atomer\n2. Träna på atomnummer\n3. Träna på atombeteckningar\n4. Träna på atomvikter\n5. Träna på periodiska systemet\n6. Sluta\n-----------------------------------")

def huvudprogram():
    while True:
        try:
            aktivitet = int(input("Vad vill du göra?: "))
            if aktivitet == 1:
                print("Okej, här är alla atomerna:")
                print()
                atom_lista_objekt.skriv_ut_atomerna('Atomer_UppgB.txt')
            elif aktivitet == 2:
                print("Okej, dags att träna på atomnummer!")
                print()
                atom_lista_objekt.spel_1()
            elif aktivitet == 3:
                print("Okej, dags att träna på atombeteckningarna!")
                print()
                atom_lista_objekt.spel_2()
            elif aktivitet == 4:
                print ("Okej,dags att träna på atomvikter!")
                print()
                atom_lista_objekt.spel_3()
            elif aktivitet == 5:
                print("Okej, dags att träna på att placera atomer i periodiska systemet!")
                print()
                atom_lista_objekt.spel_4()
            elif aktivitet == 6:
                exit(0)
            else:
                print("Inget möjligt val, försök igen")
        except ValueError:
            print ("Välj en siffra mellan 1 till 5")

huvudprogram()
