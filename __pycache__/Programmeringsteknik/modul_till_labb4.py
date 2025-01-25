

def läs_student():
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

    return förnamn, efternamn, personnummer