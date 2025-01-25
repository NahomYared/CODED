#Importerar
import math

class Planet:
    """Class Planet
    En Class som visar planeters egenskaper och räknar ut dess massa
    
    Attributes:
    Planetens_namn: string
        Planetens namn
    Planetens_radie: integer
        planetens radie
    Planetens_omloppstid: integer
        Planetens omloppstid"""
    
    def __init__(self, planetens_namn, planetens_radie, planetens_omloppstid): #Konstruktor
        #Attributen
        self.planetens_namn = planetens_namn
        self.planetens_radie = planetens_radie
        self.planetens_omloppstid = planetens_omloppstid
        self.planetens_massa = None #Det vi ska räkna ut
    
    def omvandla_värden(self): #Metod för att omvandla till rätt enheter
        self.planetens_radie=float(self.planetens_radie*1e6)
        self.planetens_omloppstid=float(self.planetens_omloppstid*3600)
    
    def beräkna_massa(self): #Metod för att beräkna planetens massa och jämföra med jordmassan
        G = 6.67*10**-11
        Jordmassa= 5.977 * 10**24
        self.planetens_massa=(4 * math.pi**2 * self.planetens_radie**3)/(G * self.planetens_omloppstid**2)/Jordmassa
    
    def __str__(self): #specialmetod
        return f"\n Planetens namn: {self.planetens_namn} ||| Planetens vikt i jordmassor: {self.planetens_massa}\n"
    
def läs_fil():
    planeter = []  # Skapa en lokal lista för att lagra objekten
    try:
        with open("planetdata.txt", "r", encoding="utf-8") as file: #Läsa in filen, "with" öppnar och stänger filen automatiskt
            for line in file:
                data=line.strip().split("/") # Dela upp raden med "/" som separator och tar bort onödiga mellanslag
                planetens_namn=data[0].strip()
                planetens_radie=float(data[1].strip())
                planetens_omloppstid=float(data[2].strip())

                planet = Planet(planetens_namn, planetens_radie, planetens_omloppstid) #Skapa objektet planet
                
                planet.omvandla_värden() #Anropa metoden omvandla_värden
                planet.beräkna_massa() #Anropa metoden beräkna_massa

                #lägg till objektet planet i listan planeter
                planeter.append(planet)
    except FileNotFoundError:
        print("Filen kunde inte hittas.")
    return planeter  # Returnera listan med planeter

 
#Huvudprogrammet
def main():
    planeter = läs_fil()  # Få tillbaka listan från öppna_fil()
    for planet in planeter:
        print(planet) #När du anropar print(planet), anropas objektets specialmetod __str__ automatiskt. 
            #Metoden __str__ använder objektets attribut (self.planetens_namn och self.planetens_massa) 
            #för att skapa en strängrepresentation av objektet.


if __name__ == "__main__":
    main()