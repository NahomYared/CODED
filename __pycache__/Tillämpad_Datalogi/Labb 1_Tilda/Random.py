"""Importer numpy modul för att nyttja matematiska uttryck"""
import numpy as np 

class Planet:
    """
    klass Planet 
    ---------------------
    En klass som representerar relevanta egenskaperna av en planet

    Attributes
    ---------
    planetnamn: str
        planetens namn

    omloppstid: int
        planetens omloppstid

    radie: int
        planetens uppmätta radie från sateliten
    """

    def __init__(self, planetnamn, omloppstid, radie):
        """Initialisera klassobjektet med dess tillhörande planetnamn, omloppstid och radie"""
        self.planetnamn = planetnamn
        self.omloppstid = omloppstid
        self.radie = radie
        self.massa = None

    def berakna_massa(self):
        """Beräkna planetens massa m.h.a dess attribut"""
        jordmassa = 5.977 * 10**24
        self.massa = ((self.radie * (10**6)) **3)*(4*np.pi**2)/((6.67 * (10 ** -11)*((self.omloppstid * 3600)**2)))
        self.massa = self.massa/jordmassa
        return self.massa

    def __str__(self):
        """ Returnerar en string representation av planetens namn, massa (om beräknad), omloppstid och radie """
        return f"{self.planetnamn} väger {self.massa} jordmassor" # {self.omloppstid} {self.radie}"


def inlasning():
    """Filinläsning för att inmata planetens parametrar och skapa klassobjekt"""
    try:
        with open('planetdata.txt', encoding='utf-8') as fil:
            rader = [rad.strip() for rad in fil.readlines() if rad.strip()]  # Strip tomma rader
    except FileNotFoundError:
        print("Error: Filen 'planetdata.txt' hittas inte")
        return []

    tmplist = []
    for i in range(0, len(rader), 2): 
        try:
            planetnamn = rader[i]
            param_raden = rader[i + 1]
            radie, omloppstid = map(float, param_raden.split('/')) #Applicerar funktionen float på varje element i "param_raden.split('/')"
            tmp = Planet(planetnamn, omloppstid, radie)
            tmplist.append(tmp)
        except (ValueError, IndexError):
            continue
    return tmplist

def main():
    """Huvudprogram"""
    planeterna = inlasning()
    for planeten in planeterna:
        planeten.berakna_massa()  #Beräkna massan av klassobjektet (planeten)
    return planeterna

if __name__ == '__main__':
    print("\n")
    planets = main()
    for planet in planets:
        print(planet)
    print("\n")