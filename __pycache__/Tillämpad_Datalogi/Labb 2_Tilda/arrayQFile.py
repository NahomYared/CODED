from array import array  # Importera array-modulen för att använda array-objekt

class ArrayQ:  # Klassdefinition för ArrayQ¨
    
    """
    Class ArrayQ
    En klass som implementerar en kö (queue) med hjälp av en array.

    Denna klass följer FIFO-principen (First In, First Out), vilket innebär
    att det första elementet som läggs till i kön också är det första som tas bort.
    Klassen använder en array för att lagra elementen i kön.

    Attributes:
    -----------
    _queue : array
        En array av typen 'i' (heltal) som används för att lagra köns element.
    """

    def __init__(self):  # Konstruktor
        self._queue = array('i', [])  # Initiera en tom array för heltal ('i' står för integer)

    def enqueue(self, x):  # Metod för att lägga till element i kön
        self._queue.append(x)  # Lägg till element x sist i kön (arrayen)

    def dequeue(self):  # Metod för att ta bort element från kön
        if self.isEmpty():  # Kontrollera om kön är tom
            raise IndexError("dequeue:a från tom kö")  # Om kön är tom, kasta ett undantag
        return self._queue.pop(0)  # Ta bort och returnera det första elementet i kön (FIFO-principen)

    def isEmpty(self):  # Metod för att kontrollera om kön är tom
        return len(self._queue) == 0  # Returnera True om kön är tom, annars False
     # En metod som håller koll på antalet element i kön 
    
    def size(self):
        return len(self._queue)
