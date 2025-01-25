class Student:
    def __init__(self, förnamn, efternamn, personnummer):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer

    def __str__(self):
        return f"Namn: {self.förnamn} {self.efternamn}, personnr: {self.personnummer}"


class Skola:
    def __init__(self):
        self.studentlista = []

    def skriv_ut_studenterna(self, filnamn):
        with open(filnamn, 'r', encoding="utf-8") as studentfil:
            while True:
                personnummer = studentfil.readline().strip()
                if not personnummer:
                    break
                efternamn = studentfil.readline().strip()
                förnamn = studentfil.readline().strip()
                person = Student(förnamn, efternamn, personnummer)
                self.studentlista.append(person)
        return self.studentlista

    def leta_student(self, objekt):
        leta_objekt = []
        for student in self.studentlista:
            if objekt.lower() in student.förnamn.lower() or objekt.lower() in student.efternamn.lower():
                leta_objekt.append(student)
        return leta_objekt


def ditt_val():
    while True:
        print("Vill du fortsätta Ja/Nej? ")
        val = input().lower()
        if val== "ja" or val=="nej":
            return val
        else:
            print("Det var inget alternativ, skriv rätt")


def skriv_filnamn():
    while True:
        filnamn = input("Vad heter filen med alla studenter? ")
        try:
            with open(filnamn, 'r'):
                break
        except FileNotFoundError:
            print("Filen kunde inte hittas, försök igen!")
    return filnamn


def huvudprogram():
    skola = Skola()
    filnamn = skriv_filnamn()
    skola.skriv_ut_studenterna(filnamn)

    print("\nDessa studenter är skrivna på KTH\n")
    for student in skola.studentlista:
        print(student)
    print()
    print("Nu ska du få söka efter studenter.")

    while True:
        student_namn = input("Skriv förnamn eller efternamn på den student du vill söka efter: ")
        matchande_namn = skola.leta_student(student_namn)
        if len(matchande_namn) == 0:
            print(f"\nHittade inga matchningar för {student_namn} i KTH:s system\n")
        else:
            for namn in matchande_namn:
                print(f"\nDen studenten läser på KTH: \n{namn}\n \n")
        val = ditt_val().lower()
        if val == "nej":
            exit(0)


# Call huvudprogram to start the program
huvudprogram()
