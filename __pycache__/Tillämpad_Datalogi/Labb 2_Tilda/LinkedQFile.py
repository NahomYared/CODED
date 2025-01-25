class Node:
    """
    Class Node
    En klass som representerar en enskild nod i en länkad lista. 

    Attributes:
    value : any
        Det värde som noden lagrar, vilket kan vara av valfri datatyp.
    next : Node or None
        En pekare som refererar till nästa nod i den länkade listan.
        Om det inte finns någon nästa nod (slutet på listan), är värdet None.
    """
    def __init__(self, value):
        self.value = value  # Noden håller ett värde
        self.next = None    # Pekar på nästa nod (initialt None)

class LinkedQ:
    """
    Class LinkedQ
    En klass som implementerar en kö (queue) med hjälp av en länkad lista.

    Attributes:
    _first : Node or None
        Referens till den första noden i kön. Om kön är tom är värdet None.
    _last : Node or None
        Referens till den sista noden i kön. Om kön är tom är värdet None.
    _size : int
        Antalet element i kön.
    """
    def __init__(self):
        self._first = None  # Första noden i kön är none, den existerar inte
        self._last = None   # Sista noden i kön är none, den existerar inte
        self._size = 0      # Håller koll på antalet noder i kön, initialt 0

    def enqueue(self, x):
        new_node = Node(x)  # Skapa en ny nod med värdet x, som ska läggas till i kön
        if self.isEmpty():  # Fall 1: Kön är tom
            self._first = new_node # Första noden blir den nya noden
            self._last = new_node #Den nya noden blir även den sista
        else:  # Fall 2: Kön är inte tom från innan
            self._last.next = new_node  # Den sista noden i den existerande kön pekar på new_node och den blir den nya noden längst bak
            self._last = new_node       # Nu är den nytillkomna noden OFFICIELLT den sista noden
        self._size += 1  #Öka antalet element i kön med 1

    def dequeue(self):
        if self.isEmpty(): # Om kön är tom
            raise IndexError("dequeue:a från en tom kö")  # Hantera tom kö
        value = self._first.value  # Value är det första värdet i kön
        self._first = self._first.next  # Det nästa värdet (värdet efter det förra) i kön blir OFFICIELLT det första värdet eftersom den som var först lämnar
        if self._first is None:  # Om det inte finns något kvar i kön, dvs om kön är tom
            self._last = None # Sista noden blir None
        self._size -= 1 # Minska antalet element i kön med 1, eftersom detta bara är processen för att lämna
        return value

    def isEmpty(self):
        return self._first is None  # True om kön är tom, annars False

    def size(self):
        return self._size  # Returnera antalet element i kön


