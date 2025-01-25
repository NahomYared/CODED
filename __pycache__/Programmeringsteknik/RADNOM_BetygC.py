import random

class Atom:
    def __init__(self, atombeteckning, atomvikt):
        self.atombeteckning = atombeteckning
        self.atomvikt = atomvikt
        self.atomnummer = None 

    def __str__(self):
        return f"{self.atomnummer} {self.atombeteckning} {self.atomvikt}"
        
class Atomlista:
    def __init__(self):
        self.atomlista = []

    def skriv_ut_atomerna(self, atomfil='Atomvikt.txt'):
        atomlista=[]
        with open(atomfil, 'r') as fil:
            for line in fil:
                data = line.strip().split()
                if len(data) == 2:
                    atom = Atom(data[0], float(data[1])) 
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
                elif guessed_atomnummer < 1 or guessed_atomnummer > 103:
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

atom_lista_objekt = Atomlista()

print("-------------- MENY ---------------")
print("1. Visa alla atomer\n2. Träna på atomnummer\n3. Träna på atombeteckningar\n4. Träna på atomvikter\nSluta\n-----------------------------------")

def huvudprogram():
        while True:
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
                    exit(0)
                else:
                    print("Inget möjligt val, försök igen")
            except ValueError:
                print ("Välj en siffra mellan 1 till 5")


huvudprogram()
