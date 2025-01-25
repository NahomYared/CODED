def int_kontroll(input1=""):
    while True:
            try:
                return int(input(input1))
            except ValueError:
                print(f"Tyvvär, endast heltal.")

def int_kontroll_atomvikt(input2=""):
    while True:
        try:
            return int(input(input2))
        except ValueError:
            print(f"Det var inte ett alternativ, försök igen")