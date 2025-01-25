print()

class Student:
    def __init__ (self, förnamn, efternamn, personnummer):
        self.förnamn=förnamn
        self.efternamn=efternamn
        self.personnummer=personnummer

    def __repr__ (self):
        return f"{self.förnamn} {self.efternamn}: {self.personnummer}"

print("Vi ska nu skriva namn och personnummer till tre studenter!")

print()

while True:
        try:
            student1_förnamn,student1_efternamn = input("Skriv första studentens för- och efternamn här: ").split()
            if  student1_förnamn.isalpha() and student1_efternamn.isalpha():
                break
            else:
                print("För- och efternamn måste innehålla enbart bokstäver, försök igen: ")
        except ValueError:
            print("För- och efternamn måste finnas med, försök igen: ")
            
while True:
        student1_personnummer = input("Skriv dess 10-siffriga personnummer: ")
        if len(student1_personnummer) == 10 and student1_personnummer.isdigit():
            break
        else:
            print("Du måste skriva ett tio-siffrigt personnummer, försök igen: ")


print()

print ("Bra första studenten är avklarad, dags för andra studenten!")

print()

while True:
    try:
        student2_förnamn,student2_efternamn = input("Skriv andra studentens för- och efternamn här: ").split()
        if  student2_förnamn.isalpha() and student2_efternamn.isalpha():
            break
        else:
            print("För- och efternamn måste innehålla enbart bokstäver, försök igen: ")
    except ValueError:
        print("För- och efternamn måste finnas med, försök igen: ")

while True:
    student2_personnummer = input("Skriv dess 10-siffriga personnummer: ")
    if len(student2_personnummer) == 10 and student2_personnummer.isdigit():
        break
    else:
        print("Du måste skriva ett tio-siffrigt personnummer, försök igen: ")

print()

print("Tack, andra studenten är också avklarad. Dags för den sista studenten!")

print()

while True:
    try:
        student3_förnamn,student3_efternamn = input("Skriv första studentens för- och efternamn här: ").split()
        if  student3_förnamn.isalpha() and student3_efternamn.isalpha():
            break
        else:
            print("För- och efternamn måste innehålla enbart bokstäver, försök igen: ")
    except ValueError:
        print("För- och efternamn måste finnas med, försök igen: ")

while True:
    student3_personnummer = input("Skriv dess 10-siffriga personnummer: ")
    if len(student3_personnummer) == 10 and student3_personnummer.isdigit():
        break
    else:
        print("Du måste skriva ett tio-siffrigt personnummer, försök igen: ")

print ("Tack, tredje eleven avklarad, nu är alla elever avklarade. Här är en lista på dem: ")

print()
    
def huvudprogram():
        studentlista=lägg_in_elever()
        studentlista.append(Student(student1_förnamn, student1_efternamn, student1_personnummer))
        lista.append(Student(student2_förnamn, student2_efternamn, student2_personnummer))
        lista.append(Student(student3_förnamn, student3_efternamn, student3_personnummer))

        for student in lista:
            print (student)
    
if __name__ == "__main__":
    huvudprogram()