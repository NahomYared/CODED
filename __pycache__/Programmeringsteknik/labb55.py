class Student:
    def __init__(self, förnamn, efternamn, personnummer):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer

        

######################
class School:
    def __init__(self):
        self.studenter = []

    def lägg_till_student(self, student):
        self.studenter.append(student)

# Skapa en skola
min_skola = School()
##########################



# Lägg till tre studenter
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
    min_skola.lägg_till_student(student)

print("Okej, tre studenter är nedskrivna\n")

# Visa alla studenter i skolan
print("Studenter i skolan:")
for student in min_skola.studenter:
    print(f"{student.förnamn} {student.efternamn}: {student.personnummer}")




###################################
# Sök efter en student
sök_namn = input("Vilken student vill du söka efter?: ")
hittad_student = None

for student in min_skola.studenter:
    if sök_namn.lower() in f"{student.förnamn.lower()} {student.efternamn.lower()}":
        hittad_student = student
        break


if hittad_student:
    print(f"Studenten hittades: {hittad_student.förnamn} {hittad_student.efternamn}: {hittad_student.personnummer}")
else:
    print("Ingen student hittades med det angivna namnet.")
#######################################