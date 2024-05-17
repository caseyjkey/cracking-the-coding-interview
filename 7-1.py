# Design the data structures for a generic deck of cards. Explain how you would subclass
# the data structures to implement blackjack.

class Card:
    def __init__(self, suite, identifier):
        self.suite = suite
        self.identifier = identifier

class Deck:
    def __init__(numberCards, shuffle = False):
        self.cards = []
        for i in ['Spades', 'Diamonds', 'Hearts', 'Clubs']:
            for j in range(1, 14):
                if j == 13:
                    identifier = 'King'
                if j == 12:
                    identifier = 'Queen'
                if j == 11:
                    identifier = 'Jack'
                identifier = j
            self.cards.append(Card(i, identifier))
        if shuffle:
            shuffle()

    def shuffle(self):
        return


