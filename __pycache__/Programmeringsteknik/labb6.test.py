
while True:
    fil = input("Vad heter filen med alla studenter?: ").strip()
    if fil.lower() == "students.txt":
        break
    else:
        print("Filen verkar inte finnas, skriv in 'students.txt'.")

students = []

with open('students.txt', 'r') as file:
    for line in file:
        students.append(line.strip()) 
    print("Filen är hittad, här är studenterna på KTH: ")
    for i in range(0, len(students), 3):
        group = students[i:i+3]
        print(group[2] + " " + group[1] + ": " + group[0])



print()


sök_namn = input("Vilken student vill du söka efter?: ").lower()
hittad_student = None

for i in range(0, len(students), 3):
    group = students[i:i+3]
    if sök_namn in group[2].lower() or sök_namn in group[1].lower() or sök_namn in group[0]: 
        hittad_student = group
        break

förnamn=hittad_student[2]
efternamn=hittad_student[1]
personnummer=hittad_student[0]

print()


if hittad_student:
    print(f"Studenten hittades:\nNamn: {förnamn} {efternamn}\nPersonnummer: {personnummer}")
else:
    print("Ingen student hittades med det angivna namnet.")