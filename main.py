import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(r) for r in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.Cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __str__(self):
        for r in self.Cards:
            print(f"{r}\n")
        return ""

    def __getitem__(self, item):
        return self.Cards[item]

    def __len__(self):
        return len(self.Cards)

    def __contains__(self, item):
        return any(item == m for m in self.Cards)


deck = FrenchDeck()
print(len(deck))
print(deck[9::13])

listing = [i for i in range(0, 50)]
print(listing)
print(listing[5::6])

print(Card('Q', 'hearts') in deck)
print("---------------")
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


print("---------------")
card = deck[13]
print(card)
print(spades_high(card))
print("---------------")
print("Deck Sorting: ")
for card in sorted(deck, key=spades_high):
    print(card)
