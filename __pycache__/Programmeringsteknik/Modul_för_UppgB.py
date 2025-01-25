class Atom:
    def __init__(self, beteckning, vikt, rad, kolonn):
        self.beteckning = beteckning
        self.vikt = vikt
        self.rad = rad
        self.kolonn = kolonn
        self.nummer = None


    def skapa_atomlista():
        atomlista = []
        with open('Atomer_UppgB.txt', 'r') as atomfil:
            for line in atomfil:
                beteckning, vikt, rad, kolonn = line.strip().split()
                atomlista.append(Atom(beteckning, float(vikt), int(rad), int(kolonn)))

        atomlista.sort(key=lambda atom: atom.vikt)

        for i, atom in enumerate(atomlista, start=1):
            atom.nummer = i

        Atom.byt_plats_och_nummer(atomlista, 'Ar', 'K')
        Atom.byt_plats_och_nummer(atomlista, 'Co', 'Ni')
        Atom.byt_plats_och_nummer(atomlista, 'Te', 'I')
        Atom.byt_plats_och_nummer(atomlista, 'Th', 'Pa')
        Atom.byt_plats_och_nummer(atomlista, 'U', 'Np')

        return atomlista

    def byt_plats_och_nummer(atomlista, beteckning1, beteckning2):
        atom1 = next(atom for atom in atomlista if atom.beteckning == beteckning1)
        atom2 = next(atom for atom in atomlista if atom.beteckning == beteckning2)

        index1, index2 = atomlista.index(atom1), atomlista.index(atom2)
        atomlista[index1], atomlista[index2] = atomlista[index2], atomlista[index1]

        atom1.nummer, atom2.nummer = atom2.nummer, atom1.nummer


def visa_atomlista():   
    nummerad_atomlista = Atom.skapa_atomlista() 
    for atom in nummerad_atomlista:
        print(f"Beteckning: {atom.beteckning}, Vikt: {atom.vikt}, Nummer: {atom.nummer}, Rad: {atom.rad}, Kolonn: {atom.kolonn}")



