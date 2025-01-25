from collections import deque

class ArrayQ:
    def __init__(self):
        self._queue = deque()  # Använd deque för att hantera kön

    def enqueue(self, x):
        self._queue.append(x)  # Lägg till element sist i kön

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")  # Hantera tom kö
        return self._queue.popleft()  # Ta bort och returnera första elementet (FIFO)

    def isEmpty(self):
        return len(self._queue) == 0  # Kontrollera om kön är tom

    def size(self):
        return len(self._queue)  # Returnera antalet element i kön


def simulate_trick(queue, start_order):
    """
    Simulerar korttricket med hjälp av en given kö och startordning.
    """
    for card in start_order:
        queue.enqueue(card)  # Lägg till korten i kön

    result = []
    while not queue.isEmpty():
        queue.enqueue(queue.dequeue())  # Flytta översta kortet till botten
        result.append(queue.dequeue())  # Lägg ut nästa kort

    return result


if __name__ == "__main__":
    # Mata in startordningen
    input_cards = input("Ange kortens startordning: ")
    start_order = list(map(int, input_cards.split()))

    # Skapa en kö med ArrayQ
    queue = ArrayQ()

    # Simulera korttricket
    output_order = simulate_trick(queue, start_order)
    print("Korten läggs ut i denna ordning:", " -> ".join(map(str, output_order)))

    # Kontrollera om korten är i korrekt ordning
    correct_order = list(range(1, len(start_order) + 1))
    if output_order == correct_order:
        print("Korten är i korrekt ordning!")
    else:
        print("Testa olika startordningar för att få rätt resultat.")
