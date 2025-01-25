class School:
    def __init__(self, förnamn, efternamn, personnummer):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer

    def __repr__(self):
        return f"{self.förnamn} {self.efternamn} : {self.personnummer}"

class Student:
    def __init__(self, förnamn, efternamn, personnummer):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer
    
    def __repr__(self):
        return f"Den sökta eleven är\nNamn: {self.förnamn} {self.efternamn}\nPersonnummer:{self.personnummer}"
    

while True:
    fil = input("Vad heter filen med alla studenter?: ").strip()
    if fil.lower() == "students.txt":
        break
    else:
        print("Filen verkar inte finnas, skriv in 'students.txt'.")

lista = []

with open('students.txt', 'r') as file:
    for line in file:
        lista.append(line.strip()) 
    print("Filen är hittad, här är studenterna på KTH: ")
    for i in range(0, len(lista), 3):
        elev=lista[i:i+3]
        fil=School(elev[2], elev[1], elev[0])
        print(repr(fil))

print()

# Sök efter en student
sök_namn = input("Vilken student vill du söka efter?: ").lower()
hittad_student = None

for i in range(0, len(lista), 3):
    elevsökning = lista[i:i+3]
    if sök_namn in elevsökning[2].lower() or sök_namn in elevsökning[1].lower() or sök_namn in elevsökning[0]: 
        Student_väljande=Student(elevsökning[2],elevsökning[1],elevsökning[0])
        print(repr(Student_väljande))
        break
else:
    print("Ingen student hittades med det angivna namnet.")