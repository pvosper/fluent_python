#!/usr/bin/env python

import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


print('Examples:')

print("\tbeer_card = Card('7', 'diamonds')")
beer_card = Card('7', 'diamonds')

print('\tbeer_card: {}'.format(beer_card))

print('\tdeck = FrenchDeck()')
deck = FrenchDeck()

print('\tlen(deck): {}'.format(len(deck)))

print('\tdeck[0]: {}'.format(deck[0]))

print('\tdeck[-1]: {}'.format(deck[-1]))

print('\tfrom random import choice')
from random import choice

print('\tchoice(deck): {}'.format(choice(deck)))

print('\tchoice(deck): {}'.format(choice(deck)))

print('\tchoice(deck): {}'.format(choice(deck)))

print('\tdeck[:3]: {}'.format(deck[:3]))

for card in deck:
    print('\t{}'.format(card))

print("\tCard('Q', 'hearts') in deck: {}".format(Card('Q', 'hearts') in deck))

print("\tCard('Q', 'beasts') in deck: {}".format(Card('Q', 'beasts') in deck))
