import tkinter as tk
from tkinter import messagebox, simpledialog #moduler för tkinter
import random

class Atom_GUI(tk.Tk):
    """
    En GUI-applikation för att lära sig om atomer genom olika aktiviteter och spel.

    Attribut:
        använda_atomer: håller reda på använda atomer.
    """
    def __init__(self, atom_lista_objekt):
        """
        Skapar en ny instans av Atom_GUI.

        Initerar fönstret och lägger till olika komponenter som knappar, listbox och scrollbar.
        """
        self.använda_atomer = []
        super().__init__()
        """
        Skapar en instans av Atom GUI-applikationen.

        Argument:
            atom_lista_objekt: En instans av Atomlista som innehåller information om atomer.

        Return:
            None
        """
        self.atom_lista_objekt=atom_lista_objekt

        self.title("Atom Inlärningsspel")
        self.geometry("800x600")

        self.menu_label = tk.Label(self, text="Välj en aktivitet:", font=('Times New Roman', 20))
        self.menu_label.pack(pady=20)

        #Alla knapparna som ska synas
        self.skapa_knappar("Visa alla atomer", self.visa_alla_atomerna)
        self.skapa_knappar("Träna atomnummer", self.träna_atomnummer)
        self.skapa_knappar("Träna atombeteckningar", self.träna_atombeteckningar)
        self.skapa_knappar("Träna atomvikter", self.träna_atomvikter)
        self.skapa_knappar("Träna periodiska systemet", self.träna_periodiska_systemet)

        # Lägg till en Listbox för att visa atomerna
        self.atom_listbox = tk.Listbox(self, font=('Times New Roman', 12), selectmode=tk.SINGLE)
        self.atom_listbox.pack(pady=20, padx=10, fill='both', expand=True) #Kontrollerar avståndet från sidorna till listboxen

        # Lägg till en Scrollbar, vertikal och y osv ser till att den kan blir vertikalt rullande och man skrollar upp och ner, inte åt sidan
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL) 
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y) #RIGHT gör så den är höger om listboxen 
        self.atom_listbox.config(yscrollcommand=self.scrollbar.set) #Scrollas vertikalt
        self.scrollbar.config(command=self.atom_listbox.yview) #Scrollbar kommer att kontrollera vypositionen på Listbox i vertikal riktning.

    def skapa_knappar(self, text, command):
        """
        Skapar och lägger till en knapp på GUI.

        Argument:
            text: Texten som ska visas på knappen.
            command: det som ska ske när man trycker på knappen, funktionen.
        Return:
            None
        """
        knappar = tk.Button(self, text=text, font=('Times New Roman', 14), command=command)
        knappar.pack(pady=10, padx=50, fill='x') #Lägger till knappar, storleken, skrivstilen, des avstånd i pixlar till varandra och kanterna

    def visa_alla_atomerna(self):
        """
        Visar alla atomer i Atomlistan i användargränssnittet.

        Argument:
            self: Instansen av klassen.

        Returnerar:
            None
        """
        self.atom_lista_objekt.listan_av_atomerna()
        self.atom_listbox.delete(0, tk.END) #Detta gör så när jag trycker på att visa atomerna-knappen flera gånger, så kommer inte flera av samma listor upp, utan den lsitan som va där innan raderas och en ny lista med samma innehåll kommer fram.
        for atom in self.atom_lista_objekt.atomlista: #För varje atom i listan
            self.atom_listbox.insert(tk.END, str(atom)) #Den blir tillagd, insertad, i listboxen och i sträng form och tk.END menar till slutet

    def träna_atomnummer(self):
        """
        Tränar gissning av atomnummer.
        Argument:
            self, instans av klassen.

        Return:
            None
        """
        self.visa_meddelande("Träna Atomnummer", "Låt oss träna på att gissa atomnummer.")
        self.atom_lista_objekt.spel_1(self) #Gissa atomnummerspelet anropas

    def träna_atombeteckningar(self):
        """
            Tränar gissning av atombeteckning.
        Argument:
            self: Instansen av klassen.

        Return:
            None
        """
        self.visa_meddelande("Träna Atombeteckningar", "Låt oss träna på att gissa atombeteckningar.")
        self.atom_lista_objekt.spel_2(self) #Gissa atombeteckningspelet anropas

    def träna_atomvikter(self):
        """
            Tränar gissning av atomvikt
        Argument:
            self: Instansen av klassen.

        Return:
            non
        """
        self.visa_meddelande("Träna Atomvikter", "Låt oss träna på att gissa atomvikter.")
        self.atom_lista_objekt.spel_3(self) #Gissa atomviktspelet anropas

    def träna_periodiska_systemet(self):
        """
            Tränar periodiska systemet
        Argument:
            self: Instansen
            
        return:
            none
        """
        self.visa_meddelande("Träna Periodiska Systemet", "Låt oss träna på att placera atomer i det periodiska systemet.")
        self.bygg_periodiskt_system(self.atom_lista_objekt) #Placera i periodiska systemet-spelet anropas

    """Använder modulen i tkinter där rutor poppas upp av meddelanden"""
    def visa_meddelande(self, title, message):
        """
        Visar ett meddelande i en liten ruta

        Metoden använder modulen i tkinter för att visa ett meddelande i en popup-ruta.

        Argumentwn:
          self: Instansen av klassen.
          title: Rubrik för meddelanderutan.
          message: poppande ruta.

        Return:
        None
        """
        messagebox.showinfo(title, message) #messagebox är en modul i tkinter som tillåter rutor av meddelanden att poppa upp, mer eller mindre print().



    def bygg_periodiskt_system(self, atomlista):
        """
        Skapar och visar ett interaktivt periodiskt system i ett nytt tkinter-fönster.

        Argument:
         atomlista: En lista av Atom-objekt som ska användas för att fylla det periodiska systemet.
            self.bygg_periodiskt_system()
        Return:
        none
        """
        self.atom_lista_objekt.listan_av_atomerna() #När funktionen listan_av_atomerna anropas så fylls atomlista med atomer, 
        random.shuffle(atomlista.atomlista) #Blanda atomerna i en random ordning

        periodiskt_system_fönster = tk.Toplevel() #Skapa ett fönster av periodiska systemet
        periodiskt_system_fönster.title("Periodiskt System")
        periodiskt_system_fönster.geometry("1000x500") 

        for row in range(1, 10):
            for col in range(1, 19): #9x18 fönster av rutor, från 19 st siffror från 1
                specifik_cell = tk.Label(periodiskt_system_fönster, text="", width=7, height=3, borderwidth=2, relief="solid") #Rutornas utseende i periodiska systemet
                specifik_cell.grid(row=row, column=col) #De består av rad och kolonn
                specifik_cell.bind("<Button-1>", lambda event, r=row, c=col: self.klickad_cell(event, r, c, atomlista)) #Button-1 gör så det är vänsterknappmusklick som gör så man placerar atomen på en viss ruta.

    
        atom_utropp = iter(atomlista.atomlista) #Man använder inbyggd funktion iteration för att se till att atom_utropp får en atom från atomlista och sedan gör atom_på_måfå att man får nästa.
        self.atom_på_måfå = next(atom_utropp, None)

        if self.atom_på_måfå:
            self.visa_meddelande(f"Placera in {self.atom_på_måfå.atombeteckning}",
                             f"Klicka in {self.atom_på_måfå.atombeteckning} i det periodiska systemet.")

        periodiskt_system_fönster.lift()

    
    
    def klickad_cell(self, event, row, col, atomlista):
            """
    Hanterar händelsen när en cell i det periodiska systemet klickas på.

    Argument:
        event: En händelse som genererades vid klickning på cellen.
        row : Radnumret för den klickade cellen.
        col: Kolumnnumret för den klickade cellen.
        atomlista: En lista av Atomobjekt som representerar de tillgängliga atomerna.

    Return:
        none
    """
            specifik_cell = event.widget #event.widget ger referensen till det specifika widgetet som användaren har utfört klicken på, alltså den specifika cellen som blivit klickad på.

            if self.atom_på_måfå.rad == row and self.atom_på_måfå.kolonn == col: #Om den frågade atomens rad och kolonn är samma som den rad och kolonn du tryckte på...
                specifik_cell.config(text=self.atom_på_måfå.atombeteckning, bg="Navy blue", fg="white")#...Blir den platsen istället marinblå med vit text
                self.använda_atomer.append(self.atom_på_måfå)  #Lägg till den redan nämnda atomen i en lista som heter använda_atomer
                self.atom_på_måfå = self.få_oanvända_atomer(atomlista)  #Den nya atom_på_måfå, alltså den nya atomen som ska tillfråga, tas från en lista atomlista från funktionen få_oanvända_atomer

                if self.atom_på_måfå:
                    self.visa_meddelande(f"Bravo!! Placera in {self.atom_på_måfå.atombeteckning}", #Den nya atomen från atom_på_måfå tillfrågas
                                 f"Bra jobbat!! Klicka in {self.atom_på_måfå.atombeteckning} i det periodiska systemet.") #Du får också positiv feedback om du gör rätt
                else:
                    self.visa_meddelande("Grattis! Du har placerat alla atomer.", "Spelet är klart!") #Om vi kommer till punkten att inga fler atomer kan tillfrågas så poppas detta upp och...
                    self.atom_listbox.delete(0, tk.END)  #...listan raderas
            else:
                self.visa_meddelande(f"Fel Placering, du ska placera {self.atom_på_måfå.atombeteckning}", #Om det läggs in fel atom, alltså om rad och kolonn av den atomen inte passar platsen du tryckte på så kommer detta meddelande fram
                             f"Försök igen! Placera {self.atom_på_måfå.atombeteckning} på rätt plats i det periodiska systemet.")

    def få_oanvända_atomer(self, atomlista):
        """
        Väljer och returnerar en slumpmässig atom från atomlistan som ännu inte har använts.

        Aegument: 
            Atomlista: En Atomlista-objekt som innehåller en lista av atomer.
        return: 
            En slumpmässig atom som inte har använts ännu, eller None om alla atomer har använts.
        """
        oanvända_atomer = [atom for atom in atomlista.atomlista if atom not in self.använda_atomer] #Listan oanvända_atomer är alltså atomer i atomlistan om de samtidigt inte är med i listan använda_atomer, alltså är listan de atomerna som inte har använts ännu.
        return random.choice(oanvända_atomer) if oanvända_atomer else None #Det är detta som används för den övre koden om att få en ny atom, denna kod ser till att vi får en ny atom.

class Atom: 
    """
        Skapar en ny instans av Atom.

        Argument:
            atombeteckning: Atombeteckningen för atomen.
            atomvikt: Atomvikten för atomen.
            rad: Raden där atomen placeras i det periodiska systemet.
            kolonn: Kolonnen där atomen placeras i det periodiska systemet.

        Attributes:
            atombeteckning: Atombeteckningen för atomen.
            atomvikt: Atomvikten för atomen.
            atomnummer: Atomnumret för atomen (initialt None).
            rad: Raden där atomen placeras i det periodiska systemet.
            kolonn: Kolonnen där atomen placeras i det periodiska systemet.
        """
    
    def __init__(self, atombeteckning, atomvikt, rad, kolonn):
        """
        Skapar en ny instans av Atom.

        Argument:
            atombeteckning: Atombeteckningen för atomen.
            atomvikt: Atomvikten för atomen.
            rad: Raden där atomen placeras i det periodiska systemet.
            kolonn: Kolonnen där atomen placeras i det periodiska systemet.

        Attributes:
            atombeteckning: Atombeteckningen för atomen.
            atomvikt: Atomvikten för atomen.
            atomnummer: Atomnumret för atomen (initialt None).
            rad: Raden där atomen placeras i det periodiska systemet.
            kolonn: Kolonnen där atomen placeras i det periodiska systemet.
        """
        self.atombeteckning = atombeteckning
        self.atomvikt = atomvikt
        self.atomnummer = None
        self.rad = rad
        self.kolonn = kolonn
        
        
    def __str__(self):
        """
        Returnerar en strängsrepresentation av atomen.

        Return:
            str: Sträng som representerar atomen med atomnummer, atombeteckning, atomvikt, rad och kolonn.
        """
        return f"{self.atomnummer}  {self.atombeteckning}  {self.atomvikt} || Kolonn: {self.kolonn} Rad: {self.rad}"

class Atomlista:
    """
        Skapar en Atomlista och initialiserar dess attribut.

        Argument:
            atomfil: Filnamnet för filen som innehåller atomdata.
        """
    def __init__(self, atomfil='Atomer_UppgB.txt'):
        """
        Skapar en instans av Atomlista.

        Argument:
            atomfil: Fil som innehåller information om atomer.

        Return
            None
        """
        self.atomlista = []
        self.atomfil = atomfil

    
    def listan_av_atomerna(self, atomfil='Atomer_UppgB.txt'):
        """
        Fyller atomlista från en given fil och sorterar atomerna.

        Argument:
            atomfil: Filnamnet för filen som innehåller atomdata.
        """
        self.atomlista = []
        with open(atomfil, 'r') as fil:
            for line in fil:
                data = line.strip().split() #strip tar bort onödiga whitespaces medan split delar upp raderna i lsitan baserat på whitespace
                if len(data) == 4: #4 st olika innehål
                    atom = Atom(data[0], float(data[1]), int(data[2]), int(data[3]))
                    self.atomlista.append(atom)

        self.atomlista = sorted(self.atomlista, key=lambda x: x.atomvikt) #Sorterar så atomerna är i ordning
        for i, atom in enumerate(self.atomlista, start=1): #Så atomerna får siffror baserat på ordning
            atom.atomnummer = i

        #Dessa atomer ska byta plats
        self.ändra_position('Th', 'Pa')
        self.ändra_position('Co', 'Ni')
        self.ändra_position('Ar', 'K')
        self.ändra_position('Te', 'I')
        self.ändra_position('U', 'Np')

    
    def ändra_position(self, första_beteckning, andra_beteckning):
        """
        Denna ska se till att vi byter plats på atomerna, förklaringen ges i de gröna kommentarerna
    
        Argument:
            första_beteckning: Atombeteckningen för den första atomen.
            andra_beteckning: Atombeteckningen för den andra atomen.

        return:
            none
    
        """
        första_atomen = next(atom for atom in self.atomlista if atom.atombeteckning == första_beteckning) #Namnge atombeteckningen till atomen i atomlistan till första_beteckning
        andra_atomen = next(atom for atom in self.atomlista if atom.atombeteckning == andra_beteckning) #Gör detsamma för andra

        position1, position2 = self.atomlista.index(första_atomen), self.atomlista.index(andra_atomen) #Ange positionerna för de 2 atomerna som namnges
        self.atomlista[position1], self.atomlista[position2] = self.atomlista[position2], self.atomlista[position1] #Byt ut deras positioner

        första_atomen.atomnummer, andra_atomen.atomnummer = andra_atomen.atomnummer, första_atomen.atomnummer #Byt också deras nummer

    def skriv_ut_atomerna(self): #Denna funktion skriver ut atomerna
        """
            Skriver ut atomerna i Atomlistan.

        Argument:
            self: Instansen av klassen.

        Return:
            None
        """
        self.listan_av_atomerna()
        for atom in self.atomlista:
            print(f"{atom}")

    
    def spel_1(self, gui):
        """
    Startar ett spel där användaren ska gissa atomnummer för en slumpmässigt vald atom.

    Argument:
        gui: En instans av GUI-objektet för att visa meddelanden och låta användaren svara.

    Return:
        none
        """ 
        self.listan_av_atomerna() #Ser till att vi får en atomlista från funktionen listan_av_atomerna(), men den funktionen spottar inte ut listan så det sker inte, utan vi kan spela med listan utan att spotta ut den.
        if not self.atomlista:
            gui.visa_meddelande("Spelfel", "Atomlistan är tom. Kunde inte starta spelet.")
            return

        slumpens_atom = random.choice(self.atomlista)
        i = 0
        while True:
                gissad_atomnummer = simpledialog.askinteger("Gissa Atomnummer", f"Gissa atomnumret för {slumpens_atom.atombeteckning}: ") #simpledialog ser till att användaren får svara, det är som input
                if gissad_atomnummer == slumpens_atom.atomnummer: #Om inputen passar svaret
                    gui.visa_meddelande("Rätt Gissat", "Rätt gissat!") 
                    break
                elif i == 2:
                    gui.visa_meddelande("Inga Försök Kvar", f"Du har inga försök kvar, rätt svar var {slumpens_atom.atomnummer}") #Om i=2 betyder det att alla 3 försöken gjorts och spelet avslöjar svaret.
                    break
                elif not str(gissad_atomnummer).isdigit():
                    gui.visa_meddelande("Ogiltig Inmatning", "Du måste skriva siffror")
                elif gissad_atomnummer < 1 or gissad_atomnummer > 103:
                    gui.visa_meddelande("Ogiltig Gissning", "Endast tal mellan 1 och 103, pröva igen.")
                else:
                    i += 1
                gui.visa_meddelande("Felaktig Gissning", f"Fel, du har {3 - i} försök kvar.") #Ju fler fel gissningar, desto större värde får i, och därmed ges annorlunda antal försök kvar.

    
    def spel_2(self, gui):
        """Startar ett spel där man ka gissa atombeteckningen på en atom baserat på atomnummer
            
            Argument:
            gui: En instans av GUI-objektet för att visa meddelanden och låta användaren svara.

            Return:
                non  
        """
        self.listan_av_atomerna() #Ser till att vi får en atomlista från funktionen listan_av_atomerna(), men den funktionen spottar inte ut listan så det sker inte, utan vi kan spela med listan utan att spotta ut den.
        if not self.atomlista:
            gui.visa_meddelande("Spelfel", "Atomlistan är tom. Kunde inte starta spelet.")
            return

        slumpens_atombeteckning = random.choice(self.atomlista)
        i = 0
        while True:
            gissad_atombeteckning = simpledialog.askstring("Gissa Atombeteckning", f"Gissa atombeteckningen för {slumpens_atombeteckning.atomnummer}: ")  #simpledialog ser till att användaren får svara, det är som input
            if gissad_atombeteckning.lower() == slumpens_atombeteckning.atombeteckning.lower():
                gui.visa_meddelande("Rätt Gissat", "Rätt gissat!") #Pga så mycket strängar så är det ganska självförklarande vad som görs
                break
            elif not gissad_atombeteckning.isalpha(): #Om ej bokstäver
                gui.visa_meddelande("Ogiltig Inmatning", "Du får bara skriva bokstäver, försök igen!")
            elif i == 2:
                gui.visa_meddelande("Inga Försök Kvar", f"Du har inga försök kvar, rätt svar var {slumpens_atombeteckning.atombeteckning}")
                break
            else:
                i += 1
                gui.visa_meddelande("Felaktig Gissning", f"Fel, du har {3 - i} försök kvar.\n")


    def spel_3(self, gui):
        """
    Startar ett spel där användaren ska gissa atomvikten för en slumpmässigt vald atom mha olika svarsalternativ.

    Argument:
        gui: En instans av GUI-objektet för att visa meddelanden och låta användaren svara.

    Return:
        none
        """
        self.listan_av_atomerna() #Ser till att vi får en atomlista från funktionen listan_av_atomerna(), men den funktionen spottar inte ut listan så det sker inte, utan vi kan spela med listan utan att spotta ut den.
        if not self.atomlista:
            gui.visa_meddelande("Spelfel", "Atomlistan är tom. Kunde inte starta spelet.")
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
                gui.visa_meddelande("Spela!", f"Vad har atomen {slumpad_atom.atombeteckning} för atomvikt?")
                svar = str(simpledialog.askstring(f"{slumpad_atom.atombeteckning}", f"A. {en_slumpvald_atom_A.atomvikt}   B. {en_slumpvald_atom_B.atomvikt}   C. {en_slumpvald_atom_C.atomvikt}\nSvar: "))  #simpledialog ser till att användaren får svara, det är som input
                if svar.upper() == 'A': #Baserat på val av svar så kommer en av de 3 atomvikterna väljas
                    vald_vikt = en_slumpvald_atom_A.atomvikt
                elif svar.upper() == 'B':
                    vald_vikt = en_slumpvald_atom_B.atomvikt
                elif svar.upper() == 'C':
                    vald_vikt = en_slumpvald_atom_C.atomvikt

                
                if vald_vikt == slumpad_atom.atomvikt: #Om korrekt
                    gui.visa_meddelande("Rätt Gissat", "Rätt gissat!")
                    break
                else:
                    gui.visa_meddelande("Felaktig Gissning", f"Fel, rätt svar var {slumpad_atom.atomvikt}") #Om ej korrekt
                    break
            except UnboundLocalError:
                gui.visa_meddelande("Ogiltig Inmatning", "Ogiltigt val. Du måste välja A, B eller C.")




def huvudprogram():
    atom_lista_objekt = Atomlista(atomfil='Atomer_UppgB.txt')
    app = Atom_GUI(atom_lista_objekt)
    app.mainloop()

if __name__ == "__main__":
    huvudprogram()


