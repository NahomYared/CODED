import tkinter
from functools import partial
import random
from tkinter import messagebox


class SpelKort():
    """
    Representerar ett spelkort i Memory-spelet.

    Attribut:
    -----------------
    ord (str): Ordet associerat med kortet.
    position (tuple): Positionen för kortet på spelbrädet.
    memory (MemorySpel): Instansen av Memory-spelet som kortet tillhör.
    """

    def __init__(self, ord, position, memory):
        """Initialiserar ett spelkort."""

        self.ord = ord
        self.position = position
        self.memory = memory
        self.uppvänd = False 
        self.knapp = self.skapa_knapp()     
    
    def skapa_knapp(self):
        """
        Skapar en knapp-widget för spelkortet.

        Returnerar:
        -------------
        tkinter.Button: Knapp-widgeten associerad med kortet.
        """

        r, c = self.position

        ram = tkinter.Frame(master=self.memory.bräda, width=300, height=300, relief=tkinter.RAISED, borderwidth=2)
        ram.grid(row=r, column=c, pady=10, padx=10)

        klicka_memorykort = partial(self.memory.matcha_kort, r, c)
        knapp = tkinter.Button(master=ram, borderwidth=2, text= "-" * len(max(self.memory.fil, key=len)), command=klicka_memorykort)
        knapp.pack()

        return knapp
 

    def flippa_kort(self):
        """ 
        Vänder på kortet och ändrar dess framsida/baksida-ställning.
        Uppdaterar texten på den associerade knappen därefter.
        """
        self.uppvänd = not self.uppvänd
        num_bindesträck = len(max(self.memory.fil, key=len))
        bindesträck_text = "-" * num_bindesträck 
        self.knapp["text"] = f"{self.ord}" if self.uppvänd else bindesträck_text


class MemorySpel():
    """Representerar Memory-spelet.

        Attribut:
        -----------------
        ruta (tkinter.Tk): Huvudfönstret för spelet.
        huvudmeny (tkinter.Toplevel): Toppfönstret för huvudmenyn.
        """

    def __init__(self):
        """Initialiserar instansen av Memory-spelet."""

        self.ruta = tkinter.Tk()
        self.ruta.withdraw()
        self.huvudmeny = None
        self.räkna_klick, self.räkna_par, self.räkna_fel, self.räkna_spel = 0, 0, 0, 0 
        self.vald_kort = [] 


    def visa_huvudmeny(self):
        """
        Visar huvudmenyn för Memory-spelet.
        """
        self.huvudmeny = tkinter.Toplevel(self.ruta)
        self.huvudmeny.title("Memory Spel")
        self.bräda = None

        rubrik = tkinter.Label(self.huvudmeny, text="Välkommen till Memory Spelet!", font=("Times New Roman", 16))
        rubrik.pack(pady=20)

        instruktion = tkinter.Label(self.huvudmeny, text="Välj storlek på spelplanen:")
        instruktion.pack()

        storlekar = [2, 4, 6, 8, 10]

        for storlek in storlekar:
            knapp_text = f"{storlek}x{storlek}"
            klicka_nytt_spel = partial(self.skapa_nytt_spel, storlek)
            knapp = tkinter.Button(self.huvudmeny, text=knapp_text, command=klicka_nytt_spel)
            knapp.pack(pady=10)

        self.huvudmeny.protocol("WM_DELETE_WINDOW", self.dölj_fönster)   
        self.huvudmeny.mainloop()


    def skapa_nytt_spel(self, format):
        """
        Skapar ett nytt Memory-spel med den angivna brädstorleken.

        Parametrar:
        -------------
        format (int): Storleken på spelbrädet (format x format).
        """
        
        self.huvudmeny.withdraw()
        self.ruta.deiconify()
        self.bräda = tkinter.Frame(master=self.ruta, relief=tkinter.RAISED, borderwidth=1)
        self.bräda.grid()

        slumpa_ord = hantera_ordlista("students.txt", format)
        slumpa_ord *= 2
        random.shuffle(slumpa_ord)

        self.fil = slumpa_ord
        self.format = format

        self.korten = []
        self.program_läge = False

        self.grafisk_spel()


    def grafisk_spel(self):
        """
        Sätter upp det grafiska gränssnittet för Memory-spelet.
        Skapar spelkort och initierar spelbrädet.
        """

        self.visa_försök_grafisk = tkinter.Frame(master=self.ruta, relief=tkinter.RAISED, borderwidth=2)
        self.visa_försök = tkinter.Label(master=self.visa_försök_grafisk, text=f"Du har försökt 0 gånger.")
        self.visa_försök.grid()
        self.visa_försök_grafisk.grid(pady=5, padx=5)

        for r in range(self.format):
            for c in range(self.format):
                index = self.format * r + c
                ord = self.fil[index]
                position = [r, c]
                kort = SpelKort(ord, position, self)
                self.korten.append(kort)


    def matcha_kort(self, r, c):
        """
        Hanterar logiken när ett kort klickas på.
        Kontrollerar matchande par, uppdaterar spelstatistik och utlöser spelets slut.
        """
        index_kort = self.format * r + c

        if self.program_läge or self.korten[index_kort].uppvänd or self.räkna_par >= 2:
            return

        self.korten[index_kort].flippa_kort()
        self.vald_kort.append(index_kort)
        self.räkna_par += 1

        if self.räkna_par == 2:
            if self.fil[self.vald_kort[0]] == self.fil[self.vald_kort[1]]:
                self.räkna_par = 0
                self.vald_kort = []
                self.räkna_klick += 1
                self.visa_försök["text"] = f"Du har försökt {self.räkna_klick} gånger."
                self.räkna_spel += 1

                if self.räkna_spel == int((self.format ** 2) / 2):
                    self.memory_avslutad()
                return True

            else:
                self.ruta.after(1000, self.flippa_tillbaka_kort, self.vald_kort.copy()) 
                self.räkna_klick += 1
                self.visa_försök["text"] = f"Du har försökt {self.räkna_klick} gånger."

        return False
    

    def flippa_tillbaka_kort(self, vald_kort):
        """Vänder tillbaka de valda korten efter en kort fördröjning."""
        for a in vald_kort:
            self.korten[a].flippa_kort()

        self.vald_kort = []
        self.räkna_par = 0
        self.räkna_fel += 1


    def memory_avslutad(self):
        """Visar avslutningsfönstret och låter användaren ange sitt namn till en rekordlista."""

        self.dölj_fönster()
        self.ruta_2 = tkinter.Toplevel(self.ruta)
        tkinter.Label(self.ruta_2, text=f"Bra jobbat, det tog dig {self.räkna_klick} försök att klara Memory spelet. \nNedan kan du skriva in dig på highscore listan\n").pack()

        skriv_namn = tkinter.Entry(self.ruta_2)
        skriv_namn.pack()
        klar_knappen = partial(self.uppdatera_poäng, skriv_namn)
        tkinter.Button(self.ruta_2, borderwidth=2, text="KLAR", command=klar_knappen).pack()

        self.ruta_2.grid()
    

    def uppdatera_poäng(self, användare):
        """
        Uppdaterar rekordlistan med spelarens poäng och namn.

        Parametrar:
        ---------------
        användare (tkinter.Entry): Entry-widgeten som innehåller spelarens namn.
        """

        användare = användare.get().strip()
        if not användare:
            tkinter.messagebox.showinfo("Fel", "Ange ditt namn innan du klickar KLAR.")
            return
    
        resultat = [str(self.räkna_klick), användare + "\n"]

        poäng_lista = []
        with open("highscore.txt", "r") as fil:
            for rad in fil:
                poäng_lista.append(rad.split(","))

        if not poäng_lista or int(poäng_lista[-1][0]) < self.räkna_klick:
            poäng_lista.append(resultat)
        else:
            for rad in range(len(poäng_lista)):
                tidigare_poäng = int(poäng_lista[rad][0])
                if tidigare_poäng > self.räkna_klick:
                    poäng_lista.insert(rad, resultat)
                    break

        with open("highscore.txt", "w") as fil:
            fil_poäng_lista = [",".join(rad) for rad in poäng_lista]
            fil.writelines(fil_poäng_lista)

        self.grafisk_rekordlista(poäng_lista)


    def dölj_fönster(self):
        """Döljer det aktuella fönstret"""
        if self.huvudmeny:
            self.huvudmeny.destroy() 

        self.ruta.withdraw()
        self.ruta.quit()

        
    def grafisk_rekordlista(self, poäng_lista):
        """
        Visar rekordlistan i ett separat fönster.

        Parametrar:
        ---------------
        poäng_lista (list): Lista med highscores som [namn, poäng]-par.
        """

        for bricka in self.ruta_2.winfo_children():
            bricka.destroy()

        self.rekord_2 = open("highscore.txt", "r")
        self.rekord_2.close() 
        sortera_nummer = "\n".join([resultat[0] for resultat in poäng_lista])
        sortera_namn = "".join([resultat[1] for resultat in poäng_lista])
        sortera_namn = sortera_namn[:-1]

        rekord_rubrik = tkinter.Label(self.ruta_2, text = "Highscore Listan", fg = "deeppink2")
        rekord_rubrik.grid(row = 0, column = 0)
        visa_nummer = tkinter.Label(self.ruta_2, text = sortera_nummer, fg = "deeppink2")
        visa_nummer.grid(row = 1, column = 1)
        visa_namn = tkinter.Label(self.ruta_2, text = sortera_namn, fg = "deeppink2")              
        visa_namn.grid(row = 1, column = 0)

        knapp_avsluta = tkinter.Button(self.ruta_2, text="Avsluta", command=self.ruta.quit)
        knapp_avsluta.grid(row=2, column=1, pady=10, padx=10)

        knapp_huvudmeny = tkinter.Button(self.ruta_2, text="Huvudmeny", command=lambda: [self.ruta_2.destroy(), huvudprogram()])
        knapp_huvudmeny.grid(row=2, column=0, pady=10, padx=10)



def hantera_ordlista(filnamn, format):
    """
    Läser in och bearbetar filen med ordlistan, returnerar en lista med slumpmässigt valda ord.

    Parametrar:
    --------------
    filnamn (str): Filnamnet för ordlistan.
    format (int): Storleken på spelbrädet (format x format).

    Returnerar:
    --------------
    list: En lista med slumpmässigt valda ord från ordlistan.
    """

    try:
        with open(filnamn, "r", encoding="utf-8") as fil:
            ordlista = [rad.strip() for rad in fil]
    except FileNotFoundError:
        messagebox.showerror("Fel", "Filen kunde inte hittas. Se till att ha rätt fil för att starta Memory-spelet.")
        quit()

    slumpa_ord = random.sample(ordlista, int((format**2)/2))
    return slumpa_ord 


def huvudprogram():
    """
    Huvudfunktionen för att köra Memory-spelet.
    Skapar en instans av MemorySpel och visar huvudmenyn.
    """
     
    memory_spel = MemorySpel()
    memory_spel.visa_huvudmeny()
    memory_spel.ruta.mainloop()

if __name__ == "__main__":
    huvudprogram()