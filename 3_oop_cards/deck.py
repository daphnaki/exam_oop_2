import random
from typing import List, override
from ideck import Ideck
from card import Card
from cards_enums import *
from  deck_cheating_error import DeckCheatingError


def fair_deck(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        shuffled_once = self._cards.copy()

        func(self, *args, **kwargs)
        shuffled_twice = self._cards.copy()

        self._cards = shuffled_once

        if shuffled_once == shuffled_twice:
            raise DeckCheatingError("Deck was not shuffled fairly!")

        return self._cards

    return wrapper

class Deck(Ideck):

    def __init__(self,do_shuffle = True):
        self._cards: List[Card] = [Card(suit, rank) for suit in CardSuit for rank in CardRank]
        self._index: int = 0
        if do_shuffle:
            self.shuffle()

    @override
    @property
    def cards(self):
        return self._cards

    @override
    @fair_deck
    def shuffle(self):
        random.shuffle(self._cards)
        return self._cards

    @override
    def draw(self) -> Card:
        if len(self._cards) > 0:
            return self._cards.pop(0)
        return None

    @override
    def add_card(self, card: Card):
        self._cards.append(card)
        return self._cards

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, index) -> Card:
        return self._cards[index]

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self) -> Card:
        if self._index >= len(self._cards):
            raise StopIteration
        card = self._cards[self._index]
        self._index += 1
        return card
