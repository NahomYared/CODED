import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class AtomGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Atom Inlärningsspel")
        self.geometry("800x600")

        self.menu_label = tk.Label(self, text="Välj en aktivitet:", font=('Times New Roman', 16))
        self.menu_label.pack(pady=20)

        self.skapa_knappar("Visa alla atomer", self.visa_alla_atomerna)
        self.skapa_knappar("Träna atomnummer", self.träna_atomnummer)
        self.skapa_knappar("Träna atombeteckningar", self.träna_atombeteckningar)
        self.skapa_knappar("Träna atomvikter", self.träna_atomvikter)
        self.skapa_knappar("Träna periodiska systemet", self.träna_periodiska_systemet)

        # Lägg till en Listbox för att visa atomerna
        self.atom_listbox = tk.Listbox(self, font=('Times New Roman', 12), selectmode=tk.SINGLE)
        self.atom_listbox.pack(pady=10, padx=20, fill='both', expand=True)

        # Lägg till en Scrollbar
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.atom_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.atom_listbox.yview)

    def skapa_knappar(self, text, command):
        knappar = tk.Button(self, text=text, font=('Times New Roman', 14), command=command)
        knappar.pack(pady=10, padx=20, fill='x')

    def visa_alla_atomerna(self):
        atom_lista_objekt.listan_av_atomerna()
        self.atom_listbox.delete(0, tk.END)
        for atom in atom_lista_objekt.atomlista:
            self.atom_listbox.insert(tk.END, str(atom))

    def träna_atomnummer(self):
        self.visa_meddelande("Träna Atomnummer", "Låt oss träna på att gissa atomnummer.")
        atom_lista_objekt.spel_1(self)

    def träna_atombeteckningar(self):
        self.visa_meddelande("Träna Atombeteckningar", "Låt oss träna på att gissa atombeteckningar.")
        atom_lista_objekt.spel_2(self)

    def träna_atomvikter(self):
        self.visa_meddelande("Träna Atomvikter", "Låt oss träna på att gissa atomvikter.")
        atom_lista_objekt.spel_3(self)

    def träna_periodiska_systemet(self):
        self.visa_meddelande("Träna Periodiska Systemet", "Låt oss träna på att placera atomer i det periodiska systemet.")
        self.bygg_periodiskt_system(self)

    def visa_meddelande(self, title, message):
        messagebox.showinfo(title, message)

    def bygg_periodiskt_system(self, atomlista):
        self.atom_listbox.delete(0, tk.END)  # Rensa Listbox
        atomlista = Atom.skapa_atomlista()
        random.shuffle(atomlista)  # Blanda atomerna för att placera dem slumpmässigt i det periodiska systemet

        periodiskt_system_fönster = tk.Toplevel()
        periodiskt_system_fönster.title("Periodiskt System")
        periodiskt_system_fönster.geometry("800x600")

        # Skapa en 9x18 grid av Labels som representerar cellerna i det periodiska systemet
        for row in range(1, 10):
            for col in range(1, 19):
                cell_label = tk.Label(periodiskt_system_fönster, text="", width=5, height=2, borderwidth=1, relief="solid")
                cell_label.grid(row=row, column=col)
                cell_label.bind("<Button-1>", lambda event, r=row, c=col: self.klickad_cell(event, r, c, atomlista))

        self.random_atom = atomlista.pop()
        self.visa_meddelande(f"Placera in {self.random_atom.atombeteckning}", "Klicka på rätt plats i det periodiska systemet.")

    def klickad_cell(self, event, row, col, atomlista):
        cell_label = event.widget

        if self.random_atom.rad == row and self.random_atom.kolonn == col:
            cell_label.config(text=self.random_atom.atombeteckning, bg="light blue", fg="black")
            if atomlista:
                self.random_atom = atomlista.pop()
                self.visa_meddelande(f"Placera in {self.random_atom.atombeteckning}", "Klicka på rätt plats i det periodiska systemet.")
            else:
                self.visa_meddelande("Grattis! Du har placerat alla atomer.", "Spelet är klart!")    
                self.atom_listbox.delete(0, tk.END)  # Rensa Listbox
        else:
            self.visa_meddelande("Fel Placering", "Försök igen! Placera atomen på rätt plats i det periodiska systemet.")

class Atom:
    def __init__(self, atombeteckning, atomvikt, rad, kolonn):
        self.atombeteckning = atombeteckning
        self.atomvikt = atomvikt
        self.atomnummer = None
        self.rad = rad
        self.kolonn = kolonn

    def __str__(self):
        return f"{self.atomnummer}  {self.atombeteckning}  {self.atomvikt} || Kolonn: {self.kolonn} Rad: {self.rad}"

class Atomlista:
    def __init__(self, atomfil='Atomer_UppgB.txt'):
        self.atomlista = []
        self.atomfil = atomfil

    def listan_av_atomerna(self, atomfil='Atomer_UppgB.txt'):
        self.atomlista = []
        with open(atomfil, 'r') as fil:
            for line in fil:
                data = line.strip().split()
                if len(data) == 4:
                    atom = Atom(data[0], float(data[1]), int(data[2]), int(data[3]))
                    self.atomlista.append(atom)

        self.atomlista = sorted(self.atomlista, key=lambda x: x.atomvikt)
        for i, atom in enumerate(self.atomlista, start=1):
            atom.atomnummer = i

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

    def skriv_ut_atomerna(self, atomfil='atomvikt.txt'):
        self.listan_av_atomerna()
        for atom in self.atomlista:
            print(f"{atom}")

    def spel_1(self, gui):
        self.listan_av_atomerna()
        if not self.atomlista:
            gui.visa_meddelande("Spelfel", "Atomlistan är tom. Kunde inte starta spelet.")
            return

        slumpens_atom = random.choice(self.atomlista)
        i = 0
        while True:
            try:
                guessed_atomnummer = int(simpledialog.askinteger("Gissa Atomnummer", f"Gissa atomnumret för {slumpens_atom.atombeteckning}: "))
                if guessed_atomnummer == slumpens_atom.atomnummer:
                    gui.visa_meddelande("Rätt Gissat", "Rätt gissat!")
                    break
                elif i == 2:
                    gui.visa_meddelande("Inga Försök Kvar", f"Du har inga försök kvar, rätt svar var {slumpens_atom.atomnummer}")
                    break
                elif guessed_atomnummer < 1 or guessed_atomnummer > 103:
                    gui.visa_meddelande("Ogiltig Gissning", "Endast tal mellan 1 och 103, pröva igen.")
                else:
                    i += 1
                gui.visa_meddelande("Felaktig Gissning", f"Fel, du har {3 - i} försök kvar.")
            except ValueError:
                gui.visa_meddelande("Ogiltig Inmatning", "Du måste skriva siffror")


    def spel_2(self, gui):
        self.listan_av_atomerna()
        if not self.atomlista:
            gui.visa_meddelande("Spelfel", "Atomlistan är tom. Kunde inte starta spelet.")
            return

        slumpens_atombeteckning = random.choice(self.atomlista)
        i = 0
        while True:
            gissad_atombeteckning = simpledialog.askstring("Gissa Atombeteckning",
                                                            f"Gissa atombeteckningen för {slumpens_atombeteckning.atomnummer}: ")
            if gissad_atombeteckning.lower() == slumpens_atombeteckning.atombeteckning.lower():
                gui.visa_meddelande("Rätt Gissat", "Rätt gissat!")
                break
            elif not gissad_atombeteckning.isalpha():
                gui.visa_meddelande("Ogiltig Inmatning", "Du får bara skriva bokstäver, försök igen!")
            elif i == 2:
                gui.visa_meddelande("Inga Försök Kvar",
                                 f"Du har inga försök kvar, rätt svar var {slumpens_atombeteckning.atombeteckning}")
                break
            else:
                i += 1
                gui.visa_meddelande("Felaktig Gissning", f"Fel, du har {3 - i} försök kvar.\n")

    def spel_3(self, gui):
        self.listan_av_atomerna()
        if not self.atomlista:
            gui.visa_meddelande("Spelfel", "Atomlistan är tom. Kunde inte starta spelet.")
            return

        en_slumpvald_atom_A = random.choice(self.atomlista)
        self.atomlista.remove(en_slumpvald_atom_A)
        en_slumpvald_atom_B = random.choice(self.atomlista)
        self.atomlista.remove(en_slumpvald_atom_B)
        en_slumpvald_atom_C = random.choice(self.atomlista)

        slumpmässiga_atomer = [en_slumpvald_atom_A, en_slumpvald_atom_B, en_slumpvald_atom_C]
        slumpad_atom = random.choice(slumpmässiga_atomer)

        while True:
            try:
                gui.visa_meddelande("Spela!", f"Vad har atomen {slumpad_atom.atombeteckning} för atomvikt?")
                svar = str(simpledialog.askstring(f"{slumpad_atom.atombeteckning}", f"A. {en_slumpvald_atom_A.atomvikt}   B. {en_slumpvald_atom_B.atomvikt}   C. {en_slumpvald_atom_C.atomvikt}\nSvar: "))
                if svar.upper() == 'A':
                    vald_vikt = en_slumpvald_atom_A.atomvikt
                elif svar.upper() == 'B':
                    vald_vikt = en_slumpvald_atom_B.atomvikt
                elif svar.upper() == 'C':
                    vald_vikt = en_slumpvald_atom_C.atomvikt

                
                if vald_vikt == slumpad_atom.atomvikt:
                    gui.visa_meddelande("Rätt Gissat", "Rätt gissat!")
                    break
                else:
                    gui.visa_meddelande("Felaktig Gissning", f"Fel, rätt svar var {slumpad_atom.atomvikt}")
                    break
            except UnboundLocalError:
                gui.visa_meddelande("Ogiltig Inmatning", "Ogiltigt val. Du måste välja A, B eller C.")

    def spel_4(self, gui):
        self.listan_av_atomerna()
        if not self.atomlista:
            gui.visa_meddelande("Spelfel", "Atomlistan är tom. Kunde inte starta spelet.")
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
                gui.visa_meddelande("Spela!", f"\nVart i det periodiska systemet ligger: {atom.atombeteckning}")
                rad = simpledialog.askstring("Placera Atom i Periodiska Systemet", f"\nVilken rad ligger atomen {atom.atombeteckning} på? ")
                kolonn = simpledialog.askstring("Placera Atom i Periodiska Systemet", f"Vilken kolonn ligger {atom.atombeteckning} på? ")
                if not rad.isdigit() or not kolonn.isdigit():
                    gui.visa_meddelande("Ogiltig Inmatning", "Det var inget alternativ, skriv en siffra och försök igen!")
                    continue
                elif not 1 <= int(rad) <= 9 or not 1 <= int(kolonn) <= 18:
                    gui.visa_meddelande("Ogiltig Inmatning",
                                     "\nFelaktigt intervall, rad mellan 1-9 och kolonn mellan 1-18. Försök igen!\n")
                    continue
                elif int(rad) == atom.rad and int(kolonn) == atom.kolonn:
                    gui.visa_meddelande("Rätt Placering", "\nRätt!!")

                    matris[int(rad) - 1][int(kolonn) - 1] = atom.atombeteckning

                    for n, rad in enumerate(matris, start=1):
                        rad_str = [f'{cell}' if cell else ' ' for cell in rad]
                        print(["',  ".join(rad_str)])
                    break
                else:
                    gui.visa_meddelande("Felaktig Placering", "\nFel!")

atom_lista_objekt = Atomlista(atomfil='Atomer_UppgB.txt')

def huvudprogram():
    app = AtomGUI()
    app.mainloop()

if __name__ == "__main__":
    huvudprogram()

