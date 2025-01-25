import random


class Atom:
    def __init__(self, atombeteckning, atomvikt, rad, kolonn):
        self.atombeteckning = atombeteckning
        self.atomvikt = atomvikt
        self.atomnummer = None 
        self.rad = rad
        self.kolonn = kolonn
    #Så här ska atomerna se ut när jag printar listan
    def __str__(self):
        return f"{self.atomnummer}  {self.atombeteckning}  {self.atomvikt} || Kolonn: {self.kolonn} Rad: {self.rad}" 

class Atomlista:
    def __init__(self, atomfil='Atomer_UppgB.txt'):
        self.atomlista = []
        self.atomfil = atomfil

    def listan_av_atomerna(self, atomfil='Atomer_UppgB.txt'):
        self.atomlista=[]
        with open(atomfil, 'r') as fil:
            for line in fil:
                data = line.strip().split()
                if len(data) == 4:
                    atom = Atom(data[0], float(data[1]), int(data[2]), int(data[3])) 
                    self.atomlista.append(atom)

        self.atomlista = sorted(self.atomlista, key=lambda x: x.atomvikt) #Sorterar så atomerna är i ordning
        for i, atom in enumerate(self.atomlista, start=1): #Så atomerna får siffror baserat på ordning
                atom.atomnummer = i  
        
        #Dessa ska byta plats
        self.ändra_position('Th', 'Pa')
        self.ändra_position('Co', 'Ni')
        self.ändra_position('Ar', 'K')
        self.ändra_position('Te', 'I')
        self.ändra_position('U', 'Np')
  
    def ändra_position(self, första_beteckning, andra_beteckning):
        första_atomen = next(atom for atom in self.atomlista if atom.atombeteckning == första_beteckning)
        andra_atomen = next(atom for atom in self.atomlista if atom.atombeteckning == andra_beteckning)

        position1, position2 = self.atomlista.index(första_atomen), self.atomlista.index(andra_atomen)
        self.atomlista[position1], self.atomlista[position2] = self.atomlista[position2], self.atomlista[position1]

        första_atomen.atomnummer, andra_atomen.atomnummer = andra_atomen.atomnummer, första_atomen.atomnummer

    def skriv_ut_atomerna(self): #Denna funktion skriver ut atomerna
        self.listan_av_atomerna()
        for atom in self.atomlista:
            print(f"{atom}")

    def spel_1(self):
        self.listan_av_atomerna() #Ser till att vi får en atomlista från funktionen listan_av_atomerna(), men den funktionen spottar inte ut listan så det sker inte, utan vi kan spela med listan utan att spotta ut den.
        if not self.atomlista:
            print("Atomlistan är tom. Kunde inte starta spelet.")
            return
        
        slumpens_atom = random.choice(self.atomlista)
        i = 0
        while True:
            try:    
                guessed_atomnummer = int(input(f"Gissa atomnumret för {slumpens_atom.atombeteckning}: "))
                if guessed_atomnummer == slumpens_atom.atomnummer:
                    print("Rätt gissat!")
                    break
                elif i==2:
                    print(f"Du har inga försök kvar, rätt svar var {slumpens_atom.atomnummer}")
                    break
                elif guessed_atomnummer < 1 or guessed_atomnummer > 103:
                    print("Endast tal mellan 1 och 103, pröva igen.")
                else:
                     i += 1
                print(f"Fel, du har {3-i} försök kvar.\n")
            except ValueError:
                print("Du måste skriva siffror")

    def spel_2(self):
        self.listan_av_atomerna()  # Ser till att vi får en atomlista från funktionen listan_av_atomerna(), men den funktionen spottar inte ut listan så det sker inte, utan vi kan spela med listan utan att spotta ut den.
        if not self.atomlista:
            print("Atomlistan är tom. Kunde inte starta spelet.")
            return
        
        slumpens_atombeteckning = random.choice(self.atomlista)
        i = 0
        while True:
                gissad_atombeteckning = input(f"Gissa atombeteckningen för {slumpens_atombeteckning.atomnummer}: ")
                if gissad_atombeteckning.lower() == slumpens_atombeteckning.atombeteckning.lower():
                    print("Rätt gissat!")
                    break
                elif not gissad_atombeteckning.isalpha():
                    print("Du får bara skriva bokstäver, försök igen!")
                elif i==2:
                    print(f"Du har inga försök kvar, rätt svar var {slumpens_atombeteckning.atombeteckning}")
                    break
                else:
                    i += 1
                print(f"Fel, du har {3-i} försök kvar.\n")


    def spel_3(self):
        self.listan_av_atomerna()  #Ser till att vi får en atomlista från funktionen listan_av_atomerna(), men den funktionen spottar inte ut listan så det sker inte, utan vi kan spela med listan utan att spotta ut den.
        if not self.atomlista:
            print("Atomlistan är tom. Kunde inte starta spelet.")
            return
        
        en_slumpvald_atom_A = random.choice(self.atomlista)
        self.atomlista.remove(en_slumpvald_atom_A) #Tar bort från listan så inte den inte kan komma upp 2 gånger, det är inte troligt att den ska men detta görs för säkerhetens skull
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
        
                if  vald_vikt == slumpad_atom.atomvikt:
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
        self.listan_av_atomerna() #Ser till att vi får en atomlista från funktionen listan_av_atomerna(), men den funktionen spottar inte ut listan så det sker inte, utan vi kan spela med listan utan att spotta ut den.
        if not self.atomlista:
            print("Atomlistan är tom. Kunde inte starta spelet.")
            return
        
        rader = 9
        kolonner = 18
        matris = [[f'{rad},{kol}' for kol in range(1, kolonner + 1)] for rad in range(1, rader + 1)]
        for rad in matris:
            print(rad) #Skapar matrisen med bara siffror

        while True:
            atom = random.choice(self.atomlista)
            self.atomlista.remove(atom)

            while True:
                print(f"\nVart i det periodiska systemet ligger: {atom.atombeteckning}")
                rad = input("\nVilken rad ligger atomen på? ")
                kolonn = input("Vilken kolonn? ")
                if not rad.isdigit() or not kolonn.isdigit():
                    print("Det var inget alternativ, skriv en siffra och försök igen!")
                    continue
                elif not 1 <= int(rad) <= 9 or not 1 <= int(kolonn) <= 18:
                    print("\nFelaktigt intervall, rad mellan 1-9 och kolonn mellan 1-18. Försök igen!\n")
                    continue
                elif int(rad) == atom.rad and int(kolonn) == atom.kolonn:
                    print("\nRätt!!")

                    matris[int(rad) - 1][int(kolonn) - 1] = atom.atombeteckning #Alltså ta bort den positionen nummer för rad och kolonn och byt ut den mot atombeteckningen.

                #Utskrift av hela matrisen inklusive atomens position
                    for n, rad in enumerate(matris, start=1):
                        rad_str = [f'{cell}' if cell else ' ' for cell in rad]
                        print(["',  ".join(rad_str)])
                    break
                else:
                    print("\nFel!")

atom_lista_objekt = Atomlista(atomfil='Atomer_UppgB.txt')

def huvudprogram():
    while True:
        
        print("\n\n\n-------------- MENY ---------------")
        print("1. Visa alla atomer\n2. Träna på atomnummer\n3. Träna på atombeteckningar\n4. Träna på atomvikter\n5. Träna på periodiska systemet\n6. Sluta\n-----------------------------------")
        try:
            aktivitet = int(input("Vad vill du göra?: "))
            if aktivitet == 1:
                print("Okej, här är alla atomerna:")
                print()
                atom_lista_objekt.skriv_ut_atomerna('Atomvikt.txt')
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
                print ("Välj en siffra mellan 1 till 6")

huvudprogram()