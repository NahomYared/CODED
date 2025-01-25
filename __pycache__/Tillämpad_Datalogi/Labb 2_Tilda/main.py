#Denna är samma som kortlek.py, bara att vi har istället för en så lång kod, endast gjort en modul och importerat klassen.

from LinkedQFile import LinkedQ  # Importera klassen LinkedQ från LinkedQFile

def simulate_cardgame(queue, start_order): #Simulerar korttricket med hjälp av en given kö och startordning.

    queue = LinkedQ()
    for card in start_order:
        queue.enqueue(card)  # Lägg till korten i kön

    result = [] #Lista för resultatet men inkluderar inte korten som loopas
    while not queue.isEmpty():
        #Detta är själva korttricket, loopen flyttar översta kortet till botten och lägger ut nästa kort
        queue.enqueue(queue.dequeue())  # Enqueue:a det som var dequeue:at. Flytta översta kortet till botten, 
        result.append(queue.dequeue())  # Sen efter detta, appenda till listan det nästa som dequeue:as. Alltså Lägg ut nästa kort

    return result

def play_trollkarlsspelet():
    input_cards = input("Ange kortens ordning med mellanrum: ")
    start_order = list(input_cards.split()) # Konvertera input till en lista av kort

    # Skapa en kö med LinkedQ
    queue = LinkedQ()

    # Simulera korttricket
    output_order = simulate_cardgame(queue, start_order)
    print(" ".join(output_order))


if __name__ == "__main__":
    play_trollkarlsspelet()