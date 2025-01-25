class Student:
    def __init__(self, förnamn, efternamn, personnummer):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer
    def __repr__ (self):
        return f"{self.förnamn} {self.efternamn}: {self.personnummer}"


print()
print("Okej, dags att lägga till tre studenter: ")
print()

# Lägg till tre studenter
def lägg_till_studenter():
    studenter = []  
    for _ in range(3):
        while True:
            try:
                förnamn, efternamn = input("Skriv studentens för- och efternamn här: ").split()
                if förnamn.isalpha() and efternamn.isalpha():
                    break
                else:
                    print("För- och efternamn måste innehålla enbart bokstäver, försök igen: ")
            except ValueError:
                print("För- och efternamn måste finnas med, försök igen: ")

        while True:
            personnummer = input("Skriv dess 10-siffriga personnummer: ")
            if len(personnummer) == 10 and personnummer.isdigit():
                break
            else:
                print("Du måste skriva ett tio-siffrigt personnummer, försök igen: ")

        student = Student(förnamn, efternamn, personnummer)
        studenter.append(student)  

    return studenter  

print()

# Visa alla studenter i skolan
def visa_studenter(studenter):
    print("Studenter i skolan:")
    for student in studenter:
        print(f"{student.förnamn} {student.efternamn}: {student.personnummer}")

# Använda funktionerna
alla_studenter = lägg_till_studenter()
print()
visa_studenter(alla_studenter)


sök_namn=input("Sök efter en elev: ")
                
