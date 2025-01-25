from array import array  # Importera array-modulen för att använda array-objekt

class ArrayQ:  # Klassdefinition för ArrayQ
    def __init__(self):  # Konstruktor
        self._queue = array('i', [])  # Initiera en tom array för heltal ('i' står för integer)

    def enqueue(self, x):  # Metod för att lägga till element i kön
        self._queue.append(x)  # Lägg till element x sist i kön (arrayen)

    def dequeue(self):  # Metod för att ta bort element från kön
        if self.isEmpty():  # Kontrollera om kön är tom
            raise IndexError("dequeue from empty queue")  # Om kön är tom, kasta ett undantag
        return self._queue.pop(0)  # Ta bort och returnera det första elementet i kön (FIFO-principen)

    def isEmpty(self):  # Metod för att kontrollera om kön är tom
        return len(self._queue) == 0  # Returnera True om kön är tom, annars False
     # En metod som håller koll på antalet element i kön 
    
    def size(self):
        return len(self._queue)
    
q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")
